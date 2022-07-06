const two_str1 = "object oriented programming";
const two_expected1 = "OOP";

// The 4 pillars of OOP
const two_str2 = "abstraction polymorphism inheritance encapsulation";
const two_expected2 = "APIE";

const two_str3 = "software development life cycle";
const two_expected3 = "SDLC";

// Bonus: ignore extra spaces
const two_str4 = "  global   information tracker    ";
const two_expected4 = "GIT";

/**
 * Turns the given str into an acronym.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string to be turned into an acronym.
 * @returns {string} The acronym.
 */
function acronymize(str) {
  

    
}

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 * 
 * pseudo code
 * - create a function that takes in a string
 * - create a newString variable
 * - loop through the given string
 *      - add each letter to a newString variable
 * - return newString
 */
function reverseString(str) {

    for(let i = 0, j = str.length - 1; i < j; i++, j--){
        let temp = str[i]
        str[i] = str[j]
        console.log(str[i]);
        str[j] = temp
        console.log(str[j]);
    }
    console.log(str);
    return str
}

console.log(reverseString(str3));
