// Find the minimum number of jumps needed to reach
//  a flag at the top of a pole.
// You are given a flag height represented by an
// integer and you are able to make a normal jump
// which increase your height by 1 or you can make
// a big jump which increase your height by a provided
// number. Calculate the minimum jumps needed to
// reach the flag.

function jumps(flagHeight: number, bigJump: number) {
  if (!flagHeight || !bigJump) return undefined;

  let current: number = 0;
  let jumps: number = 0;

  while (current < flagHeight) {
    if ((flagHeight - current) >= bigJump) {
      current += bigJump;
      jumps += 1;
    } else {
      current += 1;
      jumps += 1;
    }
  }
  return jumps;
}

console.log(jumps(8, 3)); // 4
console.log(jumps(3, 1)); // 3
console.log(jumps(3, 2)); // 2
console.log(jumps(3, 3)); // 1

