import time
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.values = {}
    def append(self, item):
        self.counter += 1
        if self.counter >= self.capacity:
            self.counter = 0
        self.values[f"{self.counter}"] = item
    def get(self):
        result = []
        for value in self.values.values():
            result.append(value)
        return result
'''
Input: an integer
Returns: an integer
'''
# Matt's Solution
# def eating_cookies(n, cache=None):
#     # check for negative values
#     if n < 0:
#         # getting to a negative number mean we didn't
#         # find one of the ways
#         return 0
#     # base case: when there are no more cookies
#     if n == 0:
#         # getting to 0, means we found a way to eat
#         # our cookies
#         return 1
#     # if no cache yet, create one
#     if cache is None:
#         cache = [0] * (n + 1)
    
#     # check for previously computed answer in our cache
#     if cache[n] != 0:
#         return cache[n]
#     # this represents our recursive case
#     # three possible decisions
#     # eat 1 cookie, 2 cookies, or 3 cookies
#     cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
#     return cache[n]
# My solution
# def eating_cookies(n, other=None):
#     if n <= 1:
#         return 1
#     if n == 2:
#         return 2
#     if n >= 3:
#         i = 3
#         values = {
#             0: 1,
#             1: 1,
#             2: 2
#         }
#         while i <= n: 
#             values[i] = values[i - 3] + values[i - 2] + values[i - 1]
#             i += 1        
#     return values[n]
# No recursion depth error here 
# Matt's solution using ring buffer
def eating_cookies(n, other=None):
    cache = RingBuffer(3)
    cache.append(1)
    cache.append(1)
    cache.append(2)
    if n < 0:
        return 0
    if n <= 1 and n >= 0:
        return 1
    for i in range(2, n + 1):
        if i != n:
            current_cache = cache.get()
            cache.append(sum(current_cache))
    return max(cache.get())
# Maximum efficiency at 100k cookies    
    
# 0  1  2  3  4  5   6   7   8   9    10   11   12   13    14    15    16
# 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 100000
    start_time = time.time()
    ate = eating_cookies(100000)
    end_time = time.time()
    sec = float(end_time) - float(start_time)
    print(f"There are {ate} ways for Cookie Monster to eat {num_cookies} cookies \n calculated in {sec:.30f}s")
