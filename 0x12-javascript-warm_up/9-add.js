#!/usr/bin/node
const f = parseInt(process.argv[2]);
const s = parseInt(process.argv[3]);
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return NaN;
  }
  return a + b;
}
console.log(add(f, s));
