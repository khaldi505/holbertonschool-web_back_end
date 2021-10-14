export default function createIteratorObject(report) {
  const keys = Object.keys(report.allEmployees);
  const result = [];
  for (const key of keys) {
    result.push(...report.allEmployees[key]);
  }
  return (result);
}
