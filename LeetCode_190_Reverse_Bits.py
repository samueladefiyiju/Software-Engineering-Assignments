class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        times = 32 
        lst = []
        while (times > 0 ):
            t = n & 1 
            lst.append(t)
            n = n >> 1
            times -=1
        res = 0 
        for i in range(len(lst)):
            res = res << 1
            res = res | lst[i]
        return res 
            

