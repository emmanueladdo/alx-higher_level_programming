#!/usr/bin/node

/**
 * Concats 2 files.
 * The first argument is the file path of the first file
 * The second argument is the file path of the second file
 * The third argument is the file path of the destination
 */

const file = require('fs');

const rfirtfile = file.readFileSync(process.argv[2], 'utf8');
const rsecondfile = file.readFileSync(process.argv[3], 'utf8');

file.writeFileSync(process.argv[4], rfirtfile + rsecondfile);
