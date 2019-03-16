class solution:
    def twoSum(self,nums,target):
        dic = {}
        for i,item in enumerate(nums):
            tmp = target - item
            for key,value in dic.items():
                if value == tmp:
                    return [key,i]
                dic[i] = item

            return None
