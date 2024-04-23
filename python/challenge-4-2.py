
import random 
import string 


char = " " + string.ascii_letters + string.digits + string.punctuation

char = list(char)

key = char.copy()

#[' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
# 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#  '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', 
# ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

random.shuffle(key)

# ['}', '&', 'F', 'V', '@', 'G', '6', '*', 'C', '5', 's', '^', 'J', '8', '~', '1', 'R', '{', '`', '7', '>',
#  '9', '.', 'p', 'v', '\\', 'e', '/', 'd', ' ', '(', 'c', 'O', 'a', 'j', '!', '0', 'A', ',', 'y', '=', 'g', 'x', 'Q', '%', 'w',
#    'm', 'f', 'h', 'n', '-', ':', ')', '2', 'S', 'k', '<', 'I', '?', 'b', 'l', "'", 'U', '+', '"', 'Z', 'u', 'W', 'X', '$', 'T', 'N', 'q', '|', 'o', 'D', 'z', 'r', 
#  ';', '#', 'L', 'E', 'i', 'M', '3', ']', '_', 'P', '4', 't', '[', 'Y', 'K', 'H', 'B']

plain_text = input("Enter your message for the encryption : ")

cipher_text = ""

for letter in plain_text:

    index = char.index(letter) #0

    cipher_text += key[index] #key[0]

print( f"Your original message : {plain_text}")
print( f"Your encrypted message : {cipher_text}")  


# DECRYPT

plain_text = ""

for letter in cipher_text:

    index = key.index(letter) 

    plain_text += char[index]

print( f"Your encrypted message : {cipher_text}")    
print( f"Your original message : {plain_text}") 
