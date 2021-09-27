export default function createEmployeesObject(departmentName, employees) {
  const result = {
    [`${departmentName}`]: employees,
  };
  return result;
}
