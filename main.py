alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(text,shift):

    encrypted_text=''
    for i in text:
        index=alphabet.index(i)
        new_text=(shift+index)%26
        new_index=alphabet[new_text]
        encrypted_text+=new_index
    print(f"Your encrypted text is: {encrypted_text}")

encrypt(text,shift)

