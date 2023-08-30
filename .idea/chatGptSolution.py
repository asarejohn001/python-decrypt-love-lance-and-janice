#push
def solution(s):
    deciphered = ''

    for char in s:
        if 'a' <= char <= 'z':
            deciphered += chr(ord('z') - (ord(char) - ord('a')))
        else:
            deciphered += char

    return deciphered


# Example usage
coded_message = "vmxibkgrlm"
decoded_message = solution(coded_message)
print(decoded_message)  # Output will be: "encryption"
