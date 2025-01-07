#https://leetcode.com/problems/two-sum/description/

def sum(array: list, target: int) -> int:
    for i in  array:
        for f in array:
            if (i +f) == target:
             print(i,f)

    
        
    

