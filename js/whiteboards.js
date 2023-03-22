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