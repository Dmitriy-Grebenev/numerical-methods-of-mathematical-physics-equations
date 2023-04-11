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
        ksi = np.zeros(N-1)
        ksi[0] = u[n-1, 1] + dt/(dx ** 2) * u[n, 0]
        ksi[-1] = u[n-1, -2] + dt/(dx ** 2) * u[n, -1]
        for j in range(1, N - 2):
            ksi[j] = u[n - 1, j + 1]
        # Решаем систему методом прогонки
        alpha = np.zeros(N-1)
        beta = np.zeros(N-1)
        alpha[0] = c[0] / b[0]
        beta[0] = ksi[0] / b[0]
        for j in range(1, N - 1):
            alpha[j] = -a[j] / (b[j] + c[j] * alpha[j - 1])
            beta[j] = (ksi[j] - c[j - 1] * beta[j - 1]) / \
                (b[j] + c[j] * alpha[j - 1])
        # Вычисляем решение на текущем временном слое
        u[n, -1] = np.exp(t[n] + 1)
        u[n, 0] = np.exp(t[n])
        for j in range(N-2, 0, -1):
            u[n, j] = beta[j] + alpha[j] * u[n, j + 1]

    np.set_printoptions(threshold=np.inf)
    f = open(name, "w")
    print(tabulate(u), file=f)


if __name__ == "__main__":
    implicit_scheme(1.0, 1.0, 10, 10, "2-1.txt")
    implicit_scheme(1.0, 1.0, 1000, 1000, "2-2.txt")
