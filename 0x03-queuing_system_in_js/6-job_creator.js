// Creating a job queue with Kue
import { createQueue } from 'kue';

const push_notification_code = createQueue();

const job = push_notification_code.create('send message', {
      phoneNumber: '+254786523142',
      message: 'Hello Holberton!',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
});

job.on('failed', () => {
  console.log('Notification job failed');
});
