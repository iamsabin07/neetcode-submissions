class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums) {
        if (nums.length === 0) return 0; // Handle empty array case

        let uniqueNums = [...new Set(nums)]; // Remove duplicates
        uniqueNums.sort((a, b) => a - b); // Sort numbers

        let left = 0;
        let right = 1;
        let highest = 1; // Default to 1 since a single number is a sequence

        while (right < uniqueNums.length) {
            if (uniqueNums[right] - uniqueNums[right - 1] !== 1) {
                highest = Math.max(highest, right - left);
                left = right;
            }
            right++;
        }

        return Math.max(highest, right - left);
    }
}
