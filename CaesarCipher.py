alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
           
def CaesarCipher(text, shift, direction):
    ciphered_text = ""
    for character in text:
        if character in alphabet:
            character_ind = alphabet.index(character)
            if direction == "encode":
                if character_ind+shift > len(alphabet)-1:
                    character_ind = character_ind - (len(alphabet)) #avoid index out of range
                ciphered_text += alphabet[character_ind+shift]
            else:
                if character_ind-shift < 0:
                    character_ind = character_ind + (len(alphabet)) #avoid index out of range
                ciphered_text += alphabet[character_ind-shift]
        else:
            ciphered_text += character
    print(f"{direction}d text is: {ciphered_text}")

run_cipher = True
while(run_cipher):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%len(alphabet) #avoid index out of range
    
    CaesarCipher(text, shift, direction)
    
    if input("Type 'yes' if you want to go again. Otherwise, type 'no': ").lower() == "yes": 
        run_cipher=True 
    else: 
        run_cipher=False