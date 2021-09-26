function getCurrentYear() {
const date = new Date();
return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
const budget = {
  ['income-2021']: income,
  ['gdp-2021']: gdp,
  ['capita-2021']: capita,
  };
  return budget;
}
