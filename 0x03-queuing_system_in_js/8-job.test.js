// Tests for createPushNotificationsJobs function
import { createQueue } from 'kue';
import chai from 'chai';
import sinon from 'sinon';
import createPushNotificationsJobs from './8-job.js';

const expect = chai.expect;

describe('createPushNotificationsJobs', () => {
  const queue = createQueue();
  before(() => {
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
  });

  after(() => {
    queue.testMode.exit()
  });

  it('Logs an error when jobs arg is not an array', () => {
    const consoleSpy = sinon.spy(console, 'log');

    createPushNotificationsJobs("list", queue);
    expect(consoleSpy.calledOnceWithExactly('Jobs is not an array'));
    consoleSpy.restore();
  });
  
  it('creates jobs in the queue', () => {
    const jobs = [{}, {}, {}];
    
    const consoleSpy = sinon.spy(console, 'log');
    createPushNotificationsJobs(jobs, queue);
    expect(consoleSpy.callCount).to.equal(jobs.length);
    consoleSpy.restore();
  });
});
