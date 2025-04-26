import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    c = real[:, np.newaxis] + 1j * imag[np.newaxis, :]
    z = np.zeros_like(c)
    div_time = np.zeros(c.shape, dtype=int)

    mask = np.full(c.shape, True, dtype=bool)

    for i in range(max_iter):
        z[mask] = z[mask]**2 + c[mask]
        mask_new = np.abs(z) <= 2
        div_now = mask & (~mask_new)
        div_time[div_now] = i
        mask = mask_new

    div_time[div_time == 0] = max_iter
    return div_time.T 

if __name__ == "__main__":
    xmin, xmax = -2.5, 1.5
    ymin, ymax = -2.0, 2.0
    width, height = 800, 800
    max_iter = 300

    image = mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='twilight_shifted', extent=[xmin, xmax, ymin, ymax])
    plt.colorbar(label='Количество итераций')
    plt.title("Множество Мандельброта")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()
