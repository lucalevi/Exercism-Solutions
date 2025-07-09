// @ts-check

/**
 * Determine how many cards of a certain type there are in the deck
 *
 * @param {number[]} stack
 * @param {number} card
 *
 * @returns {number} number of cards of a single type there are in the deck
 */
export function cardTypeCheck(stack, card) {
  // 🚨 Use .forEach
  let counter = 0;

  stack.forEach((element) => {
    if (element === card) {
      counter += 1;
    }
  });

  return counter;
}

/**
 * Determine how many cards are odd or even
 *
 * @param {number[]} stack
 * @param {boolean} type the type of value to check for - odd or even
 * @returns {number} number of cards that are either odd or even (depending on `type`)
 */
export function determineOddEvenCards(stack, type) {
  let evenCount = 0;
  let oddCount = 0;

  for (const card of stack) {
    if (card % 2 === 0) {
      evenCount += 1;
    } else {
      oddCount += 1;
    }
  }
  if (type === true) {
    return evenCount;
  } else {
    return oddCount;
  }
}
