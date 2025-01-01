const array = [2,2,3,4,9,9]

function remove_Duplicates(arr){
    const uniqueElements = [];
    for (let i = 0; i < arr.length; i++) {
        if (!uniqueElements.includes(arr[i])) {
            uniqueElements.push(arr[i]);
        }
    }
    return uniqueElements;
}
let ans = remove_Duplicates(array)
console.log(ans)