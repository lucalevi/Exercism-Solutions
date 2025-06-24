// @ts-check
//
// The line above enables type checking for this file. Various IDEs interpret
// the @ts-check directive. It will give you helpful autocompletion when
// implementing this exercise.

/**
 * Calculates the total bird count.
 *
 * @param {number[]} birdsPerDay
 * @returns {number} total bird count
 */
export function totalBirdCount(birdsPerDay) {
  let totalBirds = 0;
  for (let i = 0; i < birdsPerDay.length; i++) {
    totalBirds += birdsPerDay[i];
  };
  return totalBirds;
}

/**
 * Calculates the total number of birds seen in a specific week.
 *
 * @param {number[]} birdsPerDay
 * @param {number} week
 * @returns {number} birds counted in the given week
 */
export function birdsInWeek(birdsPerDay, week) {
  const DAYS_PER_WEEK = 7;
  const WEEK_OFFSET = 1;
  const WEEK_INDEX = (week - WEEK_OFFSET) * DAYS_PER_WEEK;

  let dayCount = 0;
  for (let i = WEEK_INDEX; i < WEEK_INDEX + DAYS_PER_WEEK; i++) {
    dayCount += birdsPerDay[i];
  }
  return dayCount;
}

/**
 * Fixes the counting mistake by increasing the bird count
 * by one for every second day.
 *
 * @param {number[]} birdsPerDay
 * @returns {void} should not return anything
 */
export function fixBirdCountLog(birdsPerDay) {
  for (let i = 0; i < birdsPerDay.length; i++) {
    if (i % 2 === 0) {
      birdsPerDay[i] += 1;
    }
  }
  return birdsPerDay;
}
