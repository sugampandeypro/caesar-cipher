alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, original_text, shift_amount):
    result_text = ""

    # If decode, reverse the shift
    if direction == "decode":
        shift_amount = -shift_amount

    for letter in original_text:
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            result_text += alphabet[shifted_position]
        else:
            result_text += letter  # keep spaces and symbols

    print(f"Here is the result: {result_text}")


# User input
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Call the single function
caesar(direction, text, shift)

