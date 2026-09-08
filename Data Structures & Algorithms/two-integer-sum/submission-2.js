class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        let s = new  Map()

        for (let i=0; i<nums.length; i++){
            let compliment = target - nums[i]
            if(s.has(compliment)){
                return [s.get(compliment), i ]
            }
            s.set(nums[i], i)
        }
        return[]
    }

}
