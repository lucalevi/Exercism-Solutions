/// <reference path="./global.d.ts" />
// @ts-check

/**
 * Implement the functions needed to solve the exercise here.
 * Do not forget to export them so they are available for the
 * tests. Here an example of the syntax as reminder:
 *
 * export function yourFunction(...) {
 *   ...
 * }
 */


/**
 * Determines the cooking status of a lasagna based on the remaining time.
 *
 * @param {number} remainingTime - The time remaining for cooking in minutes.
 * @returns {string} The cooking status message.
 */
export function cookingStatus(remainingTime) {
    if (remainingTime === 0) {
        return 'Lasagna is done.';
    }
    if (remainingTime > 0) {
        return 'Not done, please wait.';
    }
    return 'You forgot to set the timer.';
}


/**
 * Calculates the total preparation time for a lasagna based on the number of layers.
 *
 * @param {Array<string>} layersArray - An array representing the layers of the lasagna.
 * @param {number} [timePerLayer=2] - The time in minutes it takes to prepare each layer. Defaults to 2 minutes.
 * @returns {number} The total preparation time in minutes.
 */
export function preparationTime(layersArray, timePerLayer = 2) {
    return layersArray.length * timePerLayer;
}


/**
 * Calculates the quantities of noodles and sauce needed for a lasagna based on its layers.
 *
 * @param {Array<string>} layersArray - An array representing the layers of the lasagna (e.g., ['noodles', 'sauce', 'noodles']).
 * @returns {object} An object containing the total quantities of 'noodles' (in grams) and 'sauce' (in liters) needed.
 * @property {number} noodles - The total amount of noodles needed in grams.
 * @property {number} sauce - The total amount of sauce needed in liters.
 */
export function quantities(layersArray) {
    let neededIngredients = { noodles: 0, sauce: 0 };

    for (const layer of layersArray) {
        if (layer === 'noodles') {
            neededIngredients.noodles += 50;
        } else if (layer === 'sauce') {
            neededIngredients.sauce += 0.2;
        }
    }
    return neededIngredients;
}


/**
 * Adds the last element from a friend's list to your list as a "secret ingredient".
 * This function modifies `myList` in place.
 *
 * @param {Array<any>} friendsList - The array representing your friend's list.
 * @param {Array<any>} myList - The array representing your list, which will be modified.
 * @returns {void} This function does not return a value (it modifies `myList` directly).
 */
export function addSecretIngredient(friendsList, myList) {
    myList.push(friendsList[friendsList.length - 1]);
}


/**
 * Scales a lasagna recipe to a desired number of portions.
 * This function assumes the original recipe is for 2 portions.
 *
 * @param {object} recipe - The original recipe object containing ingredient quantities.
 * @param {number} portionsNumber - The desired number of portions for the scaled recipe.
 * @returns {object} A new object containing the scaled quantities of ingredients.
 */
export function scaleRecipe(recipe, portionsNumber) {
    const scaleFactor = portionsNumber / 2;
    const scaledRecipe = {};

    for (const ingredient in recipe) {
        scaledRecipe[ingredient] = recipe[ingredient] * scaleFactor;
    }

    return scaledRecipe;
}