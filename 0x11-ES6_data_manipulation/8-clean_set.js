export default function cleanSet(set, startString){
let result = "";
let counter = set.size 
set.forEach(element => {
if (element && element.startsWith(startString) && startString !== "") {
if (counter != 2){ 
result += element.slice(startString.length, element.length) + "-" 
}
else { result += element.slice(startString.length, element.length) }
}
counter -= 1
});
if (result.endsWith('-')){result = result.slice(0, result.length - 1)}
return result
}
