// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Fs = require("fs");
var Hashtbl = require("bs-platform/lib/js/hashtbl.js");
var Pervasives = require("bs-platform/lib/js/pervasives.js");
var ArrayLabels = require("bs-platform/lib/js/arrayLabels.js");
var Caml_format = require("bs-platform/lib/js/caml_format.js");
var Caml_builtin_exceptions = require("bs-platform/lib/js/caml_builtin_exceptions.js");

var wires = Fs.readFileSync("./src/day03input.txt", "utf8");

function manhattanDistance(x, y, a, b) {
  return Pervasives.abs(x - a | 0) + Pervasives.abs(y - b | 0) | 0;
}

function mdCenter(param, param$1) {
  return manhattanDistance(0, 0, param, param$1);
}

function parse(w) {
  var changeDataType = function (_a, _acc) {
    while(true) {
      var acc = _acc;
      var a = _a;
      var aux = function (v) {
        return /* tuple */[
                v.slice(0, 1),
                Caml_format.caml_int_of_string(v.slice(1))
              ];
      };
      if (a) {
        var b = a[1];
        var a$1 = a[0];
        if (b) {
          _acc = Pervasives.$at(/* :: */[
                aux(a$1),
                /* [] */0
              ], acc);
          _a = b;
          continue ;
        } else {
          return Pervasives.$at(/* :: */[
                      aux(a$1),
                      /* [] */0
                    ], acc);
        }
      } else {
        return /* [] */0;
      }
    };
  };
  var _a = w;
  var _acc = /* [] */0;
  while(true) {
    var acc = _acc;
    var a = _a;
    if (a) {
      var b = a[1];
      var a$1 = a[0];
      if (b) {
        _acc = Pervasives.$at(changeDataType(ArrayLabels.to_list(a$1.split(",")), /* [] */0), acc);
        _a = b;
        continue ;
      } else {
        return Pervasives.$at(changeDataType(ArrayLabels.to_list(a$1.split(",")), /* [] */0), acc);
      }
    } else {
      return /* [] */0;
    }
  };
}

var wireArrs = parse(ArrayLabels.to_list(wires.split("\n")));

function solver(w) {
  Hashtbl.create(undefined, 300);
  var results = Hashtbl.create(undefined, 300);
  if (w && w[1]) {
    throw [
          Caml_builtin_exceptions.match_failure,
          /* tuple */[
            "day03.re",
            48,
            4
          ]
        ];
  }
  return results;
}

exports.wires = wires;
exports.manhattanDistance = manhattanDistance;
exports.mdCenter = mdCenter;
exports.parse = parse;
exports.wireArrs = wireArrs;
exports.solver = solver;
/* wires Not a pure module */