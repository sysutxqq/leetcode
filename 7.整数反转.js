/*
 * @lc app=leetcode.cn id=7 lang=javascript
 *
 * [7] 整数反转
 */

// @lc code=start
/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) { 
/*    var mark = 1;
    if(x < 0){
        mark = -1;
    }
*/
//    var xTmp = Math.abs(x);
    var xTmp = x, digital = 1,res = 0;
    while(xTmp != 0){
        digital = xTmp % 10;
        xTmp = parseInt(xTmp/10);
        if(res > parseInt(Math.pow(2,31)/10) || (res == parseInt(Math.pow(2,31)/10) && digital > Math.pow(2.31)%10)){
            return 0;
        };
        if(res < parseInt(Math.pow(-2,31)/10) || (res == parseInt(Math.pow(-2,31)/10) && digital < Math.pow(-2.31)%10)){
            return 0;
        };
        res = digital + res * 10;
    }
    //res = res * mark;
    return res;
};
// @lc code=end

