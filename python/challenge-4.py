#Caesar cipher

plain_text = input("Enter your message for the encryption : ")

#Encryption
key = 3

cipher_text = ""

for character in plain_text:
    x = ord(character)

    if character == ' ':
        cipher_text += ' '
    else:
        cipher_text += chr(x + key)
        
print("Encrypt :" , cipher_text)

# Decryption
key = 3
plain_text = ""
for character in cipher_text:
    x = ord(character)

    if character == ' ':
        plain_text += ' '
    else:
        plain_text += chr(x - key)
print("Decrypt: " ,plain_text)