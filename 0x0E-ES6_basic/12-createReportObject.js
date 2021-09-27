export default function createReportObject(employeesList) {
  const getNumberOfDepartments = () => Object.keys(employeesList).length;
  const result = {
    allEmployees: employeesList,
    getNumberOfDepartments,
  };
  return result;
}
