#!/usr/bin/node
/**
 *scripts computes the number task
 *
 */

const request = require('request');

const apiUrl = process.argv[2]; // Get the API URL from command line arguments

if (!apiUrl) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

// Initialize an object to store the count of completed tasks per user
const completedTasksByUser = {};

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error.message}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Status code ${response.statusCode}`);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach((task) => {
      if (task.completed) {
        if (completedTasksByUser[task.userId]) {
          completedTasksByUser[task.userId]++;
        } else {
          completedTasksByUser[task.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
