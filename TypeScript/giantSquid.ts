/**
 * --- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
 */
console.log('Hi');
const fs = require('fs');
const text: string = fs.readFileSync('TypeScript/rawData/giantSquidData.txt', 'utf-8');
const textByLine: string[] = text.split('\n\n');

// console.log(textByLine.slice(0, 1));
const callNumbers: number[] = textByLine.slice(0, 1)[0].split(',').map((num) => Number(num));
// console.log(callNumbers);

// try splitting on empty line
const wholeBoards: string[] = textByLine.slice(1);
// console.log(boards[0]);

// split each board into rows
// split each row into an array of string numbers
// convert each string number to a number
const rowBoards = wholeBoards.map((data) => {
  return data.split('\n').map((row) => {
    return row.split(' ').filter((val) => {
      return val !== ''}).map((val) => {
        return Number(val);
    })
  })
})
// console.log('hi');
// console.log(rowBoards);

console.log('Hi');


function giantSquid(board: number[][][], callNumbers: number[]) {
  console.log('Hi');
  let gameOver: boolean = false;
  let store: {
    board: number;
    row: number;
    column: number;
    notCalledNumbers: number[];
    lastNumber: number;
  } = {
    board: 0,
    row: 0,
    column: 0,
    notCalledNumbers: [],
    lastNumber: 0
  }

  let ctr: number = 0;
  while (gameOver === false) {
    // get the called number and push it to the store calledNumbers
    const currentNum = callNumbers[ctr];
    console.log(currentNum);
    Loop through each column and row of each board, if the number exists, turn it into a string
    for (let i: number = 0; i < board.length; i++) {
      for (let j: number = 0; j < board[i].length; j++) {
        // Initialize a counter to count the number of number-strings in each column;
        const colNumStr: number[] = [0,0,0,0,0];
        // Initialize a counter to count the number of number-strings in each row;
        let rowNumStr = 0;
        for (let k: number = 0; k < board[i][j].length; k++) {
          if (currentNum === board[i][j][k]) {
            board[i][j][k].toString();
            rowNumStr++;
          } else if (typeof board[i][j][k] === 'string') {
            rowNumStr++;
          }

          // Check the horizontal and the vertical for winning conditions;
          // Check each horizontal to see if the game is done;
          if (rowNumStr === 5) {
            console.log(`The winning board is board is number: ${i}. \n Here is the board: ${board[i]}. \n The winning row is: ${j} which is ${board[i][j]}. \n The winning number is ${board[i][j][k]}.` );
            store.board = i;
            store.row = j;
            store.column = k;
            store.lastNumber = board[i][j][k];
            gameOver = true;
            // Break out of while loop and pass on some info;
            break;
          }
          // Check each verticalboard to see if it is correct;
          for (let n: number = 0; n < colNumStr.length; n++) {
            if (colNumStr[n] === 5) {
              gameOver = true;
              console.log(`The winning board is board is number: ${i}. \n Here is the board: ${board[i]}. \n The winning column is: ${k} which is ${board[i]}. \n The winning number is ${board[i][j][k]}.` );
              store.board = i;
              store.row = j;
              store.column = k;
              store.lastNumber = board[i][j][k];
              gameOver = true;
            }
            break;
          }
        }
      }
    }
    ctr++;
    if (ctr >= 10) {
      gameOver = true;
    }
  }

  console.log('Hi');
  for (let i: number = 0; i < board[store.board].length; i++) { // Chooses the rows;
    for (let j: number = 0; j < board[store.board][i].length; j++) { // Chooses the row x column;
      if (typeof board[store.board][i][j] === 'number') {
        store.notCalledNumbers.push(board[store.board][i][j]);
      }
    }
  }

  const sum = store.notCalledNumbers.reduce((acc, num) => {
    return acc = acc + num;
  }, 0);

  console.log(`The sum is ${sum} and the last bingo number called is ${store.lastNumber}, the total result is ${sum * store.lastNumber}.`);
  return sum * store.lastNumber;
}


// console.log(rowBoards[0]);
console.log(giantSquid(rowBoards, callNumbers))