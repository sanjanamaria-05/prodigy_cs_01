def caesar_encrypt(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():  
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption Program")
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (integer): "))

    choice = input("Do you want to (E)ncrypt or (D)ecrypt the message? ").lower()

    if choice == 'e':
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted_message}")
    elif choice == 'd':
        decrypted_message = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please choose 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()
