import numpy as np
import matplotlib.pyplot as plt


def calculate_mandelbrot(region_params, image_size, max_iterations):
    xmin, xmax, ymin, ymax = region_params
    width, height = image_size

    real = np.linspace(xmin, xmax, width)
    imag = np.linspace(ymin, ymax, height)
    c = real[:, np.newaxis] + 1j * imag[np.newaxis, :]
    z = np.zeros_like(c)
    div_time = np.zeros(c.shape, dtype=int)

    mask = np.full(c.shape, True, dtype=bool)

    for i in range(max_iterations):
        z[mask] = z[mask]**2 + c[mask]
        mask_new = np.abs(z) <= 2
        div_now = mask & (~mask_new)
        div_time[div_now] = i
        mask = mask_new

    div_time[div_time == 0] = max_iterations
    return div_time.T


if __name__ == "__main__":
    REGION = (-2.5, 1.5, -2.0, 2.0)
    SIZE = (800, 800)
    MAX_ITER = 300

    image = calculate_mandelbrot(REGION, SIZE, MAX_ITER)

    plt.figure(figsize=(8, 8))
    plt.imshow(image, cmap='twilight_shifted',
               extent=[REGION[0], REGION[1], REGION[2], REGION[3]])
    plt.colorbar(label='Количество итераций')
    plt.title("Множество Мандельброта")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()
