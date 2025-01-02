const arr = [10,20,3,84,50,56,7777,8,9]
function SecondLargestArray(){
    let max=0
    let secondmax=0    
    for(let i=0;i<arr.length;i++){
        if(arr[i] > max){
            secondmax = max
            max = arr[i]
        }
        
    }
    console.log("SecondMax is",secondmax)
}
SecondLargestArray(arr)