// @ts-check

/**
 * Converts an array of numbers to a number.
 *
 * @param {number[]} arr
 * @returns {number} the number from the converted array
 */
function arrayToNumber(arr) {
  return Number(arr.join(''));
}

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  return arrayToNumber(array1) + arrayToNumber(array2);
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  const reversedStr = [...String(value)].reverse().join('');

  return String(value) === reversedStr;
}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if (!(input)) {
    return 'Required field';
  }
  if (Number(input)) {
    return '';
  }
  return 'Must be a number besides 0';
}
