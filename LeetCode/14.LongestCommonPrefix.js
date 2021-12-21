/**
 * @param {string[]} strs
 * @return {string}
 */
 var longestCommonPrefix = function(strs) {
  if (!strs.length) return '';

  // Define prefix as strs[0];
  let prefix = strs[0];

  for (let i = 1; i < strs.length; i++) {
      let currentWord = strs[i];
      while (currentWord.indexOf(prefix) !== 0) {
          prefix = prefix.substring(0, prefix.length - 1);
      }
  }

  // Loop through all array items
      // Check if the index of the prefix exists and is at position 0 in the current word.
          // If not there, reduce the prefix length by 1 and check again
  return prefix;
};