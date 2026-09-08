class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        let set = new Set(nums)
        let longest = 0
        for(var num of nums){
            if(!set.has(num-1)){
                let left =num
                let current = 1
                while(set.has(left+1)){
                    left++
                    current++
                }
                longest = Math.max(longest, current)
            }
        }
        return longest
    }
}
