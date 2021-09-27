export default function createReportObject(employeesList) {
  let getNumberOfDepartments
  getNumberOfDepartments = _ => Object.keys(employeesList).length
  const result = {
    allEmployees: employeesList,
    getNumberOfDepartments,
};
  return result;

}
