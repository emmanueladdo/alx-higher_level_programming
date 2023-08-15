#!/usr/bin/node

/**
 *defines a Rectangle class.
 *Instance attribute width with the value of w
 *Instance attribute height with the value of h
 *creates an empty object  if w or h is zero or negative
 *print function that prints the rectangle
 *rotate function that rotates the values
 *double function that multiples by 2
 */

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
