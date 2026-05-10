# Make a grid with 100 rows and 100 columns.
# 0 means a healthy person,
# 1 means a sick person,
# 2 means a recovered person.
# Pick one random cell in the grid and make it sick (1).
# Repeat the following steps for many days:
# a. Find all cells that are sick right now.
# b. For each sick cell, look at its 8 neighbors (up, down, left, right, and the 4 corners).
# c. If a neighbor is healthy (0), try to make it sick:
# Use a random chance (based on "beta") to decide if it becomes sick (1).
# d. For every sick cell, also give it a chance to get better:
# Use another random chance (based on "gamma") to turn it into recovered (2).
# e. Save the new state of the whole grid, and optionally draw a picture of it.


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

beta, gamma, steps = 0.3, 0.05, 100
P = np.zeros((100, 100))
i0, j0 = np.random.choice(100, 2)
P[i0, j0] = 1

history = [P.copy()]

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
    history.append(P.copy())



plt.figure(figsize=(12,8))
for idx, t in enumerate([0, 10, 30, 50, 70, 100]):
    plt.subplot(2, 3, idx+1)
    plt.imshow(history[t], cmap='viridis', vmin=0, vmax=2)
    plt.title(f"Step {t}")
    plt.axis('off')
legend_patches = [
    mpatches.Patch(color=plt.cm.viridis(0), label='Susceptible'),
    mpatches.Patch(color=plt.cm.viridis(0.5), label='Infected'),
    mpatches.Patch(color=plt.cm.viridis(1.0), label='Recovered')
]
plt.figlegend(handles=legend_patches, loc='lower right', bbox_to_anchor=(0.9, 0.1))
plt.suptitle("Spatial SIR", fontsize=16)
plt.tight_layout()
plt.show()