// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines how long it takes to prepare a certain juice.
 *
 * @param {string} name
 * @returns {number} time in minutes
 */
export function timeToMixJuice(name) {
  switch (name) {
    case "Pure Strawberry Joy":
      return 0.5;
    case "Energizer":
      return 1.5;
    case "Green Garden":
      return 1.5;
    case "Tropical Island":
      return 3;
    case "All or Nothing":
      return 5;
    default:
      return 2.5;
  }
}

/**
 * Calculates the number of limes that need to be cut
 * to reach a certain supply.
 *
 * @param {number} wedgesNeeded
 * @param {string[]} limes
 * @returns {number} number of limes cut
 */
export function limesToCut(wedgesNeeded, limes) {
  let howManyLimes = 0;
  let wedgesCut = 0;

  if (wedgesNeeded === 0) {
    return 0;
  }

  for (const lime of limes) {
    if (lime === 'small') {
      wedgesCut += 6;
      howManyLimes += 1;
    } else if (lime === 'medium') {
      wedgesCut += 8;
      howManyLimes += 1;
    } else if (lime === 'large') {
      wedgesCut += 10;
      howManyLimes += 1;
    }

    if (wedgesCut >= wedgesNeeded) {
      break;
    }
  }
  return howManyLimes;
}

/**
 * Determines which juices still need to be prepared after the end of the shift.
 *
 * @param {number} timeLeft
 * @param {string[]} orders
 * @returns {string[]} remaining orders after the time is up
 */
export function remainingOrders(timeLeft, orders) {
  let currentTimeLeft = timeLeft;

  for (let i = 0; i < orders.length; i++) {
    const juiceName = orders[i];
    const mixTime = timeToMixJuice(juiceName);

    currentTimeLeft -= mixTime;

    if (currentTimeLeft <= 0) {
      return orders.slice(i + 1);
    }
  }

  return [];
}
