
from transformer import transform_text, denormalize_and_convert_back
from depend import depends
from encode_transformer import encode_text
from normalize import normalize, denormalize
from signal import signal_build, calculate_frft, plot_signal_build, plot_reconstructed_signal, reproduce_normalized_encoded_text
from frft_math import frft, frft_plot, calculate_inverse_frft, inverse_frft

import numpy as np
import matplotlib.pyplot as plt
import math

import sys


def main():
    plain_text = "jaivik"
    print(plain_text)

    transformed_text = transform_text(plain_text)
    print(transformed_text)

    text_size, k, m, c = depends(plain_text)
    print(text_size)

    encoded_text = encode_text(plain_text, k, m, c)
    print(encoded_text)

    normalized_encoded_text = normalize(encoded_text)
    print(normalized_encoded_text)

    # Generate the composite signal
    composite_signal = signal_build([normalized_encoded_text], m, k)
    plot_signal_build(composite_signal)

    alpha = math.sqrt(k/m)  # Define your alpha value

    # Calculate the Fractal Fourier Transform
    frft_result = calculate_frft(composite_signal, alpha, k, m)
    # Visualize the FrFT (optional)
    frft_plot(frft_result, alpha)

    # Assuming you already have frft_result and alpha
    reconstructed_signal = inverse_frft(frft_result, alpha)
    # Assuming you already have reconstructed_signal, frft_result, and alpha
    plot_reconstructed_signal(reconstructed_signal, frft_result, alpha)

    reproduced_text = reproduce_normalized_encoded_text(reconstructed_signal, m, k)
    print(reproduced_text)

'''    denormalized_text = denormalize(reproduced_text, encoded_text)
    print(denormalized_text)

    # Convert denormalized values back to text
    decoded_text = [chr(int(round(float(x)) + ord('A'))) for x in denormalized_text]
    decoded_text = ''.join(decoded_text)

    # Now you can print non-ASCII characters without encoding errors.
    print("Decoded Text:", decoded_text)
'''


if __name__ == "__main__":
    main()

