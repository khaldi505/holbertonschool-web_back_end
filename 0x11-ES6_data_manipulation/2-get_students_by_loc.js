export default function getStudentsByLocation(getListStudents, city){
    const result = Array()
    getListStudents.filter(element =>
        {
            if (element.location === city) {result.push(element)}
        }
        )
        return result
}