# Import and display the ASCII logo from art.py at program start
from art import logo
print(logo)

# List of lowercase letters used for the Caesar cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
            'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    """
    Encrypts or decrypts text using the Caesar cipher.
    Keeps numbers, spaces, and symbols unchanged.
    """
    output_text = ""

    # If decoding, reverse the shift direction
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        # If character is not a letter, keep it unchanged
        if letter not in alphabet:
            output_text += letter

        # Otherwise, shift the letter within the alphabet
        else:
            shifted_position = alphabet.index(letter) + shift_amount

            # Wrap around the alphabet if index goes out of range
            shifted_position %= len(alphabet)

            output_text += alphabet[shifted_position]

    print(f"Here is the {encode_or_decode}d result: {output_text}")


# Loop to allow the user to restart the program multiple times
should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Ask the user if they want to run the program again
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye!")
