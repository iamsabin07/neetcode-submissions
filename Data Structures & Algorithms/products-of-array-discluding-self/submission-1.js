class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {
        let sum = 1;
        let numberOfZero = 0
        for(const num of nums){
            if(num == 0){
                numberOfZero +=1
            }
            else{
                sum *=num
            }
        }
        if(numberOfZero >1){
            return Array.from({length: nums.length}, ()=> 0)
        }
        for(let i = 0; i< nums.length; i++){
            if(numberOfZero == 0){
                nums[i] = sum/nums[i]
            }
            else{
                if(nums[i]==0){
                    nums[i]= sum
                }
                else{
                    nums[i] = 0
                }
            }
        }
        return nums
    }
}
