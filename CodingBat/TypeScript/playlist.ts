// Given an array of integers with each integer representing
// the length of a song in seconds, find the total combination
// of pairs of songs that can be added together to end at a
// whole minute.

function playlist(songs: number[]) {
  let numResults: number = 0;
  const songsObj: object = {};

  for (let i: number = 0; i < songs.length; i++) {
    const mod: number = songs[i] % 60;
    let searchMod: number = Math.abs(mod - 60);

    if (searchMod === 60) searchMod = 0;

    if (songsObj.hasOwnProperty(searchMod)) {
      numResults += songsObj[searchMod].length;
    }

    if (songsObj.hasOwnProperty(mod)) {
      songsObj[mod].push(songs[i]);
    } else {
      songsObj[mod] = [songs[i]];
    }
  }
  return numResults;
}

console.log(playlist([60,60,60])) // 3
console.log(playlist([30,20,150, 100, 40])) // 3
console.log(playlist([10,50,90, 30])) // 2
console.log(playlist([40,20,60])) // 1
console.log(playlist([60,60,60, 30, 20, 150, 100, 40, 10, 50, 90, 30])) //12
console.log(playlist([60,60,60,60,60])) // 10