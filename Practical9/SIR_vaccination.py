import numpy as np
import matplotlib.pyplot as plt


def sSIR(v):

    N = 10000
    I = 1
    R = v * N  
    S = N - I - R 
    beta = 0.3
    gamma = 0.05
    T = [ I ] 

    for t in range(1000):
        s = np.random.binomial(S, beta * I / N)
        r = np.random.binomial(I, gamma)
        i = s - r
        S -= s
        I += i
        R += r
        T.append( I )
    return T

plt.figure(figsize=(10,5))


V = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]



for v in V:
    plt.plot(sSIR(v),
             linewidth=3,
             label=f' {v:.0%}',
             color=plt.cm.RdYlGn(v))

plt.legend()
plt.title('SIR Model with Vaccination')
plt.xlabel('time')
plt.ylabel('infected number')
plt.show()



    


