// create redis client and implement redis hset
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

const hashSet = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

for (const key in hashSet) {
  if (hashSet.hasOwnProperty(key)) {
    const val = hashSet[key];
    client.hset('HolbertonSchools', key, val, print);
  }
}

client.hgetall('HolbertonSchools', function(err, results) {
  if (err) {
    console.error(err);
  } else {
    console.log(results);
  }
});
