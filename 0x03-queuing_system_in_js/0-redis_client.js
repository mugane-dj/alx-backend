// create redis client
import { createClient } from 'redis';

const client = createClient();

client.on("error", function(err) {
  if (err.code === 'ECONNREFUSED') {
    console.log(`Redis client not connected to the server: ${err}`);
  } else {
    throw err;
  }
});

client.on("connect", function() {
  console.log('Redis client connected to the server');
});
