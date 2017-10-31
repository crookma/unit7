# By: Magnus Crooke, File Name: unit7.py, last modified 10-31-17
# This program encoded or decodes a phrase that user inputs into the program
alphabet = "abcdefghijklmnopqrstuvwxyz"


def main():
    """
    This function runs the rotation cipher.
    """
    start()


def start():
    """
    This function asks the user of the would like to encode, decode or quit and runs the program on which function they
    would like to do.
    """
    choice = input("Press e to encode, d to decode or q to quit:")
    if choice == "e":
        encode()
    elif choice == "d":
        decode()


def encode():
    """
    This function asks the user to input a phrase, and then asks them how much they would like to shift the phrase.
    :return:This function returns the shifted sentence.
    """
    blank = ""
    e = input("Please write a phrase to be encoded:")
    shift_number = int(input("How much would you like to shift the letters?(0 - 25)"))
    for letter in e:
        if letter == " ":
            blank = blank + letter
        else:
            new_num = (alphabet.index(letter) + shift_number) % 26
            new_letter = alphabet[new_num]
            blank = blank + new_letter
    print(blank)


def decode():
    """
    This function asks the user to input an encoeded phrase, and then asks them how much they would like to shift the
    phrase.
    :return:This function returns the decoded phrase.
    """
    focus = ""
    d = input("Please write a phrase to be decoded:")
    shiftnum = int(input("How much would you like to shift the letters?(0 - 25)"))
    for letter in d:
        if letter == " ":
            focus = focus + letter
        else:
            number = (alphabet.index(letter) + 26 - shiftnum) % 26
            letters = alphabet[number]
            focus = focus + letters
    print(focus)

main()
