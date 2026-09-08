class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    maxArea(heights) {
        let left = 0
        let right = heights.length-1
        let maximum = 0

        while (left<right){
            let area = Math.min(heights[left], heights[right]) * (right-left)
            maximum = Math.max(area, maximum)
            if(heights[left]< heights[right]){
                left++
            }
            else{
                right--
            }
            
        }
        return maximum
    }
}
