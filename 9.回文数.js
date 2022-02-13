/*
 * @lc app=leetcode.cn id=9 lang=javascript
 *
 * [9] 回文数
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var temp = 5;
var isPalindrome = function(x) {
    if(x < 0){
        return false;
    }
    let xTemp = x,remain,base,res = 0;
    while(xTemp != 0){
        base = xTemp % 10;
        remain = parseInt(xTemp/10);
        res = res*10 + base;
        xTemp = remain;
    }
    if(res == x){
        return true;
    }
    return false;
};
// @lc code=end
let arr = 121
res = isPalindrome(arr);
console.log(res);



