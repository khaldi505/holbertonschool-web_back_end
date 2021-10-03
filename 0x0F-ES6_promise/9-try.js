export default function guardrail(mathFunction) {
  const queue = [];
  let temp;
  try {
    temp = mathFunction();
  } catch (err) {
    temp = err.toString();
  }
  queue.push(temp);
  queue.push('Guardrail was processed');
  return queue;
}
