import redis from 'redis';

const client = redis.createClient();
const { promisify } = require('util');

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const getasync = promisify(client.get).bind(client);
  const value = await getasync(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
