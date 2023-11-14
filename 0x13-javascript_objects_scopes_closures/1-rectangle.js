#!/usr/bin/node
// Defines a class Rectangle

class Rectangle {
  // Constructor that takes 2 arguments w and h
  constructor (w, h) {
    // initialize the instance attribute width with the value of w
    this.width = w;
    // initialize the instance attribute height with the value of h
    this.height = h;
  }
}

// Export the class
module.exports = Rectangle;
