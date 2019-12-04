/**
 * --- Day 4: Secure Container ---
You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?

Your puzzle input is 124075-580769.
 */

function validPart1(val) {
  const arr = val.toString().split("");
  const sorted = [...arr].sort();

  for (let i = 0; i < arr.length; ++i) {
    if (arr[i] != sorted[i]) {
      return false;
    }
  }

  for (let i = 0; i < arr.length - 1; ++i) {
    if (arr[i] == arr[i + 1]) {
      return true;
    }
  }
  return false;
}

let count = 0;
for (let i = 124075; i <= 580769; ++i) {
  if (validPart1(i)) {
    count++;
  }
}

console.log("Part 1: " + count);

function validPart2(val) {
  const arr = val.toString().split("");
  const sorted = [...arr].sort();

  for (let i = 0; i < arr.length; ++i) {
    if (arr[i] != sorted[i]) {
      return false;
    }
  }

  const d = {};

  for (let i = 0; i < arr.length - 1; ++i) {
    if (arr[i] == arr[i + 1]) {
      if (arr[i] in d) {
        d[arr[i]]++;
      } else {
        d[arr[i]] = 1;
      }
    }
  }

  return Object.keys(d).length > 0 && Object.values(d).sort()[0] == 1;
}

count = 0;
for (let i = 124075; i <= 580769; ++i) {
  if (validPart2(i)) {
    count++;
  }
}

console.log("Part 2: " + count);
