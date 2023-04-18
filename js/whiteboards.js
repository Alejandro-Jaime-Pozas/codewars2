const bump = x => x.split("").filter(char => char === 'n').length > 15 ? 'Car Dead' : 'Woohoo!'

console.log(bump("_nnnnnnn_n__n______nn__nn_nn"));


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