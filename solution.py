"""
Author: John Asare
Date and time: 2023-08-09 20:47

Read the README.md file for a detailed description of the project.

"""

# import the string file
import string


# defined a function to hold the solution
def solution(encrypted_message):
    # get the alphabets from the string library.
    alphabet_list = list(string.ascii_lowercase)
    # print as a check-up to make sure the alphabet are stored as list.
    print(alphabet_list)
    # reversed the alphabet and make it as a list.
    alphabet_reversed = list(reversed(alphabet_list))
    # print as a check point to make the alphabet are indeed reversed.
    print(alphabet_reversed)

    message = ""
    for letter in encrypted_message:
        if letter == alphabet_reversed:
            get_decrypted_letter_index = alphabet_reversed.index(letter)
            message += get_decrypted_letter_index
        else:
            message += get_decrypted_letter_index
    return message


solution("vmxibkgrlm")
