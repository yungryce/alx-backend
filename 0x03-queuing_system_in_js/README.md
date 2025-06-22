# 0x03. Queuing System in JS

## Project Overview
This project introduces the fundamentals of queuing systems and demonstrates how to implement a simple job queue using Node.js and Redis. You will build, test, and observe queue operations, job processing, and publish/subscribe patterns in a backend environment.

## Learning Objectives
- Understand the basics of queuing systems and their use cases.
- Implement job queues and workers using Node.js and Redis.
- Use publish/subscribe patterns for real-time notifications.
- Handle asynchronous job processing and error scenarios.

## Requirements
- Node.js (v14+ recommended)
- Redis server
- Install dependencies with `npm install`

## Project Structure
- `0-redis_client.js` – Basic Redis client setup.
- `1-redis_op.js`, `2-redis_op_async.js`, `4-redis_advanced_op.js` – Redis operations (sync/async, advanced).
- `5-publisher.js`, `5-subscriber.js` – Pub/Sub example.
- `6-job_creator.js`, `6-job_processor.js` – Simple job queue and worker.
- `7-job_creator.js`, `7-job_processor.js`, `8-job.js`, `8-job.test.js` – Advanced job queue and tests.
- `9-stock.js` – Stock management with queues.
- `package.json` – Project dependencies and scripts.
- `README.md` – Project documentation.

## Usage
1. Start Redis server locally:
   ```zsh
   redis-server
   ```
2. Install dependencies:
   ```zsh
   npm install
   ```
3. Run any script, e.g.:
   ```zsh
   node 6-job_creator.js
   node 6-job_processor.js
   ```
4. Observe queue operations and job processing in the console.

## Example
```
$ node 6-job_creator.js
Job created: { id: 1, data: ... }
$ node 6-job_processor.js
Processing job: { id: 1, data: ... }
```
