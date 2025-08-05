/// <reference path="./global.d.ts" />
//
// @ts-check

/**
 * Determine the price of the pizza given the pizza and optional extras
 *
 * @param {Pizza} pizza name of the pizza to be made
 * @param {Extra[]} extras list of extras
 *
 * @returns {number} the price of the pizza
 */
export function pizzaPrice(pizza, ...extras) {
  // Base pizza prices
  const basePrices = {
    'Margherita': 7,
    'Caprese': 9,
    'Formaggio': 10
  };

  // Base case - no extras
  if (extras.length === 0) {
    return basePrices[pizza];
  }

  // Extra prices
  const extraPrices = {
    'ExtraSauce': 1,
    'ExtraToppings': 2
  };

  // Recursive case:
  // Take first extra and recursively process the rest
  const [firstExtra, ...remainingExtras] = extras;
  return extraPrices[firstExtra] + pizzaPrice(pizza, ...remainingExtras);
}


/**
 * Calculate the price of the total order, given individual orders
 *
 * (HINT: For this exercise, you can take a look at the supplied "global.d.ts" file
 * for a more info about the type definitions used)
 *
 * @param {PizzaOrder[]} pizzaOrders a list of pizza orders
 * @returns {number} the price of the total order
 */
export function orderPrice(pizzaOrders) {
  let totalPrice = 0;

  for (const order of pizzaOrders) {
    const { pizza, extras } = order;
    totalPrice += pizzaPrice(pizza, ...extras);
  }

  return totalPrice;
}
