def solution(s):
    # split a string in pairs. if odd, then last c paired w "_"
    if len(s) % 2 != 0:
        s += "_"
    final = []
    for i in range(0, len(s), 2):
        final.append(s[i:i+2])
    return final 

print(solution("asdfadsfg"))


# def is_pangram(s):
#     # grab alpha only and lowercase. how to check for all leters?
#     # can start by looping through
#     letters = list('abcdefghijklmnopqrstuvwxyz')
#     for c in s.lower():
#         if c in letters:
#             letters.remove(c)
#         if len(letters) == 0:
#             return True
#     return False 

# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


# def adjacent_element_product(array):
#     # the other way is to run through entire list...which is needed since you need to check ALL pairs in order to determine you have the max..
#     max = None 
#     for i in range(len(array)-1):
#         # take the first num and adjacent to the right
#         if max == None or array[i] * array[i+1] > max:
#             max = array[i] * array[i+1]
#     return max 

# print(adjacent_element_product([-23, 4, -5, 99, -27, 329, -2, 7, -921]))


# def sum_of_n(n):
#     running = 0
#     lst = []
#     for i in range(abs(n)+1):
#         if n > 0:
#             running += i 
#         else:
#             running -= i
#         lst.append(running)
#     return lst

# print(sum_of_n(3)) # [0,1,3,6]


# def shorter_reverse_longer(a,b):
#     # a + reverse(b) + a
#     if len(a) >= len(b):
#         return f'{b}{a[::-1]}{b}'
#     return f'{a}{b[::-1]}{a}'
    
    
# print(shorter_reverse_longer('abcabc', 'longerer'))


# def find_digit(num, nth):
#     #your code here
#     # grab absolute value of num
#     # if nth < 0 return -1
#     # if out of index, return 0
#     if nth <= 0:
#         return -1
#     elif nth > len(str(num)):
#         return 0
#     else:
#         return int(str(abs(num))[::-1][nth-1])

# print(find_digit(5673, 4))
# print('hello there')


# def vaporcode(s):
#     return '  '.join(list(''.join(s.upper().split(' '))))
                

# print(vaporcode("Why isn't my code working?"))


# def add(x):
#     def add_more(y):
#         print(add, add_more)
#         return x + y
#     print(add, add_more)
#     return add_more

# add_5 = add(5)
# print(add_5(1)) # Output: 15


# def multiply_all(lst):
#     return lambda multiplier: [n ** multiplier for n in lst]
#     # def multiply_by(multiplier):
#     #     return [num * multiplier for num in lst]
#     # return multiply_by

# print(multiply_all([1, 2, 3])(10))

# multiply_all_1 = multiply_all([1, 2, 3])
# print(multiply_all_1(10))

# def initial_num(x):
#     def whole_equation(y):
#         # print(x, y)
#         return x ** y
#     return whole_equation

# print(initial_num(2)(10))


# def blah(n):
#     return n ** 2 if n > 5 else n

# print(blah(5))
# print(blah(10))
# print(blah(15))


# def reverse_number(n):
#     # to reverse an int, need to turn into a str
#     # account for negative numbers
#     num = str(n)
#     x= '0'
#     if num[0] == '-':
#         num = num[1:]
#         x = '-'
#     return int(x + num[::-1])

# print(reverse_number(123))
# print(reverse_number(-456))
# print(reverse_number(1000))


# class Fighter(object):
#     def __init__(self, name, health, damage_per_attack):
#         self.name = name
#         self.health = health
#         self.damage_per_attack = damage_per_attack
        
#     def __str__(self): return "Fighter({}, {}, {})".format(self.name, self.health, self.damage_per_attack)
#     __repr__=__str__

# def declare_winner(fighter1, fighter2, first_attacker):
#     # first\_attacker makes first strike, take his attack to reduce other fighter's health
#     turn = fighter1 if fighter1.name == first_attacker else fighter2
#     while fighter1.health >= 0 and fighter2.health >= 0:
#         if turn == fighter1:
#             fighter2.health -= fighter1.damage_per_attack
#             turn = fighter2
#         else:
#             fighter1.health -= fighter2.damage_per_attack
#             turn = fighter1
#     print(fighter1, fighter2)
#     return fighter1.name if fighter2.health <= 0 else fighter2.name


# print(declare_winner(Fighter("susan", 20, 10),Fighter("Thomas", 5, 4), "Thomas"))

# def print_kwargs(**kwargs):
#     # for key, value in kwargs.items():
#     #     print(f"{key}: {value}")
#     return kwargs

# print(type(print_kwargs(a=1, b='two', c=True)))



# def sum_args(*args):
#     return sum(args)
#     # return sum(n for n in args)

# print(sum_args(2, 4, 5))

# def has_unique_chars(string):
#     return len(string) == len(set(string))


# def area_largest_square(r):
#     # radius is the distance from circle's center to its edge in a straight line
#     return 2*r**2

# print(area_largest_square(7))


# def my_languages(d):
#     # need to get k, v to match them
#     # final = []
#     # for key in d:
#     #     if d[key] >= 60:
#     #         final.append(key)
#     # return final
#     final = sorted(d, key=(lambda k: d[k]), reverse=True)
#     return list(filter(lambda lang: lang if d[lang] >= 60 else None, final))

# print(my_languages({"Java": 10, "Ruby": 80, "Python": 65}))

# def explode(s):
#     # new_string = ''
#     # for c in s:
#     #     new_string += int(c) * c
#     # return new_string
#     return ''.join(int(c) * c for c in s)

# print(explode('312'))

# def some_kwargs(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}:', v)

# kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
# some_kwargs(**kwargs)


# def multiply(*args, **kwargs):
#     z = 1
#     for num in args:
#         z *= num
#     print(z, type(kwargs))
#     # return (type(args))

# print(multiply(4, 5))
# print(multiply(10, 9))
# print(multiply(2, 3, 4))
# print(multiply(3, 5, 10, 6, john='smith'))


# def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
#     # your code here
#     final = []
#     for n in range(a, b+1):
#         # for each number, if number  more than 1 digit, separate digits, raise each consecutive digit to power of 1, 2, 3, 4, etc. return sum == number
#         # now separate number
#         total = 0
#         for i in range(len(str(n))):
#             # this takes '89' and loops through each digit
#             total += int(str(n)[i]) ** (i + 1) # this takes each digit to power of index starting at 1 and adds to total sum for that number
#             # check if total = number
#         if total == n:
#             final.append(n)
#     return final
        
# print(sum_dig_pow(1,10))
# print(sum_dig_pow(1,100))
# print(sum_dig_pow(10,89))
# print(sum_dig_pow(10,100))
# print(sum_dig_pow(90,100))

# def sum_consecutives(s):
#     #good luck
#     # for loop. only sum curr num if next num is the same, if different num, add either the num or sum to the list
#     # only append to new list when numbers different, if not, keep adding
#     sum_nums = 0
#     final = []
#     for i in range(len(s)-1):
#         # if number is diff than next and no sum nums, add num
#         if s[i] != s[i+1] and not sum_nums:
#             final.append(s[i])
#         # else if num diff than next but yes sum nums, add num + sumnums
#         elif s[i] != s[i+1]:
#             final.append(sum_nums + s[i])
#         # else if num same than next, sumnums += num
#         else:
#             sum_nums += s[i]
#     return final
        
# print(sum_consecutives([1,4,4,4,0,4,3,3,1]))
# print(sum_consecutives([1,4,4,4,0,4,3,3,1,1]))

# # matrixAddition(
# #   [ [1, 2, 3],
# #     [3, 2, 1],
# #     [1, 1, 1] ],
# # //      +
# #   [ [2, 2, 1],
# #     [3, 2, 3],
# #     [1, 1, 3] ] )

# # // returns:
# #   [ [3, 4, 4],
# #     [6, 4, 4],
# #     [2, 2, 4] ]

# def matrix_addition(a, b):
#     # your code here
#     final = []
#     for i, array in enumerate(a):
#         chunks = []
#         for j, num in enumerate(array):
#             chunks.append(a[i][j] + b[i][j])
#         final.append(chunks)
#     return final

# print(matrix_addition(
#     [ [1, 2, 3],
#     [3, 2, 1],
#     [1, 1, 1] ], 
#     [ [2, 2, 1],
#     [3, 2, 3],
#     [1, 1, 3] ]))

# Pair of gloves
# Winter is coming, you must prepare your ski holidays. The objective of this kata is to determine the number of pair of gloves you can constitute from the gloves you have in your drawer.

# Given an array describing the color of each glove, return the number of pairs you can constitute, assuming that only gloves of the same color can form pairs.

# Examples:
# input = ["red", "green", "red", "blue", "blue"]
# result = 2 (1 red pair + 1 blue pair)

# input = ["red", "red", "red", "red", "red", "red"]
# result = 3 (3 red pairs)

# def number_of_pairs(gloves):
#     glove_pairs = {}
#     for glove in gloves:
#         glove_pairs[glove] = glove_pairs.get(glove, 0) + 1
#     pairs = 0
#     for value in glove_pairs.values():
#         pairs += value // 2
#     return pairs

# print(number_of_pairs(["red", "green", "red", "blue", "blue"]))
# print(number_of_pairs(["red", "red", "red", "red", "red", "red"]))

# def calc(expr):
#     # need for loop through string..if can be int or float, convert, if operand, need to change its place to 1 index position to its left, if consecutive numbers wo operands, use next operand for all of them
#     # should i change the string first to have operands in right place?
#     # can create a list with the numbers if i and i+1 are both numbers to store them, always check i and i+1..if i and i+1 are numbers, store in list? if not, the perform operation
#     return eval(expr)

# print(calc("5 - 1 + 2 + 4 * + 3"))

# def clean_string(s):
#     # a backspace can be one or more and deletes characters that come before it
#     # basically pop() should delete the last from string
#     backspaced = []
#     for c in s:
#         if c == '#':
#             if not backspaced:
#                 continue
#             else:
#                 backspaced.pop()
#         else:
#             backspaced.append(c)
#     return ''.join(backspaced)

# print(clean_string('abc#d##c'))
# print(clean_string('abc##d######'))


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
# #         could loop through each elem 
# #         easy solution:
#         for num in nums:
#             if nums.count(num) > 1:
#                 return True
#         return False


# def solve(string):
#     # check if char is consonant, then get its value and store it in dict
#     cons = set('bcdfghjklmnpqrstvwxyz')
#     values = {}
#     for c in string:
#         if c in cons:
#             values[c] = ord(c) - 96 # 'a' gives 1
#     # now i have dict of all leters in string with their values..need to now store/compare consecutive consonants in string
#     # can do a running sum of values IF still consonants, 
#     is_c_cons = False
#     tally = 0
#     for i, c in enumerate(string):
#         if c in cons:
#             is_c_cons = True
#         else:
#             is_c_cons = False
#         if is_c_cons:
#             tally += values[c]

# print(solve('strength'))


# def highest_rank(arr):
#     # return the number w the highest count within the array
#     # if tie, return the largest number
#     count = 0
#     maximum = None
#     for num in set(arr):
#         this_num_count = arr.count(num)
#         if this_num_count > count:
#             count = this_num_count
#             maximum = num
#         elif this_num_count == count:
#             if num > maximum:
#                 maximum = num
#     return maximum

# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]))
# print(highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))
# print(highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]))


# def pyramid(n):
# # input is integer
# # output is array of arrays
# # cannot be less than 0, if 0 then empty array
# # each array should contain 1 as int inside each index position
# # create initial empty list
# # while loop until 0 reached? insert each new arr at index 0
# # in while loop, create single arr with n length of 1 values
# # after each loop, reduce n by 1
#     final = []
#     while n > 0:
#         # arr = list('1'*n) # need to create [1, 1, 1]
#         arr = [1 for _ in range(n)]
#         final.insert(0, arr)
#         n -= 1
#     # print(10*['i'])
#     return final

# print(pyramid(5))


# # Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

# # For example:

# # c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# # c.encode('Codewars') # returns 'HTIJBFWX'
# # c.decode('BFKKQJX') # returns 'WAFFLES'
# # If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
# # The shift will always be in range of [1, 26].

# class CaesarCipher(object):
#     # need to lowercase the string, then for each alpha character move forward if encode or backward if decode
#     # range in shift will be within 1, 26
#     # need formula to do if c after shift is < 1 or > 26, then subtract accordingly or something
#     def __init__(self, shift):
#         self.shift = shift

#     def encode(self, string):
#         # returns + shift
#         # will change the string in-place not out of place
#         st = list(string.lower())
#         for i, c in enumerate(st):
#             if c.isalpha():
#                 # change c by + shift, if out of range, do result - 26 or something
#                 new = ord(c) + self.shift # NEED TO GET THE INT OF C HERE
#                 # if letter goes over 'z', subtract 26 from ord value
#                 if new > 122:
#                     st[i] = chr(new - 26)
#                 else:
#                     st[i] = chr(new)
#         return ''.join(st).upper()

#         # 97  a
#         # 122 z
        
#     def decode(self, string):
#         # returns - shift
#         st = list(string.lower())
#         for i, c in enumerate(st):
#             if c.isalpha():
#                 # change c by + shift, if out of range, do result - 26 or something
#                 new = ord(c) - self.shift # NEED TO GET THE INT OF C HERE
#                 # if letter goes over 'z', subtract 26 from ord value
#                 if new < 97:
#                     st[i] = chr(new + 26)
#                 else:
#                     st[i] = chr(new)
#         return ''.join(st).upper()

# c = CaesarCipher(5)
# print(c.encode('Code.wars'))
# print(c.decode('BFKKQJX'))


# Your Task
# You will be given a wishlist (array), containing all possible items. Each item is in the format: {name: "toy car", size: "medium", clatters: "a bit", weight: "medium"} (Ruby version has an analog hash structure, see example below)

# You also get a list of presents (array), you see under the christmas tree, which have the following format each: {size: "small", clatters: "no", weight: "light"}

# Your task is to return the names of all wishlisted presents that you might have gotten.

# Rules
# Possible values for size: "small", "medium", "large"
# Possible values for clatters: "no", "a bit", "yes"
# Possible values for weight: "light", "medium", "heavy"
# Don't add any item more than once to the result
# The order of names in the output doesn't matter
# It's possible, that multiple items from your wish list have the same attribute values. If they match the attributes of one of the presents, add all of them.
# Example
# wishlist = [{'name': "mini puzzle", 'size': "small", 'clatters': "yes", 'weight': "light"},
#             {'name': "toy car", 'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#             {'name': "card game", 'size': "small", 'clatters': "no", 'weight': "light"}]
# presents = [{'size': "medium", 'clatters': "a bit", 'weight': "medium"},
#             {'size': "small", 'clatters': "yes", 'weight': "light"}]
# # guess_gifts(wishlist, presents) # => must return ["Toy Car", "Mini Puzzle"]

# def guess_gifts(wishlist, presents): 
#     # input: 2 lists, each with multiple dictionaries with string attr
#     # output: list with string attr
#     # check for every present, if all of its 3 attributes match w 1 or multiple items in wishlist
#     possible = []
#     for i, present in enumerate(presents):
#         # print(i, present['weight'])
#         for j, wishlist_p in enumerate(wishlist):
#             if present['weight'] == wishlist_p['weight'] and present['size'] == wishlist_p['size'] and present['clatters'] == wishlist_p['clatters']:
#                 possible.append(wishlist_p['name'])
#     return list(set(possible))

# print(guess_gifts(wishlist, presents))


# def zero(): #your code here
# def one(): #your code here
# def two(): #your code here
# def three(): #your code here
# def four(): #your code here
# def five(): #your code here
# def six(): #your code here
# def seven(): #your code here
# def eight(): #your code here
# def nine(): #your code here

# def plus(): #your code here
# def minus(): #your code here
# def times(): #your code here
# def divided_by(): #your code here


# print(seven(times(five()))) # must return 35
# print(four(plus(nine()))) # must return 13
# print(eight(minus(three()))) # must return 5
# print(six(divided_by(two()))) # must return 3


# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

# You can find some examples in the test fixtures.

# def make_readable(seconds):
#     # input -> int
#     # output -> str w hh:mm:ss as numbers
#     # need to figure out how each s, m, h will display its number accordingly...
#     # can take a number and retain its remainder converted to s, then m, then h...
#     # need to first check its remainder as divided by 60, then its remainder by 3600? that would give you the resting minutes in seconds, so would need to convert those seconds to minute notation probably? same with hours?
#     # if divide 21 / 10, you get 1 as remainder, 25 / 10 you get 5. its all in its base notation

#     # logically, I would split the number into chunks
#     # last chunk div by 60
#     secs = '0' + str(seconds % 60) if seconds % 60 < 10 else str(seconds % 60) # gets seconds
#     mins = '0' + str((seconds % (60*60)) // 60 ) if ((seconds % (60*60)) // 60 ) < 10 else str((seconds % (60*60)) // 60 ) # need minutes
#     hrs = '0' + str((seconds // (60*60))) if ((seconds // (60*60))) < 10 else str((seconds // (60*60))) # gets hours
#     return f'{hrs}:{mins}:{secs}'

# print(make_readable(0))
# print(make_readable(5))
# print(make_readable(60))
# print(make_readable(86399))
# print(make_readable(359999))

# def narcissistic(value):
#     exp = len(str(value))
#     numbers = [int(d)**exp for d in (str(value))]
#     return sum(numbers) == value

# print(narcissistic(153))



# def order(sentence):
#     # code here
# #   need to split the str, then check if there is an integer in string, and place that word or insert in its right position in new array
#     def int_order(word):
#         # list_sentence = sentence.split()
#         # for word in (list_sentence):
#         for c in word:
#             if c.isnumeric():
#                 # need to modify original list...so pop word at its index, and insert that popped word at new index...
#                 return int(c)

#     return ' '.join(sorted(sentence.split(), key=int_order))

# print(order('4of Fo1r pe6ople g3ood th5e the2'))


# def sort_by_length(arr):
#     # need to sort array from small to largest in length...
#     return sorted(arr, key=len)

# print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))

# def remove_url_anchor(url):

#     # TODO: complete
#     # need to look at url, see 1st instance of '#' symbol, and only return whatever is before that symbol
#     return url.partition('#')

# print(remove_url_anchor("www.codewars.com#about#me"))
# print(remove_url_anchor("www.codewars.com?page=1"))


# write the function is_anagram
# def is_anagram(test, original):
#     # so if we can compare letters by re-arraning w a fn, should solve problem, taking sentence case into acct
#     return sorted(test.lower()) == sorted(original.lower())

# print(is_anagram("foefeT", "toffee"))


# def sequence_sum(begin_number, end_number, step):
#     # input three numbers as integers
#     # output one integer
#     total = 0
#     for num in range(begin_number, end_number+1, step):
#         total += num
#     return total

# print(sequence_sum(1,5,1))

# def order_weight(string):
#     # input: string of numbers separated by spaces
#     # output: string of numbers separated by spaces
#     # need to separate strings by whitespace, change each string to integer for comparison, sort smallest to largest integer, if same integer sort by their string form, when finished sorting, return string of joined integers
#     str_list = string.split(' ')
#     sums_list = []
#     for weight in str_list:
#         dsum = 0
#         for d in weight:
#             dsum += int(d)
#         sums_list.append(dsum)
#     return (sums_list)
    # return sorted(int_list)

# def order_weight(_str):
#     return ' '.join(sorted((_str.split(' ')), key=lambda x: sum([int(c) for c in x])))
#     # return (int(c) for c in _str.split())
#     # return sum([1,2,3,4,5])
#     # return sum(1,2,3,4,5)

# print(order_weight("56 65 74 100 99 68 86 180 90")) # "100 180 90 56 65 74 68 86 99"


# A single die can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

# Example scoring
#  Throw       Score
#  ---------   ------------------
#  5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
#  1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
#  2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

# def score(dice):
#     # input: array of 5 numbers from 1-6 random
#     # output: integer of total points
#     # if a number is contained exactly 3 times in array, sum those special points
#     # elif for every 1 or 5 in array, sum 100 or 50 points
#     # esta mucho mas complicado de lo que pensaba...
#     # me la estoy complicando siento
#     points = 0
#     dnums = {}
#     for num in set(dice):
#         dnums[num] = dice.count(num)
#         if dnums[num] >= 3:
#             if num == 1:
#                 points += num * 1000
#                 dnums[num] -= 3
#                 points += dnums[num] * 100
#             elif num == 5:
#                 points += num * 100
#                 dnums[num] -= 3
#                 points += dnums[num] * 100
#             else:
#                 points += num * 100
#         else:
#             if num == 1:
#                 points += dnums[num] * 100
#             elif num == 5:
#                 points += dnums[num] * 50
#     return points

# print(score([5,1,3,4,1]))
# print(score([1,1,1,1,1]))
# print(score([1,1,1,1,3]))
# print(score([2,4,4,5,4]))


# def calc():
#     # there is a pattern here: 2^n always follows 2, 4, 8, 6, 2, 4, 8, 6, etc
#     for num in range(12, 16):
#         for exp in range(1, 16):
#             print(num, 'to the', exp, f"Result is {num**exp}")
#     return pow(3, 3, 7) % 7

# print(calc())


# def strings(word1, word2):
#     return ''.join(word1) == ''.join(word2)


# print(strings(['ab', 'c'], ['a', 'bc']))


# def steps(num):
#     steps = 0
#     while num > 0:
#         if num % 2 == 0:
#             num /= 2
#         else:
#             num -= 1
#         steps += 1
#     return steps

# print(steps(4))


# def richest(xlist):
#     for i, customer in enumerate(xlist):
#         xlist[i] = sum(customer)
#     return max(xlist)

# print(richest([[7,1,3],[2,8,7],[1,9,5]]))


# def running_sum(nums):
#     # nums is a list
#     count = 0
#     running_list = []
#     for num in nums:
#         count += num
#         running_list.append(count)
#     return running_list

# print(running_sum([3,1,2,10,1]))


# # You need to write regex that will validate a password to make sure it meets the following criteria:

# # At least six characters long
# # contains a lowercase letter
# # contains an uppercase letter
# # contains a digit
# # only contains alphanumeric characters (note that '_' is not alphanumeric)

# import re
# # pattern = re.compile(r'')
# # creo que ya tengo todo lo que necesito para cumplir..

# test = re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?!.*_)(?!.*\W).{6,}', '2Aabcdf')
# print(test)
# # test2 = re.search(r'\w{9}', '2Aabcdf__\t')
# # print(test2)


# def done_or_not(board):
#     for i in range(0, 9):
#       (l, c, b) = (set(), set(), set())
#       for j in range(0, 9):
#           c.add(board[i][j]) 
#           l.add(board[j][i])
#           b.add(board[0 + j // 3][((i * 3) % 9) + j % 3])
#       if len(l)!=9 or len(c)!=9 or len(b)!=9:
#           return 'Try again!'
#     return "Finished!"


# print(done_or_not([  [1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

# def done_or_not(board): #board[i][j]
#     # okay. rows are easy just create a set for each row to check for duplicates..
#     # n is a number
#     # if n at position 1, n cannot be in that row, nor that column, nor in the range of variable 3x3 grid
#     # we could create a set for each row, each column, and each 3x3. that would check if all are unique values...
#     # row set...for each list, check if set(list) has length of 9 to continue
#     for i, row in enumerate(board):
#         if len(set(row)) != 9:
#             return 'Try again!'
#     # col set...for each row at row[index], check if num not in set to add to set and continue
#     for i in range(len(board)):
#         cols = set()
#         for j in range(len(board)):
#             if board[j][i] in cols:
#                 return 'Try again!'
#             cols.add(board[j][i])
#             # print(cols)
#     # 3x3 set...for each row, if row[index] in range 0:3,3:6,6:9, check row numbers in that range, and two above/below rows as well at same range, check if num not in 3x3 set to add to set and continue
#     grid = set()
#     for i in range(len(board)):
#         for j in range(len(board)):
#             if i in range(0,3):
#                 if j in range(0,3):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(3,6):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(6,9):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#             grid = set()
#             if i in range(3,6):
#                 if j in range(0,3):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(3,6):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(6,9):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#             grid = set()
#             if i in range(6,9):
#                 if j in range(0,3):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(3,6):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])
#                 elif j in range(6,9):
#                     if board[i][j] in grid:
#                         return 'Try again!'
#                     grid.add(board[i][j])

#     return 'Finished!'

# print(done_or_not([  [1, 3, 2, 5, 7, 9, 4, 6, 8]
#                         ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
#                         ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
#                         ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
#                         ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
#                         ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
#                         ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
#                         ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
#                         ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]))

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