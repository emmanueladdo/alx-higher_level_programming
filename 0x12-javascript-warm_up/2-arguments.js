#!/usr/bin/node
const argumentsNum = process.argv.length;
if (argumentsNum > 2) {
	console.log('Argument found');
} else {
	console.log('No argument');
}
