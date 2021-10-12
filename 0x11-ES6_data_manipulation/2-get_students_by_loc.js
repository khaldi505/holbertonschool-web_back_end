export default function getStudentsByLocation(getListStudents, city) {
  return getListStudents.filter((element) => element.location === city);
}
