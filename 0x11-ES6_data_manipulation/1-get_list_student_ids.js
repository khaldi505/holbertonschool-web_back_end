export default function getListStudentIds(getListStudents) {
  if (Array.isArray(getListStudents)) {
    return getListStudents.map((element) => element.id);
  }
  return [];
}
