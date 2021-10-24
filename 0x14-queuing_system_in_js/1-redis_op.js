import redis from "redis";
const client = redis.createClient();

client.on("error", function(err) {
  console.log("Redis client not connected to the server: " + err.message);
});
client.on("connect", function() {
  console.log("Redis client connected to the server");
});


function setNewSchool(schoolName, value){
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName){
  client.get(schoolName, function(err, rep){
    console.log(rep);
  });
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
