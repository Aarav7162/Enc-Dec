def caesar_encrypt(text, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']
    
    encrypted = ""
    text = text.lower()

    for char in text:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + key) % 26
            encrypted += alphabet[new_index]
        else:
            encrypted += char
    
    return encrypted

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

message = input("Enter a message: ")
key = int(input("Enter the key (shift number): "))

encrypted = caesar_encrypt(message, key)
print("Encrypted message:", encrypted)

decrypted = caesar_decrypt(encrypted, key)
print("Decrypted message:", decrypted)
