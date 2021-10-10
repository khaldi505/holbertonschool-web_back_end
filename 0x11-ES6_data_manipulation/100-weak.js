export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const counter = weakMap.get(endpoint) || 0;
  if (counter !== undefined) weakMap.set(endpoint, counter + 1);
  if (weakMap.get(endpoint) >= 5) throw Error('Endpoint load is high');
}
