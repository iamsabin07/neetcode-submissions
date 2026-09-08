class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s) {        
        const stack = [];
        const closeToOpen = {
            ')': '(',
            ']': '[',
            '}': '{',
        };

        for (let c of s) {
            if (closeToOpen[c]) {
                if(stack.length==0){
                    return false
                }
                if (
                    stack.length > 0 &&
                    stack.pop() !== closeToOpen[c]
                )  {
                    return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.length === 0;
    }
}
