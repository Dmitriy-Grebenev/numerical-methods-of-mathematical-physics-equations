import numpy as np
from tabulate import tabulate

# Задаем начальные и граничные условия
def explicit_scheme(T=1.0, L=1.0, N=100, M=100, name="1-1.txt"):
    dx = L / N
    dt = T / M
    x = np.linspace(0, L, N+1)
    t = np.linspace(0, T, M+1)
    u = np.zeros((M+1, N+1))
    #u = np.arange(N*M).reshape(N, M)
    u[0, :] = np.exp(x)

    for n in range(M):
        for i in range(1, N):
            u[n+1, i] = u[n, i] + dt/dx**2 * \
                (u[n, i+1] - 2*u[n, i] + u[n, i-1])
        u[n+1, 0] = np.exp(t[n+1])
        u[n+1, -1] = np.exp(t[n+1]+1)

    np.set_printoptions(threshold=np.inf)
    f = open(name, "w")
    print(tabulate(u), file=f)


if __name__ == "__main__":
    explicit_scheme(1.0, 1.0, 10, 10, "1-1.txt")
    explicit_scheme(1.0, 1.0, 1000, 1000, "1-2.txt")
