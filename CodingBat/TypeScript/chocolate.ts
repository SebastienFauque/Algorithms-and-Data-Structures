/**
 * We want make a package of goal kilos of chocolate. We have
small bars (1 kilo each) and big bars (5 kilos each). Return
the number of small bars to use, assuming we always use big
 bars before small bars. Return -1 if it can't be done.
make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2
 */

function chocolate(small:number, big: number, goal: number): number {
  if (!goal || !small && !big) return -1;

  if (goal > (small + big*5)) return -1;
  else {

    let ctr: number = 0;
    while (goal > 0 && (small > 0 || big > 0)) {

      if (big > 0 && goal >=5) {
        big--;
        goal -= 5;
      } else {
        small--;
        ctr++;
        goal--;
      }
      if (goal === 0) return ctr;
    }
  }
  return -1;
}


console.log(chocolate(4, 1, 9)); // 4
console.log(chocolate(4, 1, 10)); // -1
console.log(chocolate(4, 1, 7)); // 2