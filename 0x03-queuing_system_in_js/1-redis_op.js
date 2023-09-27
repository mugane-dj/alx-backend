// create redis client & implement set get functions
import { createClient, print } from 'redis';

const client = createClient();

client.on("error", function(err) {
 console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", function() {
  console.log('Redis client connected to the server');
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
