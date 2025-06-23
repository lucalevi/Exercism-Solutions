// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Determines whether or not you need a license to operate a certain kind of vehicle.
 *
 * @param {string} kind
 * @returns {boolean} whether a license is required
 */
export function needsLicense(kind) {
  return kind === "car" || kind === "truck";
}

/**
 * Helps choosing between two options by recommending the one that
 * comes first in dictionary order.
 *
 * @param {string} option1
 * @param {string} option2
 * @returns {string} a sentence of advice which option to choose
 */
export function chooseVehicle(option1, option2) {
  const better = (option1 < option2) ? option1 : option2;
  return `${better} is clearly the better choice.`
}

/**
 * Calculates an estimate for the price of a used vehicle in the dealership
 * based on the original price and the age of the vehicle.
 *
 * @param {number} originalPrice
 * @param {number} age
 * @returns {number} expected resell price in the dealership
 */
export function calculateResellPrice(originalPrice, age) {
  // Input Validation
  if (typeof originalPrice !== 'number' || originalPrice <= 0) {
    throw new Error("Original price must be a positive number.");
  }
  if (typeof age !== 'number' || age < 0) {
    throw new Error("Age must be a non-negative number.");
  }

  const PRICE_MULTIPLIER_NEW = 0.8; // Less than 3 years old
  const PRICE_MULTIPLIER_OLD = 0.5;  // More than 10 years old
  const PRICE_MULTIPLIER_MEDIUM = 0.7; // 3 to 10 years old

  if (age < 3) {
    return originalPrice * PRICE_MULTIPLIER_NEW;
  }

  if (age > 10) {
    return originalPrice * PRICE_MULTIPLIER_OLD;
  }

  // If neither of the above conditions were met, it must be between 3 and 10 (inclusive)
  return originalPrice * PRICE_MULTIPLIER_MEDIUM;
}
