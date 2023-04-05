import numpy as np
from tabulate import tabulate

# Задаем начальные и граничные условия
def implicit_scheme(T=1.0, L=1.0, N=100, M=100, name="2-2.txt"):
    dx = L / N
    dt = T / M
    x = np.linspace(0, L, N+1)
    t = np.linspace(0, T, M+1)
    u = np.zeros((M+1, N+1))
    u[0, :] = np.exp(x)

    # Задаем коэффициенты для метода прогонки
    a = b = np.zeros(N-1) - 1
    c = np.zeros(N-1) + 2

    # Вычисляем прогоночные коэффициенты для каждого временного слоя
    for n in range(1, M+1):
        d = np.zeros(N-1)
        d[0] = u[n-1, 1] + dt/(dx**2) * u[n, 0]
        d[-1] = u[n-1, -2] + dt/(dx**2) * u[n, -1]
        for i in range(1, N-2):
            d[i] = u[n-1, i+1]
        # Решаем систему методом прогонки
        c_star = np.zeros(N-1)
        d_star = np.zeros(N-1)
        c_star[0] = c[0] / b[0]
        d_star[0] = d[0] / b[0]
        for i in range(1, N-1):
            c_star[i] = c[i] / (b[i] - a[i-1] * c_star[i-1])
            d_star[i] = (d[i] - a[i-1] * d_star[i-1]) / \
                (b[i] - a[i-1] * c_star[i-1])
        # Вычисляем решение на текущем временном слое
        u[n, -1] = np.exp(t[n] + 1)
        u[n, 0] = np.exp(t[n])
        for i in range(N-2, 0, -1):
            u[n, i] = d_star[i] - c_star[i] * u[n, i+1]

    np.set_printoptions(threshold=np.inf)
    f = open(name, "w")
    print(tabulate(u), file=f)


if __name__ == "__main__":
    implicit_scheme(1.0, 1.0, 10, 10, "2-1.txt")
    implicit_scheme(1.0, 1.0, 1000, 1000, "2-2.txt")
