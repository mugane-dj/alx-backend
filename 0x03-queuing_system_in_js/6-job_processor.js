// Job processor
import { createQueue } from 'kue';

const push_notification_code = createQueue();

push_notification_code.process('send notification', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}
