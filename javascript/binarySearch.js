/* 
DESCRIPTION
With binary search, you guess in the middle and eliminate half the remaining options every iteration.
Binary search only works when the array that is passed is sorted.

binary_search takes a sorted array and the item we are looking for as parameters.
In this case, we are looking for a number.

BIG O NOTATION
Logarithmic: O(log N)
*/

const binarySearch = (arr, num) => {
  // sort the list in case it is not already sorted
  arr = arr.sort((a, b) => a - b);
  let high = arr.length - 1;
  let low = 0;

  while (high >= low) {
    // take the ceiling value of mid in case the arr length is even.
    let mid = Math.ceil((high + low) / 2);
    let guess = arr[mid];

    // if the guess is correct, return the index
    if (guess === num) {
      return mid;
    }
    // if the guess is too high, adjust the ceiling
    if (guess > num) {
      high = mid - 1;
      // if the guess is too low
    } else {
      low = mid + 1;
    }
  }

  // if we exit the loop without returning the index, return null
  return null;
};

// TEST CASES
const arrayOne = [1, 3, 5, 7, 9];
const numOne = 3;
// => 1
const arrayTwo = [9, 921, 5, 102, 23, 99, 4, 1, 13];
const numTwo = 23;

console.log(binarySearch(arrayOne, numOne));
