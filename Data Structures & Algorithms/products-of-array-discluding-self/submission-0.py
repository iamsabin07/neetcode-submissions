class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        product_without_zero = 1
        zeros = 0
        for num in nums:
            if(num != 0):
                product_without_zero = product_without_zero * num
            else:
                zeros = zeros + 1
            product = product * num
            
        answer = []
        for num in nums:
            if(num == 0 and zeros == 1):
                answer.append(product_without_zero)
            elif (num ==0. and zeros > 1):
                answer.append(0)
            else:
                self_product = int(product/num)
                answer.append(self_product)

        return answer
        