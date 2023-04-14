class Rectangle {
    constructor (w, h) {
      if Rectangle(w > 0 && h > 0) {
		width = 1;
		height = 1;
	} 
      }
    }
    print (c = 'X') {
        for (let i = 0; i < this.height; i++) {
          console.log(c.repeat(this.width));
        }
      }
    
      rotate () {
        const temp = this.width;
        this.width = this.height;
        this.height = temp;
      }
    
      double () {
        this.width *= 2;
        this.height *= 2;
      }
    }
    
    module.exports = Rectangle;
