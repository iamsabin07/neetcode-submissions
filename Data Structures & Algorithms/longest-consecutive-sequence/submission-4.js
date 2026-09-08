class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if(nums.length <2) return nums.length;
        let set = new Set(nums);
        let highest = 1;
        for(let num of set){
            let count = 0;
            let i = num;
            while(i<= nums.length){
                if(set.has(i)){
                    count++;
                    i++;
                }
                else{
                    break;
                }
            }
            highest = Math.max(count, highest);
        }
        return highest;
    }
}
