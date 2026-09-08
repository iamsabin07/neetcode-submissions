class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        if(strs.length === 1){
            return[strs]
        }
        let res = {};
        for(let str of strs){
            let str1 = str.split('').sort().join('');
            if(!res[str1]){
                res[str1]=[]
            }
            res[str1].push(str);
        }
        return Object.values(res);

    }
}
