class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        dicta = {}

        for stra in strs:
            reqa = sorted(stra)
            req = "".join(reqa)
            if req in dicta:
                dicta[req].append(stra)
            else:
                dicta[req] = [stra]
        
        return list(dicta.values())
        