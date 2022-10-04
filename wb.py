def first_non_repeating_letter(string):
    # logic: check the entire string for chars, count them, look for first non-repeating
    # lower same as upper, but return accordingly
    # i'm thinking a for loop to create a dict of chars, then another for loop afterwards to check dict items vs non-dict
    # chars = {}
    # for c in string:
    #     if c.lower() in chars:
    #         chars[c.lower()] = chars[c.lower()] + 1
    #     else:
    #         chars[c.lower()] = 1
    
    # for c in string:
    #     if chars[c.lower()] == 1:
    #         return c
    # return ''
    for c in string:
        print(string.index(c))

print(first_non_repeating_letter([1, 2, 3, 2, 4, 2, 5, 2]))
print(first_non_repeating_letter('sTreSS'))

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