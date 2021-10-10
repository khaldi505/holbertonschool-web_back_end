export default function cleanSet(set, startString){
let counter = 0
let result = "" 
set.forEach(element => {
    if (element.startsWith(startString) && startString !== "") {
        if (counter === set.size - 1){
            result += element.slice(startString.length, element.length)
        } else { result += element.slice(startString.length, element.length) + "-" }
        counter += 1;
    }
})
    return result
}
