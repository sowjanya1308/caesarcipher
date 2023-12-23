alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n")) 

#encrypting the code
def encrypt(plain_text,shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new = position + shift_amount
        cipher_text += alphabet[new]
    print(f"The encoded text is {cipher_text}")

#decrypting the code
def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new = position - shift_amount
        plain_text += alphabet[new]
    print(f"The decoded text is {plain_text}") 

#Using direction 
if direction == "encode":
    encrypt(plain_text = text, shift_amount = shift)
elif direction == "decode":
    decrypt(cipher_text = text, shift_amount = shift) 

