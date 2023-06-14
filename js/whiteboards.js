


// function countDevelopers(list) {
//     let counter = 0
//     list.forEach(dev => dev.language == 'JavaScript' && dev.continent == 'Europe' ? counter += 1 : 0)
//     // for (let dev of list){
//     //     dev.language == 'JavaScript' && dev.continent == 'Europe' ? counter += 1 : 0
//     // }
//     return counter 
//   }

// console.log(countDevelopers([
//     { firstName: 'Noah', lastName: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'JavaScript' },
//     { firstName: 'Maia', lastName: 'S.', country: 'Tahiti', continent: 'Oceania', age: 28, language: 'JavaScript' },
//     { firstName: 'Shufen', lastName: 'L.', country: 'Taiwan', continent: 'Asia', age: 35, language: 'HTML' },
//     { firstName: 'Sumayah', lastName: 'M.', country: 'Tajikistan', continent: 'Asia', age: 30, language: 'CSS' }
//   ]));


// function evenNumbers(array, number) {
//     return array.filter(a => a % 2 == 0).slice(-number)
//   }

// console.log(evenNumbers([-22, 5, 3, 11, 26, -6, -7, -8, -9, -8, 26], 2));


// function getCount(str) {
//     let counter = 0
//     const vowels = 'aeiou'
//     for (c of str){
//         vowels.includes(c) ? counter += 1 : null 
//     }
//     return counter 
//   }

// console.log(getCount("abracadabra"))

// function disemvowel(str) {
//     // // advanced
//     // const vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
//     // return str
//     //   .split('')
//     //   .filter(char => !vowels.includes(char))
//     //   .join('')
    
//     // basic
//     let vowels = 'aeiouAEIOU'
//     let final = ''
//     for (c of str){
//         !vowels.includes(c) ? final += c : null 
//     }
//     return final 
//   }

// console.log(disemvowel("This website is for losers LOL!"))


// function largest(n, array) {
//     // Find the n highest elements in a list
//     return array.sort((a,b)=>b-a).slice(0, n).sort((a,b)=>a-b)
//   }

// console.log(largest(2, [5,6,7,4,3,2,100]));


// function solve(arr) {
//     let unique = []
//     for (i=arr.length-1; i>=0; i--){
//         unique.includes(arr[i]) ? null : unique.push(arr[i])
//     }
//     return unique.reverse()
//   }

  
//   console.log(solve([3,4,4,3,6,3]));


// function toNumberArray(stringarray){
//   return stringarray.map(a => Number(a))
// }

// console.log(toNumberArray(["1","2.2","3.3"]));

// let multiline = `
//   This is a\
//   multiline
//   string.
// `;
// console.log(multiline);


// function findLongest(array){
//     // need to count num of digits in each number in array
//     let largest = array[0]
//     for (let n of array){
//         n.toString().length > largest.toString().length ? largest = n : null
//         // console.log(n.toString().length)
//         // console.log(n)
//     }
//     return largest 
//   }

// console.log(findLongest([8, 900, 500]));


// function solution(digits){
// //   for loop that takes in current iter digit and 4 following digits, update a var if number > var
//     let max = 0
//     for (i=0; i <= digits.length-4; i++){
//         let num = parseInt(digits.substring(i, i+5))
//         if (num > max){
//             max = num 
//         }
//     }
//     return max 
// }

// console.log(solution('731674765'));

// function solution(number) {
//     let greatestSequence = 0;
    
//     for (let i = 0; i < number.length - 4; i++) {
//       const sequence = parseInt(number.substring(i, i + 5));
//       if (sequence > greatestSequence) {
//         greatestSequence = sequence;
//       }
//     }
    
//     return greatestSequence;
//   }
  



// function alphabetWar(fight){
//     let left = {'w': 4, 'p': 3, 'b': 2, 's': 1}
//     let right = {'m': 4, 'q': 3, 'd': 2, 'z': 1}
//     let lt = 0
//     let rt = 0
//     for (let c of fight){
//         c in left ? lt += left.c : c in right ? rt += right.c : null 
//         console.log(rt, lt )
//     } 
//     return lt, rt 
//     // return lt > rt ? 'Left side wins!' : rt > lt ? 'Right side wins!' : `Let's fight again`
//     // return "Let's fight again!";
// }

// console.log(alphabetWar('zdqmwpbs'));


// function sumTriangularNumbers(n) {
//     // need to sum ...
//     let count = 0
//     let final = 0
//     for (let i=1; i<n+1; i++){
//         count += i
//         final += count 
//     }
//     return final 
//   }

// console.log(sumTriangularNumbers(6));


// const bump = x => x.split("").filter(char => char === 'n').length > 15 ? 'Car Dead' : 'Woohoo!'

// console.log(bump("_nnnnnnn_n__n______nn__nn_nn"));


// // return the two oldest/oldest ages within the array of ages passed in.
// function twoOldestAges(ages){
//   return ages.sort((a,b) => a-b).slice(-2)
// }

// console.log(twoOldestAges([1, 5, 87, 45, 8, 8]));

// function vowelIndices(word) {
//     const vowels = ['a', 'e', 'i', 'o', 'u'];
//     const indices = [];
//     for (let i = 0; i < word.length; i++) {
//       if (vowels.includes(word[i])) {
//         indices.push(i + 1);
//       }
//     }
//     return indices;
//   }
  

// console.log(vowelIndices('apple'));

// function divCon(x){
//     let plus = 0
//     let minus = 0
//     for (num of x){
//         console.log(typeof num);
//     }
//     return plus
// }

// console.log(divCon([9, 3, '7', '3']));


// function add(n) {
//   return function addAlso(m) {
//     return n+m;
//   }
//   // function also(m){
//   //   return n + m
//   // }
//   // return also 
// }

// console.log(add(5)(2));


// // function solve(s){
// //     // upper: 65-90
// //     // lower: 97-122
// //     // numbers: 30-39
// //     // special: all others
// //     let upper = 0
// //     let lower = 0
// //     let number = 0
// //     let special = 0
// //     for (let i in s){
// //         let x = s.charCodeAt(i)
// //         x>=65 && x<=90 ? upper += 1 : x>=97 && x<=122 ? lower += 1 : x>=49 && x<=58 ? number += 1 : special += 1
// //     }
// //     return [upper, lower, number, special]
// // }

// const solve = x => {
//     let u = x.match(/[A-Za-z0-9*]/g)||[]
//     let d = x.match(/[a-z]/g)||[]
//     let n = x.match(/[0-9]/g)||[]
//     let s = x.match(/[^A-Z0-9]/gi)||[]
//     return [u, d.length, n.length, s.length]
//   }

// console.log(solve("*'&ABCDabcde12345"));


// function digitize(n) {
//   return [...n.toString()].map(Number)
// }

// console.log(digitize(8675309));


// function sortGiftCode(code){
//   return code.split('').sort().join('')
// }

// console.log(sortGiftCode('zyxwvutsrqponmlkjihgfedcba'));

// function removeDuplicateWords(s){
//     // your perfect code...
//     // to remove words, need to separate by white spaces first into a list outside for loop
//     // in for loop, check if current word in 
//     return [...(new Set(s.split(" ")))].join(" ")
//   }

// console.log(removeDuplicateWords("alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"))


// function sumDigits(number){
//     return (Math.abs(number).toString().split('')).map(c => Number(c)).reduce((a, b) => a + b)
//     // return (Math.abs(number).toString().split('')).reduce((a, b) => +a + +b)
// }

// console.log(sumDigits(-99));

// function oddOrEven(array) {
//     let sum = 0
//     for (n of array){
//         sum += n 
//     }
//     return sum % 2 === 0 ? 'even' : 'odd'
//  }

//  console.log(oddOrEven([0, -1, 5]));

// Make a program that filters a list of strings and returns a list with only your friends name in it.

// If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
// Otherwise, you can be sure he's not...

// Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

// i.e.

// friend = ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]


// let input = ["Ryan", "Kieran", "Jason", "Yous"]

// function friend(names){
//     return names.filter(element => element.length === 4);
// };

// console.log(friend(input));



// // 2
// // need to check each iterable of string, check if it is capital letter, push capital letters to new array
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