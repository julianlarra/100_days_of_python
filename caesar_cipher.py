alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', ]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# caesar cipher: the code allows you to choose between "encrypt" and "decrypt". then enter the text you want to encode or decode adjusted by the offset number.


def called_caesar(plain_text, shift_amount, direction_enc):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if direction == "encode":
            new_position = position + shift_amount
            answer = "encoded"
        elif direction == "decode":
            new_position = position - shift_amount
            answer = "decoded"
        cipher_text += alphabet[new_position]

    print(f"The {answer} text is {cipher_text}")


shift = shift % 27

called_caesar(plain_text=text, shift_amount=shift, direction_enc=direction)
restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
if restart == "no":
    print("Goodbye")

while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    called_caesar(plain_text=text, shift_amount=shift, direction_enc=direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")