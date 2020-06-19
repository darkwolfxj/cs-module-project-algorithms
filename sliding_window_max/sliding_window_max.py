import collections
'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.counter = 0
#         self.values = {}
#     def append(self, item):
#         self.counter += 1
#         if self.counter >= self.capacity:
#             self.counter = 0
#         self.values[f"{self.counter}"] = item
#     def get(self):
#         result = []
#         for value in self.values.values():
#             result.append(value)
#         return result
# def sliding_window_max(nums, k):
#     lst = RingBuffer(k)
#     # Create a max array
#     # Loop through nums
#     # For each num, find the max from num to num + k
#     # Append max to max array
#     maxes = []
#     i = 0
#     j = 0
#     while i < len(nums) - k + 1:
#         for j in range(j, i + k):
#             lst.append(nums[j])
#             j += 1   
#         maxes.append(max(lst.get()))
#         i += 1
#     return maxes    
def sliding_window_max(nums, k):
    deque = collections.deque()
    res = []
    for i, num in enumerate(nums):
        while(deque and nums[deque[-1]] < num):
            deque.pop()     # 2
        if(deque and i - deque[0] >= k):
            deque.popleft() # 3
        deque.append(i)
        res.append(nums[deque[0]])
    return res[k-1:]


# if __name__ == '__main__':
#     # Use the main function here to test out your implementation 
#     arr = [1, 3, -1, -3, 5, 3, 6, 7]
#     k = 3

#     print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
