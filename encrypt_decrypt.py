alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"Encoded text is :{cipher_text}")


def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"Decoded text is:{plain_text}")
'''
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:")
text = input("Type your message:").lower()
shift = int(input("Type number of shifts:"))
'''
if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)
elif direction == 'decode':
    decrypt(cipher_text=text, shift_amount=shift)
'''


# Combined function-->>

def caeser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabet.index(letter)
        if cipher_direction == 'decode':
            shift_amount *= -1
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction} text is {end_text}")
