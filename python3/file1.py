#https://leetcode.com/problems/two-sum/description/

def sum(array: list, target: int) -> int:
    for i in  array:
        for f in array:
            if (i +f) == target:
             print(i,f)

# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome (n: int) -> bool:

    array = [int(x) for x in str(n)] 
    invertedArray = array[::-1]
    
    if (array == invertedArray):
        print(True)
    else:
        print(False)

    

   