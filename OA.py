class OADP:
    def minFrogJump(nums):
        # [0,10,20,10,10]
        if nums is None or len(nums) == 0:
            return 0
        n = len(nums)
        table = [float('inf') for _ in range(n)]
        table[0] = 0
        table[1] = table[0] + abs(nums[0]-nums[1])

        for i in range(2, n):
            table[i] = min(table[i-1] + abs(nums[i-1] - nums[i]) , table[i-2] + abs(nums[i-2] - nums[i]))
        
        print('hi',table[-1])
        return table[-1]
    

    minFrogJump([10,30,40,20])
    minFrogJump([10,10])
    minFrogJump([30,10,60,10,60,50])