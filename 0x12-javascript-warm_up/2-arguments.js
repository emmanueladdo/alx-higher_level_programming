#!/usr/bin/node
const argumentNum = process.argv.length - 2;
if (argumentNum == 1) {
	console.log('Argument found');
} else if (argumentNum > 1) {
	console.log('Arguments found');
} else {
	console.log('No Argument');
}

