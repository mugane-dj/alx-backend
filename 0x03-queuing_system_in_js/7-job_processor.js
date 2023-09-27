// Track progress with Kue
import { createQueue } from 'kue';

const push_notification_code_2 = createQueue();

const blackListed = ['4153518780', '4153518781'];

push_notification_code_2.process('send notification', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
  done();
});

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);
  if (blackListed.includes(phoneNumber)) {
    const err = new Error(`Phone number ${phoneNumber} is blacklisted`);
    done(err);
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  }
}
