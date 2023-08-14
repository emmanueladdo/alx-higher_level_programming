#!/usr/bin/node

if (process.argv.length > 3) {
  const arg = process.argv.map(Number);
  arg.slice(2);
  arg.sort((a, b) => a - b);
  console.log(args[arg.length - 2]);
} else {
  console.log(0);
}
