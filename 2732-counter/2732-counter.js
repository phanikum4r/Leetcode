/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let c=-1
    return function() {
        c+=1
        return n+c
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */