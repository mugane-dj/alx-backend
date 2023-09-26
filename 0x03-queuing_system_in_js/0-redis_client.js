// create redis client
import { createClient } from 'redis';

(async () => {
  await createClient()
  .on('error', err => console.log(`Redis client not connected to the server: ${err}`))
  .on('ready', () => console.log('Redis client connected to the server'))
  .connect();
})();
