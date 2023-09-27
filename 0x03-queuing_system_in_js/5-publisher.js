// pub/sub in redis client
import { createClient } from 'redis';

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

function publishMessage (message, time) {
  setTimeout(() => {
    console.log(`About to send MESSAGE ${message}`);
    client.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
