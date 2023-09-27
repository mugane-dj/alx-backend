// Creating a job queue with Kue
import { createQueue } from 'kue';

const push_notification_code = createQueue();

const job = push_notification_code.create('send notification', {
      phoneNumber: '4153518780',
      message: 'This is the code to verify your account',
}).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
