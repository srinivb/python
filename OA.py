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
        
        #print('hi',table[-1])
        return table[-1]
    

    minFrogJump([10,30,40,20])
    minFrogJump([10,10])
    minFrogJump([30,10,60,10,60,50])

    def minCostNjumps(h, k):
        if h is None or len(h) == 0:
            return 0
        m = len(h)
        table = [float('inf') for _ in range(m)]
        table[0] = 0
        for i in range(1, m):
            for j in range(1, k+1):
                if i - j >= 0:
                    table[i] = min(table[i], table[i-j] + abs(h[i-j] - h[i]))
       # print('hi ',table[-1])
        return table[-1]

    minCostNjumps([10,30,40,50,20], 3)
    minCostNjumps([10,20,10], 1)
    minCostNjumps([10,10], 100)
    minCostNjumps([40,10,20,70,80,10,20,70,80,60], 4)

    def CVacation(N, a, b, c):
        swim, bug, hw = [float('-inf')] * len(a), [float('-inf')]*len(b) , [float('-inf')] * len(c)
        swim[0] = a[0]
        bug[0] = b[0]
        hw[0] = c[0]
        
        for i in range(1, N):
            swim[i] = max(bug[i-1], hw[i-1]) + a[i]
            bug[i] = max(swim[i-1], hw[i-1]) + b[i]
            hw[i] = max(swim[i-1], bug[i-1]) + c[i]
        
        print('hi ',max(swim[-1], bug[-1], hw[-1]))
        return max(swim[-1], bug[-1], hw[-1])
            
    CVacation(3,[10,20,30],[40,50,60],[70,80,90])
    CVacation(1,[100],[10],[1])
    CVacation(7,[6,8,2,7,4,2,7],[7,8,5,8,6,3,5],[8,3,2,6,8,4,1])