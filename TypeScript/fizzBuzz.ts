/**
 * Write a function that takes in an integer value n and logs
 * the value of that integer and all values below it if it is not
 * evenly divisible by 3 or 5. If divisible by 3, log "Fizz", if
 * divisible by 5, log "Buzz", and if divisible by both 3 and 5,
 * log "FizzBuzz".
 *
 * The function should not return anything if the input is valid..
 * If n does not exist or n is negative, return -1.
 * if n is 0, return 0;
 */

const fizzBuzz = (n?: number) => {
  if (n === 0) return 0;
  if (n < 0 || !n) return -1;

  let ctr: number = 1;
  while (ctr <= n) {
    let logMsg: string = ``;
    if (ctr % 3 === 0) logMsg += `Fizz`;
    if (ctr % 5 === 0) logMsg += `Buzz`;
    if (!logMsg.length) logMsg += `${ctr}`;
    console.log(logMsg);
    ctr++;
  }
  return;
}



// console.log(fizzBuzz()) //-1
// console.log(fizzBuzz(-1)) //-1
// console.log(fizzBuzz(0)) //0
// console.log(fizzBuzz(1)) //1
// console.log(fizzBuzz(2)) //1, 2
// console.log(fizzBuzz(3)) //1, 2, Fizz
// console.log(fizzBuzz(4)) //1, 2, Fizz, 4
// console.log(fizzBuzz(5)) //1, 2, Fizz, 4, Buzz
// console.log(fizzBuzz(6)) //1, 2, Fizz, 4, Buzz, Fizz
console.log(fizzBuzz(15)) //1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz