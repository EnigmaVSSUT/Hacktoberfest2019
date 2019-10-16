// Pass this function an array...
// ...you'll get back an object containing a count of each element.
// Useful if you have a really long list and need to find the duplicates!

// From the root of this repo type `node JavaScript/countArrayInstances.js` to see the results

function countArrayElements(array) {
  result = {};
  array.forEach(element => {
    if (result[element]) {
      result[element] += 1;
    } else {
      result[element] = 1;
    }
  });
  return result;
}

const names = [
  "Bill",
  "Michael",
  "Trevor",
  "Bill",
  "Marsha",
  "Horace",
  "Teresa",
  "Bill",
  "Horace",
  "Louise",
  "Bill",
  "Teresa",
  "Horace"
];

const shoppingList = [
  "Milk",
  "Croissant",
  "Croissant",
  "Apple",
  "Apple",
  "Apple",
  "Apple",
  "Apple",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Egg",
  "Juice",
  "Cereal"
];

console.log(countArrayElements(names));
console.log(countArrayElements(shoppingList));
