#!/usr/bin/node

/**
 * Imports an array and computes a new array
 * Imports list from the file 100-data.js
 * New list is created with each value equal
 * to the value of the initial list,
 * multipled by the index in the list
 * Both the initial list and the new list are printed
 */

// Import the array from the file 100-data.js
const { list } = require('./100-data');

// Compute a new array using the map function
const newList = list.map((value, index) => value * index);

// Print the initial list
console.log('Initial List:', list);

// Print the new list
console.log('New List:', newList);
