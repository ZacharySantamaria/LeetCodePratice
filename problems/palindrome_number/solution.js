/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if( x < 0 ) {return false;}
    for(let i = 0; i < x.toString().length / 2; i++) {
        if(x.toString()[i] != x.toString()[x.toString().length-1 - i]) {
            return false
        }
    }
    
    return true;
};