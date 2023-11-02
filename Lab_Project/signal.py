from transformer import transform_text
from depend import depends
from encode_transformer import encode_text
from normalize import normalize
from frft_math import frft, frft_plot
import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(amplitude, angular_frequency, t, phase_difference):
    return amplitude * np.sin(angular_frequency * t + phase_difference)

def signal_build(normalized_encoded_texts, m, k):
    angular_frequency = np.sqrt(k / m)
    t = np.linspace(0, np.pi, len(normalized_encoded_texts[0]))
    phase_difference = 0
    composite_signal = np.zeros(len(t))
    
    for normalized_encoded_text in normalized_encoded_texts:
        sine_wave = generate_sine_wave(normalized_encoded_text, angular_frequency, t, 0)
        composite_signal += sine_wave

    return composite_signal

def plot_signal_build(composite_signal):
    # Plot the signal produced by signal_build function
    plt.plot(np.arange(len(composite_signal)), composite_signal)
    plt.title("Signal Build Result")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.show()

def calculate_frft(composite_signal, alpha, k, m):
    # Calculate the Fractal Fourier Transform
    frft_result = frft(composite_signal, alpha)
    
    # Add the plotting code here if you want to visualize the FrFT
    frequencies = np.arange(len(frft_result))
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, np.abs(frft_result))
    plt.title(f"Fractal Fourier Transform (alpha={alpha})")
    plt.xlabel("Frequency Component")
    plt.ylabel("Amplitude")
    plt.tight_layout()
    plt.show()

    return frft_result

def plot_reconstructed_signal(reconstructed_signal, frft_result, alpha):
    plt.figure(figsize=(8, 4))

    # Plot the reconstructed signal
    plt.subplot(1, 2, 1)
    plt.plot(np.arange(len(reconstructed_signal)), reconstructed_signal)
    plt.title("Reconstructed Signal")
    plt.xlabel("Time")
    plt.ylabel("Amplitude")

    # Plot the original FrFT result
    plt.subplot(1, 2, 2)
    frequencies = np.arange(len(frft_result))
    plt.plot(frequencies, np.abs(frft_result))
    plt.title(f"Original Fractal Fourier Transform (alpha={alpha})")
    plt.xlabel("Frequency Component")
    plt.ylabel("Amplitude")

    plt.tight_layout()
    plt.show()

def reproduce_normalized_encoded_text(reconstructed_signal, m, k):
    # Calculate the angular frequency
    angular_frequency = np.sqrt(k / m)
    t = np.linspace(0, np.pi, len(reconstructed_signal))
    
    # Initialize an array to store the reproduced normalized encoded text
    reproduced_normalized_encoded_text = np.zeros(len(reconstructed_signal))
    
    for i in range(len(reconstructed_signal)):
        # Calculate the sine wave at each time point
        sine_wave = generate_sine_wave(reconstructed_signal[i], angular_frequency, t[i], 0)
        reproduced_normalized_encoded_text[i] = sine_wave

    return reproduced_normalized_encoded_text