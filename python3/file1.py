#https://leetcode.com/problems/two-sum/description/

def sum(array: list, target: int) -> int:
    for i in  array:
        for f in array:
            if (i +f) == target:
             print(i,f)

#--------------------------------------------------------------------------------------------                   

# https://leetcode.com/problems/palindrome-number/description/

def isPalindrome (n: int) -> bool:

    array = [int(x) for x in str(n)] 
    invertedArray = array[::-1]
    
    if (array == invertedArray):
        print(True)
    else:
        print(False)

    
#--------------------------------------------------------------------------------------------      
# https://leetcode.com/problems/valid-parentheses/description/

#This funcion does nort verify parenthesys order, only if the number of open and close parenthesis is the same

def validParenthesis (a: list) -> bool:

    c1, c2 = 0, 0  # ()
    c3, c4 = 0, 0  # {}
    c5, c6 = 0, 0  # []
     
    for i in a:
        if (i == '('):
            c1 += 1
        elif (i == ')'):
            c2 += 1
        elif (i == '{'):
            c3 += 1
        elif (i == '}'):
            c4 += 1
        elif (i == '['):
            c5 += 1
        elif (i == ']'):
            c6 += 1    

    if (c1 == c2 ) and (c3 == c4 ) and (c5 == c6):
        print("True")
    else:
        print("False")

#--------------------------------------------------------------------------------------------      
#https://leetcode.com/problems/remove-element/description/

def removeElement(a:list,  n: int) -> list:

    for i in a:
         if (a[i] == n):
            a.remove(a[i])
            
    return print(a)

