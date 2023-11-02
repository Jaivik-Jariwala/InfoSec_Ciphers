import numpy as np
import matplotlib.pyplot as plt


def frft(signal, alpha):
    N = len(signal)
    result = np.zeros(N, dtype=complex)

    for m in range(N):
        for n in range(N):
            angle = alpha * m * n * np.pi / N
            result[m] += signal[n] * np.exp(-1j * angle)

    return result   

def frft_plot(frft_result, alpha):
    # Plot the Fractal Fourier Transform
    frequencies = np.arange(len(frft_result))
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, np.abs(frft_result))
    plt.title(f"Fractal Fourier Transform (alpha={alpha})")
    plt.xlabel("Frequency Component")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

def calculate_inverse_frft(frft_result, alpha, k, m):
    # Calculate the inverse Fractal Fourier Transform
    inverse_alpha = 1.0 / alpha  # Use the inverse of the original alpha
    inverse_frft_result = calculate_frft(frft_result, inverse_alpha, k, m)

    return inverse_frft_result

def inverse_frft(frft_result, alpha):
    N = len(frft_result)
    result = np.zeros(N, dtype=complex)

    for m in range(N):
        for n in range(N):
            angle = alpha * m * n * np.pi / N
            result[m] += frft_result[n] * np.exp(1j * angle)

    return result
