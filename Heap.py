import heapq, List

class Heap:
    # Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]
    
    # IPO
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = [(capital[i], profits[i]) for i in range(n)]
        projects.sort()
        maxHeap = []
        i = 0
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(maxHeap, -projects[i][1])
                i += 1
            if not maxHeap:
                break
            w -= heapq.heappop(maxHeap)

        return w
    
    # Find K Pairs with Smallest Sums
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        min_heap = []
        result = []

        for i in range(len(nums1)):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        while k > 0 and min_heap:
            # Pop the pair with the smallest sum
            _, i, j = heapq.heappop(min_heap)  
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                # Push the next pair into the min-heap
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j+1))

            k -= 1

        return result
    
# Find Median from Data Stream
class MedianFinder:
    def __init__(self):
        self.lo = []  
        self.hi = []  

    def addNum(self, num):
        heapq.heappush(self.lo, -num)             # lo is maxheap, so -1 * num
        heapq.heappush(self.hi, -self.lo[0])      # hi is minheap
        heapq.heappop(self.lo)
        
        if len(self.lo) < len(self.hi):
            heapq.heappush(self.lo, -self.hi[0])
            heapq.heappop(self.hi)
            
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]                  
        else:
            return (self.hi[0] - self.lo[0]) / 2  # - as low has -ve values