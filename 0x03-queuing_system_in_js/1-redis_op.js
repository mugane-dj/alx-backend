// create redis client & implement set and get functions
import { createClient, print } from 'redis';

let client;

(async () => {
  client = await createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('ready', () => console.log('Redis client connected to the server'))
  .connect();
})();

async function setNewSchool (schoolName, value) {
  await client.set(schoolName, value, print);
}

async function displaySchoolValue (schoolName) {
  const output = await client.get(schoolName);
  console.log(output);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
