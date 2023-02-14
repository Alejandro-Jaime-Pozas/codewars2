
// Make a program that filters a list of strings and returns a list with only your friends name in it.

// If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! 
// Otherwise, you can be sure he's not...

// Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

// i.e.

// friend = ["Ryan", "Kieran", "Mark"] `shouldBe` ["Ryan", "Mark"]


let input = ["Ryan", "Kieran", "Jason", "Yous"]

function friend(names){
    return names.filter(element => element.length === 4);
};

console.log(friend(input));



// 2
// need to check each iterable of string, check if it is capital letter, push capital letters to new array
function ord_str(word){
    let capitals = []
    for (let index in word){
        if (word[index] == word[index].toUpperCase()){
            capitals.push(Number(index))
        }
    }
    return capitals
};

console.log(ord_str('CodEWaRs'));