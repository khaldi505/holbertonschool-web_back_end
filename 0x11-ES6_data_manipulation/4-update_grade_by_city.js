export default function updateStudentGradeByCity(getListStudents, city, newGrades) {
  const students = getListStudents.filter((stud) => stud.location === city);
  return students.map((student) => {
    const studentGrade_byId = newGrades.filter((element) => element.studentId === student.id);
    try {
      if (studentGrade_byId[0].grade) { student.grade = studentGrade_byId[0].grade; }
    } catch (e) {
      student.grade = 'N/A';
    }
    return student;
  });
}
