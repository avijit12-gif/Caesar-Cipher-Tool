def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main_simulated_input(input_choices):
    print("Caesar Cipher Tool")
    input_index = 0

    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        if input_index >= len(input_choices):
            print("No more inputs provided.")
            break

        choice = input_choices[input_index]
        input_index += 1
        print(f"Enter your choice (1/2/3): {choice}")

        if choice == "1":
            if input_index + 1 >= len(input_choices):
                print("Insufficient input for encryption.")
                break

            message = input_choices[input_index]
            input_index += 1
            print(f"Enter the message to encrypt: {message}")

            try:
                shift = int(input_choices[input_index])
                input_index += 1
                print(f"Enter the shift value (integer): {shift}")

                encrypted_message = caesar_cipher_encrypt(message, shift)
                print(f"Encrypted Message: {encrypted_message}")
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")
        elif choice == "2":
            if input_index + 1 >= len(input_choices):
                print("Insufficient input for decryption.")
                break

            message = input_choices[input_index]
            input_index += 1
            print(f"Enter the message to decrypt: {message}")

            try:
                shift = int(input_choices[input_index])
                input_index += 1
                print(f"Enter the shift value (integer): {shift}")

                decrypted_message = caesar_cipher_decrypt(message, shift)
                print(f"Decrypted Message: {decrypted_message}")
            except ValueError:
                print("Invalid input. Please enter an integer for the shift value.")
        elif choice == "3":
            print("Exiting the tool. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    try:
        # Simulated input for testing purposes.
        simulated_inputs = ["1", "hello", "3", "2", "khoor", "3", "3"]
        main_simulated_input(simulated_inputs)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
