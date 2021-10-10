export default function cleanSet(set, startString){
if (typeof startString === "String") {return ""}
if (typeof set !== typeof(new Set)) {return ""}

let counter = 0
let result = [] 

set.forEach(element => {

if (element && element.startsWith(startString) && startString !== "") {
result.push(element.slice(startString.length, element.length))
}})
return result.join('-')
}
