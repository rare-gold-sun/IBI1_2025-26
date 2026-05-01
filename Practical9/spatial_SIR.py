import numpy as np
import matplotlib.pyplot as plt

beta, gamma, steps = 0.3, 0.05, 100
P = np.zeros((100, 100))
i0, j0 = np.random.choice(100, 2)
P[i0, j0] = 1

for _ in range(steps):
    P_new = P.copy()
    for i in range(100):
        for j in range(100):
            if P[i, j] == 1:
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == dj == 0:
                            continue
                        ni, nj = i + di, j + dj
                        if 0 <= ni < 100 and 0 <= nj < 100:
                            if P[ni, nj] == 0 and np.random.rand() < beta:
                                P_new[ni, nj] = 1
                if np.random.rand() < gamma:
                    P_new[i, j] = 2
    P = P_new

plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(P, cmap='viridis', interpolation='nearest')
plt.title("Spatial SIR 8-neighbor")
plt.show()