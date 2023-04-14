#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if Rectangle(w > 0 && h > 0) {
		width = 1;
		height = 1;
	} 
      }
    }
  }
  
  print (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
