// https://leetcode.com/problems/two-sum/description/

function sum (array , target){

    var lenght = array.length;
     
    for(let step = 0; step < lenght; step++){
        for(let step2 = 0; step2 < lenght; step2++){
            if(array[step] + array[step2] == target)[
                console.log(array[step],"+",array[step2],"=", target)
            ]
         }
    }
}


sum([1,2,3,4,5], 5)

