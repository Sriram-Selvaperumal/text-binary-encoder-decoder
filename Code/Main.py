def string_to_binary(input_string):
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    binary_list = []
    for char in input_string:
        ordinal_value = ord(char)
        binary_char = bin(ordinal_value)[2:].zfill(8)
        binary_list.append(binary_char)
    return " ".join(binary_list)

def binary_to_string(binary_string):
    if not isinstance(binary_string, str):
        raise TypeError("Input must be a string.")

    binary_segments = binary_string.split(" ")
    decoded_chars = []

    for segment in binary_segments:
        if not all(c in '01' for c in segment) or len(segment) != 8: # Added len check for strict 8-bit segments
            raise ValueError(f"Invalid binary segment found: '{segment}'. "
                             "Binary string should only contain 8-bit '0' or '1' sequences separated by spaces.")
        
        decimal_value = int(segment, 2)
        decoded_char = chr(decimal_value)
        decoded_chars.append(decoded_char)
    
    return "".join(decoded_chars)

if __name__ == "__main__":
    while True:
        print("\n--- Choose an option ---")
        print("1. Convert String to Binary")
        print("2. Convert Binary to String")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            user_string = input("Enter the string you want to convert to binary: ")
            try:
                encoded_binary = string_to_binary(user_string)
                print(f"Encoded Binary: '{encoded_binary}'")
            except TypeError as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            user_binary = input("Enter the binary string (space-separated 8-bit sequences): ")
            try:
                decoded_text = binary_to_string(user_binary)
                print(f"Decoded String: '{decoded_text}'")
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


