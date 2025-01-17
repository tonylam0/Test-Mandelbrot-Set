import numpy as np
import pygame


class Bounds:
    SCALE = 350
    power = 2

    # Creates a range for real and imaginary numbers
    # Increasing the amount of points increases the accuracy
    points = 1000
    real_range = np.linspace(-2, 1, int(points))
    imag_range = np.linspace(-1.5, 1.5, int(points))

    # Creates a 2D grid for the complex plane
    real, imag = np.meshgrid(real_range, imag_range)

    # Outputs a list of lists containing real array + imaginary array * j
    c_values = real + imag * 1j
    iterations = np.zeros(c_values.shape)
    coordinates = {}

    escape_radius = 2

    # Used to update values when power is set
    def update():
        Bounds.points = 1000 * Bounds.power
        real_range = np.linspace(-2, 1, int(Bounds.points))
        imag_range = np.linspace(-1.5, 1.5, int(Bounds.points))

        real, imag = np.meshgrid(real_range, imag_range)

        Bounds.c_values = real + imag * 1j
        Bounds.iterations = np.zeros(Bounds.c_values.shape)
        Bounds.coordinates = {}
    
    # Mandelbrot's recursive formula
    # c represents a complex number 
    def calc():
        # Will return numbers of points in ranges
        for real in range(Bounds.c_values.shape[0]):
            print(f"Computing: {int(real/Bounds.points*100+1)}% done")
            for imag in range(Bounds.c_values.shape[1]):
                z = 0
                c = Bounds.c_values[real, imag]  # Treated as coordinate in the 2D plane
                max_iterations = 100
                Bounds.coordinates[(real, imag)] = 0

                for i in range(max_iterations):
                    z = z**Bounds.power + c
                    
                    # Tracks when z unbounds
                    # i > 0 prevents escaped c's to be colored the same as bounded
                    if abs(z) > Bounds.escape_radius and i > 0:
                        Bounds.iterations[real, imag] = i
                        Bounds.coordinates[real, imag] = i
                        break
    
    def draw(win):
        for coordinate, i in Bounds.coordinates.items():
            c = Bounds.c_values[coordinate[0], coordinate[1]] 
            color = (
                i * 5 % 255, 
                i * 10 % 255, 
                i * 15 % 255
            )

            pygame.draw.circle(
                win, 
                color, 
                (c.real * Bounds.SCALE + 1400 / 2, c.imag * Bounds.SCALE + 800 / 2),
                1
            )