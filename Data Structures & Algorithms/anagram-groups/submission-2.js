class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const result = new Map();
        const resArray = []
        for(const str of strs){
            const sorted = str.split('').sort().join('');
            const count = (result.get(sorted) || [])
            count.push(str)
            result.set(sorted, count)
        }
        for(const[key, value] of result){
            resArray.push(value)
        }
        return resArray
    }
}
