import time
'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    if len(arr) <= 2:
        return sorted(arr, reverse=True) 
    if arr.count(0) == 2:
        return [0] * len(arr)
    ans = [] 
    # apply product function to all indexes besides the current index in the array
    for i in range(len(arr)):
        newArr = []
        for idx in range(len(arr)):
            if idx != i:
                newArr.append(arr[idx])
    # product function appends the product of all other indexes to a ans list 
        result = 1
        for x in newArr:
            result *= x
        ans.append(result)
    return ans

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2000, 3, 4, 5]
    arr = [2000, 6, 9, 8, 2000, 2000, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 7, 8, 6, 2000, 6, 4, 8, 9, 5, 4, 9, 70, 3, 9, 7, 9, 2000, 6, 8, 5, 5, 4, 7, 7, 5, 8, 7, 6, 5, 7, 7, 7, 8, 701, 200050]
    start_time = time.time()
    printthis = product_of_all_other_numbers(arr)
    end_time = time.time()
    thetime = float(end_time) - float(start_time)
    print(f"Output of product_of_all_other_numbers: {printthis} \n Ran in: {thetime}s")
