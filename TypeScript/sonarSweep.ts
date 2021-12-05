/**
 * The advent of code www.adventofcode.com
*
--- Day 1: Sonar Sweep --- problem 1
You're minding your own business on a ship at sea when
the overboard alarm goes off! You rush to see if you can help.
Apparently, one of the Elves tripped and accidentally sent the
sleigh keys flying into the ocean!

Before you know it, you're inside a submarine the Elves keep ready
for situations like this. It's covered in Christmas lights (because of course
it is), and it even has an experimental antenna that should be able to
track the keys if you can boost its signal strength high enough; there's a
little meter that indicates the antenna's signal strength by displaying 0-50 stars.

Your instincts tell you that in order to save Christmas, you'll need to get
all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on
each day in the Advent calendar; the second puzzle is unlocked when
you complete the first. Each puzzle grants one star. Good luck!

As the submarine drops below the surface of the ocean, it automatically
performs a sonar sweep of the nearby sea floor. On a small screen, the
sonar sweep report (your puzzle input) appears: each line is a measurement
of the sea floor depth as the sweep looks further and further away from
the submarine.

For example, suppose you had the following report:

199
200
208
210
200
207
240
269
260
263

This report indicates that, scanning outward from the submarine,
the sonar sweep found depths of 199, 200, 208, 210, and so on.

The first order of business is to figure out how quickly the depth
increases, just so you know what you're dealing with - you never
know if the keys will get carried into deeper water by an ocean
current or a fish or something.

To do this, count the number of times a depth measurement
increases from the previous measurement. (There is no measurement
before the first measurement.) In the example above, the changes
are as follows:

199 (N/A - no previous measurement)
200 (increased)
208 (increased)
210 (increased)
200 (decreased)
207 (increased)
240 (increased)
269 (increased)
260 (decreased)
263 (increased)

In this example, there are 7 measurements that are larger than the previous measurement.


 */


const sonarSweep = (depths: number[]) => {
  if (!depths || !depths.length) return undefined;

  let previous: number = depths[0];
  let count: number = 0;

  for (let i:number = 1; i < depths.length; i++) {
    if (depths[i] > previous) count++;
    previous = depths[i];
  }

  return count;
}


// Solving the example
const exampleNums: number[] = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263];
console.log(sonarSweep(exampleNums)) // 7

// Solving the real test
const fs = require('fs');
const text: string = fs.readFileSync("TypeScript/sonarSweepText.txt", 'utf-8');
const textByLine: string[] = text.split('\n');

const parse = (testSuite: string[]) => {
  const inputNums: number[] = [];
  for (let i: number = 0; i < testSuite.length; i++) {
    inputNums.push(parseInt(testSuite[i]));
  }
  return inputNums;
}

// console.log(sonarSweep(parse(textByLine))); //1195 Solved!

const sonarSweepSum = (depths: number[]) => {
  if (!depths || !depths.length) return undefined;

  function sum(nums: number[]) {
    return nums[0] + nums[1] + nums[2];
  }

  let previous: number = sum(depths.slice(0, 3));
  let current: number = 0;
  let countDeeper: number = 0;

  for (let i = 1; i < depths.length; i++) {
    current = sum(depths.slice(i, i+3));

    if (current > previous) countDeeper++;
    previous = current;
  }

  return countDeeper;
}


console.log(sonarSweepSum(parse(textByLine)));