// create redis client & implement set and get functions
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on("error", function(err) {
 console.log(`Redis client not connected to the server: ${err}`);
});

client.on("connect", function() {
  console.log('Redis client connected to the server');
});

const getAsync = promisify(client.get).bind(client);

function setNewSchool (schoolName, value) {
  client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
 try {
   const reply = await getAsync(schoolName);
   console.log(reply);
 } catch (error) {
   console.error(error);
 }
}

(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();
