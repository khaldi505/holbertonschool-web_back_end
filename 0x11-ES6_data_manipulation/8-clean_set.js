export default function cleanSet(set, startString){
let counter = 2
let result = "" 
set.forEach(element => {
if (element && element.startsWith(startString) && startString !== "") {
if (counter === set.size){
result += element.slice(startString.length, element.length)
} else { result += element.slice(startString.length, element.length) + "-" }
counter += 1;
}
})
return result
}
