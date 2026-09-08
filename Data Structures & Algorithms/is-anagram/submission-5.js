class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(a, t) {
        if(a.length!= t.length) return false
        let s = new Map()

        for(var char of a){
            let count = s.get(char) || 0
            s.set(char, count+1)
        }

        for(var char of t){
            if(!s.has(char)){
                return false
            }
            let count = s.get(char)
            if(count == 0 ){
                return false
            }
            s.set(char, count-1)
        }
        return true
    }

}
