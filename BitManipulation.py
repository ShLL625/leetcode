import List

class BitManipulation:
    # Add Binary
    def addBinary(self, a: str, b: str) -> str:
        if int(b) > int(a):
            a, b = b, a
        carry = 0
        output = ""
        for i in range(-1, -len(a)-1, -1):
            if abs(i) > len(b):
                sums = int(a[i]) + carry
            else:
                sums = int(a[i]) + int(b[i]) + carry
            output = str(sums%2) + output
            carry = sums // 2
        if carry:
            output = '1' + output
        #print(output)
        return output
    
    # Reverse Bits
    def reverseBits(self, n: int) -> int:
        output = 0
        for i in range(32):
            output = (output << 1) | (n&1)
            n >>= 1 
        return output
    
    # Number of 1 Bits
    def hammingWeight(self, n: int) -> int:
        #O(log n), O(1)
        count = 0
        while n != 0:
            count += n & 1
            n >>= 1
        return count
    
    # Single Number
    def singleNumber(self, nums: List[int]) -> int:
        #1 ^ 1 == 0, 0^single_number = single_number
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
    
    # Single Number II
    def singleNumber(self, nums: List[int]) -> int:
        '''
        count = defaultdict(int)
        for x in nums:
            count[x] += 1

        for x, freq in count.items():
            if freq == 1:
                return x
        
        return -1
        '''
        ones, twos = 0, 0

        for num in nums:
            # Update ones and twos
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones  # The single number remains in "ones"
    
    # Bitwise AND of Numbers Range
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        cnt = 0
        while left != right:
            left >>= 1
            right >>= 1
            cnt += 1
        return left << cnt
    
