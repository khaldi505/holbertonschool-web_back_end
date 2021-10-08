export default function getStudentIdsSum(getListStudents) {
  const result = getListStudents.map((element) => element.id);
  const reducer = (previousValue, currentValue) => previousValue + currentValue;
  return result.reduce(reducer);
}
