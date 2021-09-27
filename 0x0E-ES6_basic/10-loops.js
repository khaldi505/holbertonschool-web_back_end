export default function appendToEachArrayValue(array, appendString) {
  let counter = 0;
  for (const value of array) {
    array[counter] = appendString + value;
    counter += 1;
  }
  return array;
}
