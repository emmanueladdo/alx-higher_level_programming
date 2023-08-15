#!/usr/bin/node

/**
 *defines a Sqaure class.
 *that inherits from a rectangle
 *takes 1 arg "size"
 *Creates an instance method called charPrint(c).
 * Prints the rectangle using the character c
 * Uses the character X If c is undefined
 */

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
