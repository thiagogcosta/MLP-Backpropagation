''' Nome: Thiago Aparecido Gonçalves da Costa    R.A.:537241
          Leonardo Ademir Tonezi dos Santos      R.A.:540201
          João Ricardo Ito Messias               R.A.:536814
'''
from random import uniform
from math import pow

''' *******************Declaração de Variáveis*************************** '''
'inicialização das sinapses'
wx0h1 = uniform(-1,1)
wx1h1 = uniform(-1,1)
wx1h2 = uniform(-1,1)
wx2h1 = uniform(-1,1)
wx2h2 = uniform(-1,1)
wx0h2 = uniform(-1,1)
wh1o1 = uniform(-1,1)
wh2o1 = uniform(-1,1)
wx0o1 = uniform(-1,1)

'constantes'
e = 2.7182818284590455;
eta = 0.2
alpha = 0.2

'zerando as variáveis'
uH1 = 0
uH2 = 0
uO1 = 0
yH1 = 0
yH2 = 0
yO1 = 0
x0 = 1
Dx0h1 = 0
Dx1h1 = 0
Dx1h2 = 0
Dx2h1 = 0
Dx2h2 = 0
Dx0h2 = 0
Dh1o1 = 0
Dh2o1 = 0
Dx0o1 = 0
            
'padrões e desejaveis:'
padroes = [[0,0],[0,1],[1,0],[1,1]]
desejavel = [0,1,1,0]

''' ************************Função Saída******************************** '''

def Y(entradas):
    global wx0h1, wx1h1, wx2h1, yH1, wx0h2, wx1h2, wx2h2, yH2, wx0o1, wh1o1, wh2o1
    uH1 = wx0h1 + entradas[0] * wx1h1 + entradas[1] * wx2h1
    yH1 = 1 / (1 + pow(e,-uH1))
    uH2 = wx0h2 + entradas[0] * wx1h2 + entradas[1] * wx2h2
    yH2 = 1 / (1 + pow(e,-uH2))
    uO1 = wx0o1 + yH1 * wh1o1 + yH2 * wh2o1
    yO1 = 1 / (1 + pow(e,-uO1))
    return yO1

''' ******************************************************************** '''

''' **************************Função MSE******************************** '''
def MSE(padroes, desejavel):
    soma = 0
    for i in range(0, 4):
        soma = soma + pow(desejavel[i] - Y(padroes[i]),2)
    return soma/4

''' ******************************************************************** '''

''' **************************Função Treinamento************************ '''
def Treinamento(eta, alpha, padroes, desejavel):
    epoca = 0
    while True:
        print(MSE(padroes,desejavel))
        if MSE(padroes,desejavel) < 0.01 or epoca > 10000:
            print ("Treinamento Finalizado!")
            print ("Esforço de: " + repr(epoca))
            break
        epoca += 1
        for i in range(0, 4):

            'buscando as vars globais'
            global wh1o1, yH1, wh2o1, yH2, x0
            
            'delta do O1'
            Saida = Y(padroes[i])
            Erro = desejavel[i] - Saida
            deltaO1 = (Saida * (1 - Saida)) * Erro
                    
            'delta do H1'
            deltaH1 = (yH1 * (1 - yH1)) * wh1o1 * deltaO1
            
            'delta do H2'
            deltaH2 = (yH2 * (1 - yH2)) * wh2o1 * deltaO1

            'calculo dos gradientes'
            Gx0h1 = deltaH1 * x0
            Gx1h1 = deltaH1 * padroes[i][0]
            Gx1h2 = deltaH2 * padroes[i][0]
            Gx2h1 = deltaH1 * padroes[i][1]
            Gx2h2 = deltaH2 * padroes[i][1]
            Gx0h2 = deltaH2 * x0
            Gh1o1 = deltaO1 * yH1
            Gh2o1 = deltaO1 * yH2 
            Gx0o1 = deltaO1 * x0

            'buscando as vars globais'
            global Dx0h1,wx0h1,Dx1h1,wx1h1,Dx1h2,wx1h2,Dx2h1,wx2h1,Dx2h2,wx2h2,Dx0h2,wx0h2,Dh1o1,wh1o1,Dh2o1,wh2o1,Dx0o1,wx0o1
            
            'atualização de pesos'            
            Dx0h1 = eta * Gx0h1 + alpha * Dx0h1
            wx0h1 = wx0h1 + Dx0h1

            Dx1h1 = eta * Gx1h1 + alpha * Dx1h1
            wx1h1 = wx1h1 + Dx1h1
            
            Dx1h2 = eta * Gx1h2 + alpha * Dx1h2
            wx1h2 = wx1h2 + Dx1h2
        
            Dx2h1 = eta * Gx2h1 + alpha * Dx2h1
            wx2h1 = wx2h1 + Dx2h1
            
            Dx2h2 = eta * Gx2h2 + alpha * Dx2h2
            wx2h2 = wx2h2 + Dx2h2
           
            Dx0h2 = eta * Gx0h2 + alpha * Dx0h2
            wx0h2 = wx0h2 + Dx0h2
            
            Dh1o1 = eta * Gh1o1 + alpha * Dh1o1
            wh1o1 = wh1o1 + Dh1o1
        
            Dh2o1 = eta * Gh2o1 + alpha * Dh2o1
            wh2o1 = wh2o1 + Dh2o1
        
            Dx0o1 = eta * Gx0o1 + alpha * Dx0o1
            wx0o1 = wx0o1 + Dx0o1
            
            
''' ******************************************************************** '''
print ('RECONHECENDO A PORTA LÓGICA XOR')
print ('**********SEM TREINAMENTO**********')
print (' 0 - 0  = '+repr(Y([0,0])))
print (' 0 - 1  = '+repr(Y([0,1])))
print (' 1 - 0  = '+repr(Y([1,0])))
print (' 1 - 1  = '+repr(Y([1,1])))
print ('***********************************')
Treinamento(eta,alpha,padroes,desejavel)
print ('**********COM TREINAMENTO**********')
print (' 0 - 0  = '+repr(Y([0,0])))
print (' 0 - 1  = '+repr(Y([0,1])))
print (' 1 - 0  = '+repr(Y([1,0])))
print (' 1 - 1  = '+repr(Y([1,1])))
print ('***********************************')



