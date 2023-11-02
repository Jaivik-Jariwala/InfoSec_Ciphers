def normalize(encoded_text):
    # Find the minimum and maximum values in the encoded_text
    min_value = min(encoded_text)
    max_value = max(encoded_text)

    # Define the desired normalization range
    new_min = 0
    new_max = 1

    # Normalize the values
    normalized_encoded_text = [(x - min_value) / (max_value - min_value) * (new_max - new_min) + new_min for x in encoded_text]

    return normalized_encoded_text

def denormalize(normalized_encoded_text, encoded_text):
    # Find the minimum and maximum values in the original encoded_text
    min_value = min(encoded_text)
    max_value = max(encoded_text)

    # Define the desired normalization range
    new_min = 0
    new_max = 1

    # Denormalize the values
    denormalized_encoded_text = [(x - new_min) / (new_max - new_min) * (max_value - min_value) + min_value for x in normalized_encoded_text]

    return denormalized_encoded_text
