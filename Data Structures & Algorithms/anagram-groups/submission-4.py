class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        map = {}
        result = []
        for str in strs:
            sortedStr = "".join(sorted(str))
            temp = map.get(sortedStr,[])
            temp.append(str)
            map[sortedStr] = temp
        
        for i in map.values():
            result.append(i)

        return result
        