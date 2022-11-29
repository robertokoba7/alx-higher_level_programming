#!/usr/bin/node

class Rectangle {
	constuctor (w, h) {
		if ((w > 0) && (h > 0)) {
			this.width = w;
			this.height = h;
		}
	}

	print() {
		for (let i = 0; i < this.height; i++) {
			let square = '';
			for (let j = 0; j < this.width; j++) {
				square += 'X';
			}
			console.log(s);
		}
	}

	rotate() {
		const aux = this.width;
		this.width = this.height;
		this.height = aux;
	}

	double() {
		this.width *= 2;
		this.height *= 2;
	}
}

module.exports = Rectangle;
