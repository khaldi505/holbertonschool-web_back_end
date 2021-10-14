export default function iterateThroughObject(reportWithIterator) {
  const result = [];
  for (const rep of reportWithIterator) {
    result.push(rep);
  }
  return result.join(' | ');
}
