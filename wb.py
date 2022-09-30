# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

def rot13(message):
    # need to loop through each 
    rot = ''
    for c in message:
        # if c is not a letter, add it to rot
        if not c.isalpha():
            rot += c
        # if c is a letter, add 13 in alphabet
        if c.isalpha():
            # if c is in capital range
            if ord(c) in range(65, 90 + 1):
                # if c less than 'N' do c + 13, else -13
                if ord(c) < 78:
                    rot += chr(ord(c) + 13)
                else:
                    rot += chr(ord(c) - 13)
            # if c is in lowercase range
            elif ord(c) in range(ord('a'), ord('z') + 1):
                # if c less than 'n' do c + 13, else -13
                if ord(c) < ord('n'):
                    rot += chr(ord(c) + 13)
                else:
                    rot += chr(ord(c) - 13)

    return rot


print(rot13('aA bB zZ 1234 *!?%'))


# 65 A
# 77 M
# 78 N
# 90 Z

# 97 a
# 109 m
# 110 n
# 122 z