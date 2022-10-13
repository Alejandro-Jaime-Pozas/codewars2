# Your job is to write a function which increments a string, to create a new string.

# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.
# Examples:

# foo -> foo1

# foobar23 -> foobar24

# foo0042 -> foo0043

# foo9 -> foo10

# foo099 -> foo100

# Attention: If the number has leading zeros the amount of digits should be considered.


# def increment_string(string):
#     # okay, so take the string, iterate to check if c is letter, add to letters list, number to numbers list
#     # once you have a numbers list, join numbers, add + 1 to that number (but what if 0's before?)
#         # leading 0s Not Permitted. So will have to add leading 0s to strings list or split from numbers list...could do a count to check for 0s, if 0 after letter, change count to 1, if no longer 0, change count to 2
#     # NUMBERS COULD BE BETWEEN LETTERS, ONLY COUNT CONSECUTIVE LAST NUMBERS
#     # IF 099, THEN + 1 WOULD BE 100 NOT 0100
#     # ALSO, 000 SHOULD EQUAL 001 NOT 0001
#     count = 0
#     letters = ''
#     numbers = ''
#     for i, c in enumerate(string[::-1]):
#         if c.isnumeric() and count == 0:
#             numbers += c
#         else:
#             count = 1
#             letters += c
#     # need to check if numbers starts with 0s,
#     letters = letters[::-1] 
#     numbers = numbers[::-1]
#     if not numbers:
#         numbers = '1'
#     else:
#         plus_one = str(int(numbers) + 1) # this removes leading 0s
#         if len(numbers) <= len(plus_one):
#             numbers = plus_one
#         else:
#             numbers = numbers[0:(len(numbers)-len(plus_one))] + plus_one
#     return ''.join(letters + numbers)

# print(increment_string('foo'))
# print(increment_string('foobar23'))
# print(increment_string('foo0042'))
# print(increment_string('fo99o099'))
# print(increment_string('fo99o0099'))
# print(increment_string('fo99o009899'))


# def scramble(s1, s2):
#     # do a dict approach
#     chars = {}
#     for c in set(s1):
#         chars[c] = s1.count(c)
#     for c in s2:
#         if c in chars:
#             chars[c] -= 1
#         else:
#             return False
#         if chars[c] < 0:
#             return False
#     return True

# print(scramble('cedewaraaossoqqyt', 'codewars'))


# def zeros(n):
#     # factorial:
#     # need to multiply successive integers up to given number input
#     # zeros(3) = 1 * 2 * 3 = 6 -> zero 0s
#     # order doesn't matter, can go from up to down
#     # start with n, then go down n-1 until that == 1
#     # need to multiply each n * n-1...
#     if n == 1:
#         print('n is at end: 1')
#         return prod
#     else:
#         print(f'n is {n}')
#         prod = n * zeros(n-1)

# print(zeros(6))


# def first_non_repeating_letter(string):
#     # logic: check the entire string for chars, count them, look for first non-repeating
#     # lower same as upper, but return accordingly
#     # i'm thinking a for loop to create a dict of chars, then another for loop afterwards to check dict items vs non-dict
#     # chars = {}
#     # for c in string:
#     #     if c.lower() in chars:
#     #         chars[c.lower()] = chars[c.lower()] + 1
#     #     else:
#     #         chars[c.lower()] = 1
    
#     # for c in string:
#     #     if chars[c.lower()] == 1:
#     #         return c
#     # return ''
#     for c in string:
#         print(string.index(c))

# print(first_non_repeating_letter([1, 2, 3, 2, 4, 2, 5, 2]))
# print(first_non_repeating_letter('sTreSS'))

# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"


# def domain_name(string):
    # need to check if '.' on either side to indicate start/finish of domain name
    # need to check if before '.' there is http:// or www
    #  can check if string before is '/' then take whatever is after until there is a '.'
    # domain = ''
    # if 'www' in string:
    #     # check where first '.' is, return whatever comes after
    #     dots = 0
    #     for c in string:
    #         if c == '.' and dots == 0:
    #             dots += 1
    #             continue
    #         elif c == '.' and dots != 0:
    #             break
    #         if dots == 1:
    #             domain += c
    # elif 'http' in string:
    #     http = ''
    #     for c in string:
    #         if c in {':', '/'}:
    #             http += c
    #             continue
    #         elif c == '.':
    #             break
    #         if http == '://':
    #             domain += c
    # else:
    #     for c in string:
    #         if c == '.':
    #             break
    #         else:
    #             domain += c
    # return domain
#     return string.split('www.')


# print(domain_name("https://youtube.com"))
# print(domain_name("https://www.you-tube.com"))
# print(domain_name("www.you-tube.com"))

# ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.

# Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

# def rot13(message):
#     # need to loop through each 
#     rot = ''
#     for c in message:
#         # if c is not a letter, add it to rot
#         if not c.isalpha():
#             rot += c
#         # if c is a letter, add 13 in alphabet
#         if c.isalpha():
#             # if c is in capital range
#             if ord(c) in range(65, 90 + 1):
#                 # if c less than 'N' do c + 13, else -13
#                 if ord(c) < 78:
#                     rot += chr(ord(c) + 13)
#                 else:
#                     rot += chr(ord(c) - 13)
#             # if c is in lowercase range
#             elif ord(c) in range(ord('a'), ord('z') + 1):
#                 # if c less than 'n' do c + 13, else -13
#                 if ord(c) < ord('n'):
#                     rot += chr(ord(c) + 13)
#                 else:
#                     rot += chr(ord(c) - 13)

#     return rot


# print(rot13('aA bB zZ 1234 *!?%'))


# 65 A
# 77 M
# 78 N
# 90 Z

# 97 a
# 109 m
# 110 n
# 122 z