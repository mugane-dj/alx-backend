// create redis client & implement set and get functions
import { createClient, print } from 'redis';

const client = createClient();

client.on("connect", function() {
  console.log('Redis client connected to the server');
});

client.on("error", function(err) {
  if (err.code === 'ECONNREFUSED') {
    console.log(`Redis client not connected to the server: ${err}`);
  } else {
    throw err;
  }
});

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

function displaySchoolValue (schoolName) {
  client.get(schoolName, function (err, reply) {
    console.log(reply);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
