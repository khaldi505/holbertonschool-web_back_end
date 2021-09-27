export default function createEmployeesObject(departmentName, employees) {
    let result = {
        [`${departmentName}`]: employees
    }
    return result
   }
