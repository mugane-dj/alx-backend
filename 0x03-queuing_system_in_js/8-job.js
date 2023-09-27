// Create job function
const createPushNotificationsJobs = (jobs, push_notification_code_3) => {
  if (!Array.isArray(jobs)) console.log('Jobs is not an array');
  for (const obj of jobs) {
    const job = push_notification_code_3.create('send notification', obj)
    .save((err) => {
      if (!err) console.log(`Notification job created: ${job.id}`);
    });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (errorMessage) => {
      console.log(`Notification job ${job.id} failed: ${errorMessage}`);
    }).on('progress', (progress) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  }
}
module.exports = createPushNotificationsJobs;
