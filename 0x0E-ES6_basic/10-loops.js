export default function appendToEachArrayValue(array, appendString) {
  let counter = 0;
  for (let value of array) {
    array[counter] = appendString + value;
    counter += 1;
  }
  return array;
}
