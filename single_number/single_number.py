'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(lst):
    counts = {}
    for i in lst:
        if i in counts:
            del counts[i]
        else:
            counts[i] = 1 
    for k, v in counts.items():
        if v == 1:
            return k

if __name__ == '__main__':
    # Use the main function to test your implementation
    lst = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(lst)}")