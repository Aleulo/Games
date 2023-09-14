const prompt = require('prompt-sync')({ sigint: true });

const hat = '^';
const hole = 'O';
const fieldCharacter = '░';
const pathCharacter = '*';

class Field {
  constructor(array) {
    this._field = array;
    this._x = 0;
    this._y = 0;
    this._gameOver = false;
    this._path = [];
  }

  print() {
    for (const row of this._field) {
      console.log(row.join(' '));
    }
  }

  move(direction) {
    let newX = this._x;
    let newY = this._y;

    switch (direction) {
      case 'r':
        newY++;
        break;
      case 'd':
        newX++;
        break;
      case 'l':
        newY--;
        break;
      case 'u':
        newX--;
        break;
      default:
        console.log('Invalid move. Please use r, d, l, or u.');
        return;
    }

    if (newX < 0 || newX >= this._field.length || newY < 0 || newY >= this._field[0].length) {
      console.log('You went outside the field. Game over!');
      this._gameOver = true;
      return;
    }

    const currentTile = this._field[newX][newY];
    if (currentTile === hat) {
      console.log('Congratulations! You found your hat. You win!');
      this._gameOver = true;
    } else if (currentTile === hole) {
      console.log('Oh no! You fell into a hole. Game over!');
      this._gameOver = true;
    } else {
      this._x = newX;
      this._y = newY;
      this._path.push([this._x, this._y]);
      this._field[this._x][this._y] = pathCharacter;
    }
  }

  isGameOver() {
    return this._gameOver;
  }
}

function generateField(height, width, percentage = 0.2) {
  const field = [];
  for (let i = 0; i < height; i++) {
    const row = [];
    for (let j = 0; j < width; j++) {
      const random = Math.random();
      if (random < percentage) {
        row.push(hole);
      } else {
        row.push(fieldCharacter);
      }
    }
    field.push(row);
  }
  const x = 0;
  const y = 0;
  field[x][y] = pathCharacter; // Start position
  
  const hatX = Math.floor(Math.random() * height);
  const hatY = Math.floor(Math.random() * width);
  field[hatX][hatY] = hat; // Hat position
  return field;
}

function main() {
  const height = 10; // Change to the desired height of the field
  const width = 10; // Change to the desired width of the field
  const field = generateField(height, width);
  const myField = new Field(field);

  console.log('Welcome to the Find Your Hat game!');
  while (!myField.isGameOver()) {
    myField.print();
    const moveDirection = prompt('Enter your move (r, d, l, u): ');
    myField.move(moveDirection);
  }
}

main();
