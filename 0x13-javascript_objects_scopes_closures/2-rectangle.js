#!/usr/bin/node

/**
 *defines a Rectangle class.
 *Instance attribute width with the value of w
 *Instance attribute height with the value of h
 */

module.exports = class Rectangle {
  constructor (w, h) {
	  if (w > 0 && h > 0) {
		  this.width = w;
		  this.height = h;
	  }
  }
};
