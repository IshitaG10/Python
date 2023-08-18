from art import logo



def ceaser(text , shift,direction):
    if direction == "decode":
        shift*=-1
    s =[]
    for c in text:
        if c not in alphabet:
            s.append(c)
            continue
        idx = alphabet.index(c)
        new_pos = idx+shift
        if new_pos > 25:
            new_pos-= 26
        if new_pos <0:
            new_pos+=26
        s.append(alphabet[new_pos]) 
    ciphered = ""
    for c in s:
        ciphered += c

    print(ciphered)



print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while(True):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26
    ceaser(text,shift,direction)
    repeat = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if repeat == "no":
        break