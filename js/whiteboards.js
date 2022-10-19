// function reverseWords(str) {
//     // Go for it
//     return str[0]
//   }

// console.log(reverseWords('The quick brown fox jumps over the lazy dog.'));

// function number(busStops){
//     // need to extract arr within arr to access the numbers...
//     // for each pair, subtract right side from left, add to global count variable
//     let count = 0
//     busStops.map(([hopOn, hopOff]) => count += hopOn - hopOff)
//     return count
// }

// console.log(number([[10,0],[3,5],[5,8]])); // 5

// In a factory a printer prints labels for boxes. For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

// The colors used by the printer are recorded in a control string. For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

// Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

// You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

// The string has a length greater or equal to one and contains only letters from a to z.

// Examples:
// s="aaabbbbhaijjjm"
// printer_error(s) => "0/14"

// s="aaaxbbbbyyhwawiwjjjwwm"
// printer_error(s) => "8/22"

// function printerError(s){
//     // takes in a string, outputs a fraction as a string "numerator/denominator"
//     // let errors = 0
//     // for (let c of s){
//     //     if ('nopqrstuvwxyz'.includes(c)){
//     //         errors += 1
//     //     }
//     // }
//     let errors = s.split('').filter(c => c > 'm')
//     return `${errors.length}/${s.length}`
//     // return slist
// }

// console.log(printerError('aaabbbcccno'))


// function openOrSenior(data){
//     //   logic: look at each pair, see if age > 54 and handicap > 7
//     //   let playerType = []
//     //   for (let player of data){
//     //     player[0] >= 55 && player[1] > 7 ? playerType.push("Senior") : playerType.push("Open")
//     //   }
//     //   return playerType
//     // }

//     // option 2:
//     return data.map(([age, handicap]) => (age >= 55 && handicap > 7) ? "Senior" : "Open")
// }

// console.log(openOrSenior([[45, 12],[55,21],[19, -2],[104, 20]]),['Open', 'Senior', 'Open', 'Senior'])


// function findNextSquare(sq) {
//     // Return the next square if sq is a perfect square, -1 otherwise
//     sqrt = Math.sqrt(sq)
//     return sqrt % 2 === 1 || sqrt % 2 === 0 ? (sqrt + 1) ** 2 : -1
//   }

// console.log(findNextSquare(121))
// console.log(findNextSquare(64))
// console.log(findNextSquare(121))


// function validatePIN (pin) {
//     return Number(pin) && (pin.length == 4 || pin.length == 6) ? true : false
//   }

// console.log(validatePIN('1234a'))
// console.log(validatePIN('0000'))
// console.log(validatePIN('12345'))
// console.log(validatePIN('123456'))
// console.log(validatePIN('12345a'))


// function addBinary(a,b){
//     return (a+b).toString(2)
//   }

// console.log(addBinary(9, 5))


// String.prototype.toJadenCase = function () {
//   //   split the string by spaces
//   //   once split, for loop for every word, capitalize word[0]
//   //   
//     splitStr = str.split(" ");
//     newStr = []
//     for (word of splitStr){
//         newStr.push(word[0].toUpperCase() + word.slice(1))
//     }
//     return newStr.join(" ")
//   };

// var str = "How can mirrors be real if our eyes aren't real";
// console.log(str.toJadenCase())
// str.toJadenCase(), "How Can Mirrors Be Real If Our Eyes Aren't Real";

// function isIsogram(str){
//     // for (i in str){
//     //     for (j in str){
//     //         if (j != i){
//     //             if (str[j].toLowerCase() === str[i].toLowerCase()){
//     //                 return false
//     //             }
//     //         }
//     //     }
//     // }
//     // return true
//     return new Set(str.toLowerCase()).size === str.length
//   }

// console.log(isIsogram('MoOse'))
// console.log(isIsogram('abrujmklP'))

// let x = new Set('ababababa')
// console.log(x)


// function filter_list(l) {
//     // Return a new array with the strings filtered out
//     return l.filter((item) => typeof (item) !== 'string')
//   }

// console.log(filter_list([1,2,'a','b']))



// Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

// Examples input/output:

// XO("ooxx") => true
// XO("xooxx") => false
// XO("ooxXm") => true
// XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
// XO("zzoo") => false

// checking for o or O if == to x or X total amount...
// if string is odd, then false
// then check for every character if is equal to any of 4 options

// function XO(s){
//     let counterX = 0
//     let counterO = 0
//     for (let c of s){
//         // if (c.toLowerCase() === 'x'){
//         //     counterX += 1
//         // } else if (c.toLowerCase() === 'o'){
//         //     counterO += 1
//         // }
//         c.toLowerCase() === 'x' ? counterX += 1 : c.toLowerCase() === 'o' ? counterO += 1 : null
//     }
//     return counterX === counterO
// }

// console.log(XO("ooxx"))
// console.log(XO("xooxx"))
// console.log(XO("ooxXm"))
// console.log(XO("zpzpzpp"))
// console.log(XO("zzoo"))


// function removeExclamationMarks(s) {
//     // let noEx = ''
//     // for (let c of s){
//     //     c !== '!' ? noEx += c : null
//     // }
//     // return noEx
//     // let sArr = s.split('')
//     return s.split('').filter((c) => c !== '!').join('')
//   }

// console.log(removeExclamationMarks('!!hell??!!o world!!'))

// const a = 10

// function f(){
//     console.log(a)
// }
// f()
// console.log(a)


    // let a = 10
 
    // // It is not allowed
    // let a = 8
 
    // // It is allowed
    // a = 10


    // function f() {
 
    //     // It can be accessible any
    //     // where within this function
    //     var a = 10;
    //     console.log(a)
    // }
    // f();
 
    // // A cannot be accessible
    // // outside of function
    // console.log(a);


// Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

// The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

// Mind the input validation.

// Example
// { 6, 2, 1, 8, 10 } => 16
// { 1, 1, 11, 2, 3 } => 6
// Input validation
// If an empty value ( null, None, Nothing etc. ) is given instead of an array, or the given array is an empty list or a list with only 1 element, return 0.


// function sumArray(array) {
//     // const compareNums = (a, b) => a - b
//     // console.log(Math.min(...array), Math.max(...array))
//     counter = 0
//     for (let num of array){
//         num !== Math.min(...array) && num !== Math.max(...array) ? counter += num : console.log(`${num} is not being added`)
//     }
//     return counter
//     // return array.sort(compareNums)
// }

// console.log(sumArray([6, 2, 1, 8, 10]))


// You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
// If it is a square, return its area. If it is a rectangle, return its perimeter.

// Example(Input1, Input2 --> Output):

// 6, 10 --> 32
// 3, 3 --> 9
// Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.

// const areaOrPerimeter = (l , w) => l === w ? l * w : (l*2) + (w*2)

// console.log(areaOrPerimeter(3, 3))

// Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

// For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

// const quarterOf = (month) => {
//     if (month % 3 === 0){
//         return month / 3
//     } else {
//         return Math.floor(month / 3) + 1
//     }
// }

// console.log(quarterOf(10))

// Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

// Return your answer as a number.

// function sumMix(x){
//   return x.reduce((prev, curr) => Number(prev) + Number(curr))
// } 

// console.log(sumMix([9, 3, '7', '3']))

// function sumMix2(x){
//   return x.map((num, i) => parseInt(num) + i)
// } 

// console.log(sumMix2([9, -3, '-7', '-3']))


// I'm new to coding and now I want to get the sum of two arrays... Actually the sum of all their elements. I'll appreciate for your help.

// P.S. Each array includes only integer numbers. Output is a number too.

// function arrayPlusArray(arr1, arr2, arr3) {
//     return arr1.concat(arr2, arr3).reduce((prev, curr) => prev + curr) // this automatically takes the first prev value as 0 if nothing input
// }
// console.log(arrayPlusArray([1,2,3], [4,5,6], [3,4,7]))
// console.log(([1,2,3] + [4,5,6]))


// Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

// For example: ["3:1", "2:2", "0:1", ...]

// Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

// if x > y: 3 points
// if x < y: 0 point
// if x = y: 1 point

// function points(games) {
//     let counter = 0;
//     for (let result of games){
//         let score = result.split(':');
//         // console.log(score)
//         (score[0] > score[1]) ? counter += 3 : (score[0] === score[1]) ? counter += 1 : 'nini';
//     }
//     return 'counter'
// }

// points(["3:1", "2:2", "0:1"])

// Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

// It should remove all values from list a, which are present in list b keeping their order.

// array_diff([1,2],[1]) == [2]
// If a value is present in b, all of its occurrences must be removed from the other:

// array_diff([1,2,2,2,3],[2]) == [1,3]








// Given a binary array called nums, return the maximum number of consecutive 1's in the array.
// Input: nums = [1,1,0,1,1,1]
// Output: 3
// Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

// Example 2:
// Input: nums = [1,0,1,1,0,1]
// Output: 2

// function maxOnes(arr){
    
// }




// // Sum Numbers

// function sum (numbers) {
//     let total = 0;
//     for (num of numbers){
//       total += num
//     }
//     return total
//   }

// console.log(sum([4,3]))


// // Make a program that filters a list of strings and returns a list with only your friends name in it.

// // If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
// // Otherwise, you can be sure he's not...

// // Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

// // i.e.

// // friend = ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]


// let input = ["Ryan", "Kieran", "Jason", "Yous"]

// function friend(names){
//     return names.filter(element => element.length === 4);
// };

// console.log(friend(input));



// // 2
// // need to check each iterable of string, check if it is capital letter, 
// // push capital letters to new array
// function ord_str(word){
//     let capitals = []
//     for (let index in word){
//         if (word[index] == word[index].toUpperCase()){
//             capitals.push(Number(index))
//         }
//     }
//     return capitals
// };

// console.log(ord_str('CodEWaRs'));

