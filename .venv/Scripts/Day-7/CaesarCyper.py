import alphabet

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt \n").lower
text = input("Type your message: \n").lower
shift = int(input("Type the shift number: \n"))




def encode(original_text, shift_amount):
    cyper = ""
    for letter in original_text:
        shift_positon = alphabet.alphabet_letter.index(letter) + shift_amount
        #in case of shift position is grater then len of alphabet
        shift_positon %= len(alphabet.alphabet_letter)
        cyper += alphabet.alphabet_letter[shift_positon + 1]
    print(f"Here is the encoded result: {cyper}\n")

def decode(original_text, shift_amount):
    cyper = ""
    for letter in original_text:
        shift_positon = alphabet.alphabet_letter.index(letter) - shift_amount
        # in case of shift position is grater then len of alphabet
        shift_positon %= len(alphabet.alphabet_letter)
        #added +1 because shift is not done correctly
        cyper += alphabet.alphabet_letter[shift_positon + 1]
    print(f"Here is the  result: {cyper}\n")

def caesar(original_text, shift_amount, encode_or_decode):
    cyper = ""
    for letter in original_text:
        if encode_or_decode == "decode":
            shift_amount *= -1
        shift_positon = alphabet.alphabet_letter.index(letter) + shift_amount
        # in case of shift position is grater then len of alphabet
        shift_positon %= len(alphabet.alphabet_letter)
        cyper += alphabet.alphabet_letter[shift_positon]
    print(f"Here is the {encode_or_decode} result: {cyper}\n")



#encode("z", shift_amount=shift)
#decode("z", shift_amount=shift)
#Hardcoded beacuse original_text and encoded_or_decoded doesnt work as intended
caesar(original_text="a", shift_amount=shift, encode_or_decode="decode")