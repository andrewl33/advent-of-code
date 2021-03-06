// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Fs = require("fs");
var ArrayLabels = require("bs-platform/lib/js/arrayLabels.js");
var Caml_format = require("bs-platform/lib/js/caml_format.js");

var fuelReads = Fs.readFileSync("./src/day01input.txt", "utf8");

function requiredFuel(mass) {
  return (mass / 3 | 0) - 2 | 0;
}

function recursiveFuel(_mass, _acc) {
  while(true) {
    var acc = _acc;
    var mass = _mass;
    var v = requiredFuel(mass);
    var match = v > 0;
    if (match) {
      _acc = v + acc | 0;
      _mass = v;
      continue ;
    } else {
      return acc;
    }
  };
}

var arr = fuelReads.split("\r\n");

function readlinePart1(_arr, _acc) {
  while(true) {
    var acc = _acc;
    var arr = _arr;
    if (arr) {
      _acc = acc + requiredFuel(Caml_format.caml_int_of_string(arr[0])) | 0;
      _arr = arr[1];
      continue ;
    } else {
      return acc;
    }
  };
}

function readlinePart2(_arr, _acc) {
  while(true) {
    var acc = _acc;
    var arr = _arr;
    if (arr) {
      _acc = acc + recursiveFuel(Caml_format.caml_int_of_string(arr[0]), 0) | 0;
      _arr = arr[1];
      continue ;
    } else {
      return acc;
    }
  };
}

console.log("Part 1: " + String(readlinePart1(ArrayLabels.to_list(arr), 0)));

console.log("Part 2: " + String(readlinePart2(ArrayLabels.to_list(arr), 0)));

exports.fuelReads = fuelReads;
exports.requiredFuel = requiredFuel;
exports.recursiveFuel = recursiveFuel;
exports.arr = arr;
exports.readlinePart1 = readlinePart1;
exports.readlinePart2 = readlinePart2;
/* fuelReads Not a pure module */
