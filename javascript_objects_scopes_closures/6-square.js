#!/usr/bin/node

const Rectangle = require('./5-square');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      if (c === undefined) {
        console.log('X'.repeat(this.height));
      } else {
        console.log(c.repeat(this.height));
      }
    }
  }
}
module.exports = Square;
