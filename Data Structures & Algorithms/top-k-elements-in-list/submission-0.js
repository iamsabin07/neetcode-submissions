class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        const res = {}
        for(let i = 0; i<nums.length; i++){
            res[nums[i]] = (res[nums[i]] || 0) + 1;
        }

            const sortedEntries = Object.entries(res)
        .sort((a, b) => b[1] - a[1]); // Sort by value in descending order

    // Get the first two entries
    const firstK = sortedEntries.slice(0, k);
    
        return firstK.map(entry => parseInt(entry[0])); 
    }
}
