'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # old code
    # counter = 0
    # for i in range(len(arr)):
    #     if arr[counter] == 0:
    #     # pop idx, append 0
    #         arr.pop(counter)
    #         arr.append(0)
    #     else:
    #         counter += 1
    # return arr
    left = 0
    right = len(arr) - 1
    for i in range(len(arr)):
        if arr[left] == 0 and arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        elif arr[left] != 0:
            left += 1
        elif arr[right] == 0:
            right -= 1
        if right <= left:
            return arr

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 0, 0, 3, 2, 1]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")