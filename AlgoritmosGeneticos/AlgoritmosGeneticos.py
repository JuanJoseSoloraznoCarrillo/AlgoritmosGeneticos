import numpy as np
import random
import matplotlib.pyplot as plt


individuos=10
N=individuos
bits = 10


X = np.zeros([N,bits])

for i in range(N):
  for j in range (bits):
    X[i,j]=random.randint(0,1)


numDec  = np.zeros(N)
T = 0

for p in range(N):
  for u in range(bits):
    if X[p,u]==1:
      numDec[p] += 2**(9-u)  
  T += numDec[p] 
  
r = np.zeros(N)

for j in range (N):
   r[j] = random.randint(1,T)


print(X)
print('individuos: ',numDec)
print('T:          ',T)
print('r:          ',r)

indiv = numDec[0]
padreGana1 = np.zeros(N)

for b in range(N):
  i=0
  while indiv < r[b]:
    indiv += numDec[i+1]
    i += 1
  padreGana1[b] = numDec[i]
  print('padreRuleta = ',padreGana1[b])  
  indiv=numDec[0]

print('VecPadreRuleta ',padreGana1 )





padreGana = np.zeros(N)

for i in range(N):
  J = np.random.randint(0,9)
  H = np.random.randint(0,9)
  # print(J,H)
  padre_1 = numDec[J]
  padre_2 = numDec[H]
  # print(padre_1)
  # print(padre_2)
  if padre_1<padre_2:
      padreGana[i] = padre_2
  elif padre_1 == padre_2:
     padreGana[i] = padre_1
  else:
     padreGana[i] = padre_1
  print('PadreTorneo = ',padreGana[i])


print('VecPadreTorneo: ', padreGana)
print('VecPadreRuleta: ', padreGana1)



frecc = {}
frecc2 = {}
for n in padreGana:
  if n in frecc:
    frecc[n] += 1
  else:
    frecc[n] = 1

for n in padreGana1:
  if n in frecc2:
    frecc2[n] += 1
  else:
    frecc2[n] = 1

print('FrecuanciaPorTorneo',frecc)
print('FrecuenciaPorRuleta',frecc2)

equals = np.zeros(N)
i = 0
for g in padreGana:
  if g in padreGana1:
    equals[i] = g
    i +=1


print(equals)