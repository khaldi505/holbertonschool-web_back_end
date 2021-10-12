export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') { return ''; }
  if (typeof set !== typeof (new Set())) { return ''; }
  if (startString === '') { return ''; }
  const result = [];
  set.forEach((element) => {
    if (element && element.startsWith(startString) && startString !== '') {
      result.push(element.slice(startString.length, element.length));
    }
  });
  return result.join('-');
}
