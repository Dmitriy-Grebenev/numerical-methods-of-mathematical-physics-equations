import numpy as np
from tabulate import tabulate

start_x = 0
end_x = 1
start_t = 0
end_t = 1

#Значение шага по t
dt = 0.001

#Задаём значение шага по x, исходя из условия устойчивости 
# h^2  >= 2 * dt
h = 0.1

#Число шагов по x
N_j = int((end_x - start_x)/h + 1)
#Число шагов по t
N_n = int((end_t - start_t)/dt + 1)
u = np.zeros([N_n, N_j])

#Задаём начальные условия
for j in range(N_j):
    u[0, j] = np.exp((j - 1) * h)

for n in range(N_n - 1):
    for j in range(2, N_j - 1):
        u[n + 1, j] = u[n, j] + dt/(h ** 2) * \
                (u[n, j + 1] - 2 * u[n, j] + u[n, j - 1])
    u[n + 1, 0] = np.exp((n + 1) * dt)
    u[n + 1, -1] = np.exp((n + 1) * dt + 1)

f = open("list1.txt", "w")

# for n in range(N_n - 1):
#     for j in range(2, N_j - 1):
#         print(u[n, j], end="\t", file=f)
#     print(file=f)

print(tabulate(u), file=f)
