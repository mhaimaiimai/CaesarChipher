alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    text_encrypted = ""
    for character in text:
        character_ind = alphabet.index(character)
        if character_ind+shift > len(alphabet)-1:
            character_ind = character_ind - (len(alphabet))
        text_encrypted += alphabet[character_ind+shift]
    return text_encrypted

def decrypt(text, shift):
    text_decoded = ""
    for character in text:
        character_ind = alphabet.index(character)
        if character_ind-shift < 0:
            character_ind = character_ind + (len(alphabet))
        text_decoded += alphabet[character_ind-shift]
    return text_decoded
        
def CaesarCipher():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    if direction == "encode":
        text_encrypted = encrypt(text, shift)
        print(f"Encrypted text: {text_encrypted}")
    else:
        text_decoded = decrypt(text, shift)
        print(f"Decrypted text: {text_encrypted}")

CaesarCipher()