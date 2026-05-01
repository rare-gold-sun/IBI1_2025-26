import numpy as np
import matplotlib.pyplot as plt

N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
T = [ [S, I, R] ] 

for t in range(1000):
    s = np.random.binomial(S, beta * I / N)
    r = np.random.binomial(I, gamma)
    i = s - r
    S -= s
    I += i
    R += r
    T.append( [S, I, R] )


T = np.array(T)
plt.plot(T[:,0], label='S')
plt.plot(T[:,1], label='I')
plt.plot(T[:,2], label='R')
plt.legend()
plt.title('stochastic SIR Model')
plt.xlabel('time')
plt.ylabel('people number')
plt.show()






    


