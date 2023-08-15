#!/usr/bin/node

/**
 *defines a Sqaure class.
 *that inherits from a rectangle
 *takes 1 arg "size"
 */

module.exports = class Square extends require('./4-rectangle'){
	constructor (size){
		super(size, size);
	}
};
