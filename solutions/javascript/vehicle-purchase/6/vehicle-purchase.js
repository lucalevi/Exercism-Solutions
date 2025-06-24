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
  let better = option1;
  if (option1 > option2) {
    better = option2;
  }
  return `${better} is clearly the better choice.`
}

/**
 * Calculates the price multiplier based on the age of a vehicle
 *
 * @param {number} age
 * @returns {number} price multiplier for a given age
 */
export function calculatePriceMultiplier(age) {
  const PRICE_MULTIPLIER_NEW = 0.8; // Less than 3 years old
  const PRICE_MULTIPLIER_OLD = 0.5;  // More than 10 years old
  const PRICE_MULTIPLIER_MEDIUM = 0.7; // 3 to 10 years old


  if (age < 3) {
    return PRICE_MULTIPLIER_NEW;
  } else if (age > 10) {
    return PRICE_MULTIPLIER_OLD;
  } else {
    return PRICE_MULTIPLIER_MEDIUM;
  }

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

  return originalPrice * calculatePriceMultiplier(age);
}
