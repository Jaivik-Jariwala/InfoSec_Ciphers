def denormalize(normalized_value, min_value, max_value, new_min, new_max):
    # Calculate the original value from the normalized value
    original_value = (normalized_value - new_min) / (new_max - new_min) * (max_value - min_value) + min_value
    return original_value

# Example usage:
normalized_encoded_text = [0.1, 0.3, 0.5, 0.7, 0.9]

# Denormalize the values back to the original range
original_min = min(encoded_text)
original_max = max(encoded_text)
new_min = 1
new_max = 7000
original_encoded_text = [denormalize(value, original_min, original_max, new_min, new_max) for value in normalized_encoded_text]

print("Original Encoded Text:", original_encoded_text)
