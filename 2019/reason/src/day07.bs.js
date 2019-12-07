// Generated by BUCKLESCRIPT, PLEASE EDIT WITH CARE
'use strict';

var Fs = require("fs");
var List = require("bs-platform/lib/js/list.js");
var $$Array = require("bs-platform/lib/js/array.js");
var Curry = require("bs-platform/lib/js/curry.js");
var Caml_array = require("bs-platform/lib/js/caml_array.js");
var Caml_int32 = require("bs-platform/lib/js/caml_int32.js");
var Pervasives = require("bs-platform/lib/js/pervasives.js");
var Caml_format = require("bs-platform/lib/js/caml_format.js");
var Caml_builtin_exceptions = require("bs-platform/lib/js/caml_builtin_exceptions.js");

var input = Fs.readFileSync("./src/day07input.txt", "utf8");

var inputArr = $$Array.map(Caml_format.caml_int_of_string, input.split(","));

function computer(arr, phase, input) {
  var arr$1 = $$Array.copy(arr);
  var one = function (a, b, c) {
    return Caml_array.caml_array_set(arr$1, c, Caml_array.caml_array_get(arr$1, a) + Caml_array.caml_array_get(arr$1, b) | 0);
  };
  var two = function (a, b, c) {
    return Caml_array.caml_array_set(arr$1, c, Caml_int32.imul(Caml_array.caml_array_get(arr$1, a), Caml_array.caml_array_get(arr$1, b)));
  };
  var seven = function (a, b, c) {
    var match = Caml_array.caml_array_get(arr$1, a) < Caml_array.caml_array_get(arr$1, b);
    return Caml_array.caml_array_set(arr$1, c, match ? 1 : 0);
  };
  var eight = function (a, b, c) {
    var match = Caml_array.caml_array_get(arr$1, a) === Caml_array.caml_array_get(arr$1, b);
    return Caml_array.caml_array_set(arr$1, c, match ? 1 : 0);
  };
  var parseOpcode = function (opcode) {
    var aux = function (_modes, _parsed, _counter) {
      while(true) {
        var counter = _counter;
        var parsed = _parsed;
        var modes = _modes;
        if (counter !== 0) {
          _counter = counter - 1 | 0;
          _parsed = Pervasives.$at(/* :: */[
                modes % 10,
                /* [] */0
              ], parsed);
          _modes = modes / 10 | 0;
          continue ;
        } else {
          return parsed;
        }
      };
    };
    var oc = opcode % 100;
    var paramSize;
    if (oc >= 9 || oc <= 0) {
      paramSize = 0;
    } else {
      switch (oc - 1 | 0) {
        case 2 :
        case 3 :
            paramSize = 1;
            break;
        case 4 :
        case 5 :
            paramSize = 2;
            break;
        case 0 :
        case 1 :
        case 6 :
        case 7 :
            paramSize = 3;
            break;
        
      }
    }
    return List.rev(aux(opcode / 100 | 0, /* :: */[
                    opcode % 100,
                    /* [] */0
                  ], paramSize));
  };
  var setIndex = function (opcodeArr, instructionPtr) {
    var aux = function (_opcodeArr, _acc, _counter) {
      while(true) {
        var counter = _counter;
        var acc = _acc;
        var opcodeArr = _opcodeArr;
        var setIdx = (function(counter){
        return function setIdx(mode) {
          if (mode !== 0) {
            if (mode !== 1) {
              return -10000000;
            } else {
              return instructionPtr + counter | 0;
            }
          } else {
            return Caml_array.caml_array_get(arr$1, instructionPtr + counter | 0);
          }
        }
        }(counter));
        if (opcodeArr) {
          var b = opcodeArr[1];
          var a = opcodeArr[0];
          _counter = counter + 1 | 0;
          _acc = Pervasives.$at(/* :: */[
                setIdx(a),
                /* [] */0
              ], acc);
          if (b) {
            _opcodeArr = b;
            continue ;
          } else {
            _opcodeArr = /* [] */0;
            continue ;
          }
        } else {
          return acc;
        }
      };
    };
    return List.rev(aux(opcodeArr, /* [] */0, 1));
  };
  var runner = function (_output, _i, _instructionPtr) {
    while(true) {
      var instructionPtr = _instructionPtr;
      var i = _i;
      var output = _output;
      var parsed = parseOpcode(Caml_array.caml_array_get(arr$1, instructionPtr));
      var indexes = setIndex(List.tl(parsed), instructionPtr);
      var match = List.hd(parsed);
      if (match >= 9 || match <= 0) {
        return output;
      } else {
        switch (match - 1 | 0) {
          case 0 :
              if (indexes) {
                var match$1 = indexes[1];
                if (match$1) {
                  var match$2 = match$1[1];
                  if (match$2 && !match$2[1]) {
                    one(indexes[0], match$1[0], match$2[0]);
                    _instructionPtr = instructionPtr + 4 | 0;
                    continue ;
                  }
                  
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      85,
                      10
                    ]
                  ];
          case 1 :
              if (indexes) {
                var match$3 = indexes[1];
                if (match$3) {
                  var match$4 = match$3[1];
                  if (match$4 && !match$4[1]) {
                    two(indexes[0], match$3[0], match$4[0]);
                    _instructionPtr = instructionPtr + 4 | 0;
                    continue ;
                  }
                  
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      89,
                      10
                    ]
                  ];
          case 2 :
              var instructionPtr$1 = List.hd(indexes);
              var p = i;
              var callback = (function(output,instructionPtr){
              return function callback(param) {
                return runner(output, input, instructionPtr + 2 | 0);
              }
              }(output,instructionPtr));
              Caml_array.caml_array_set(arr$1, instructionPtr$1, p);
              return Curry._1(callback, /* () */0);
          case 3 :
              _instructionPtr = instructionPtr + 2 | 0;
              _i = input;
              _output = Caml_array.caml_array_get(arr$1, List.hd(indexes));
              continue ;
          case 4 :
              if (indexes) {
                var match$5 = indexes[1];
                if (match$5 && !match$5[1]) {
                  var ip = instructionPtr;
                  var a = indexes[0];
                  var b = match$5[0];
                  var r = (function(output,i){
                  return function r(param) {
                    return runner(output, i, param);
                  }
                  }(output,i));
                  var match$6 = Caml_array.caml_array_get(arr$1, a) !== 0 && ip !== Caml_array.caml_array_get(arr$1, b);
                  if (match$6) {
                    return Curry._1(r, Caml_array.caml_array_get(arr$1, b));
                  } else {
                    return Curry._1(r, ip + 3 | 0);
                  }
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      98,
                      10
                    ]
                  ];
          case 5 :
              if (indexes) {
                var match$7 = indexes[1];
                if (match$7 && !match$7[1]) {
                  var ip$1 = instructionPtr;
                  var a$1 = indexes[0];
                  var b$1 = match$7[0];
                  var r$1 = (function(output,i){
                  return function r$1(param) {
                    return runner(output, i, param);
                  }
                  }(output,i));
                  var match$8 = Caml_array.caml_array_get(arr$1, a$1) === 0 && ip$1 !== Caml_array.caml_array_get(arr$1, b$1);
                  if (match$8) {
                    return Curry._1(r$1, Caml_array.caml_array_get(arr$1, b$1));
                  } else {
                    return Curry._1(r$1, ip$1 + 3 | 0);
                  }
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      101,
                      10
                    ]
                  ];
          case 6 :
              if (indexes) {
                var match$9 = indexes[1];
                if (match$9) {
                  var match$10 = match$9[1];
                  if (match$10 && !match$10[1]) {
                    seven(indexes[0], match$9[0], match$10[0]);
                    _instructionPtr = instructionPtr + 4 | 0;
                    continue ;
                  }
                  
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      104,
                      10
                    ]
                  ];
          case 7 :
              if (indexes) {
                var match$11 = indexes[1];
                if (match$11) {
                  var match$12 = match$11[1];
                  if (match$12 && !match$12[1]) {
                    eight(indexes[0], match$11[0], match$12[0]);
                    _instructionPtr = instructionPtr + 4 | 0;
                    continue ;
                  }
                  
                }
                
              }
              throw [
                    Caml_builtin_exceptions.match_failure,
                    /* tuple */[
                      "day07.re",
                      108,
                      10
                    ]
                  ];
          
        }
      }
    };
  };
  return runner(0, phase, 0);
}

function generatePermutations(values) {
  var ins_all_positions = function (x, l) {
    var _prev = /* [] */0;
    var _acc = /* [] */0;
    var _l = l;
    while(true) {
      var l$1 = _l;
      var acc = _acc;
      var prev = _prev;
      if (l$1) {
        _l = l$1[1];
        _acc = /* :: */[
          Pervasives.$at(prev, Pervasives.$at(/* :: */[
                    x,
                    /* [] */0
                  ], l$1)),
          acc
        ];
        _prev = Pervasives.$at(prev, /* :: */[
              l$1[0],
              /* [] */0
            ]);
        continue ;
      } else {
        return List.rev(/* :: */[
                    Pervasives.$at(prev, /* :: */[
                          x,
                          /* [] */0
                        ]),
                    acc
                  ]);
      }
    };
  };
  if (values) {
    var b = values[1];
    var a = values[0];
    if (b) {
      return List.fold_left((function (acc, p) {
                    return Pervasives.$at(acc, ins_all_positions(a, p));
                  }), /* [] */0, generatePermutations(b));
    } else {
      return /* :: */[
              /* :: */[
                a,
                /* [] */0
              ],
              /* [] */0
            ];
    }
  } else {
    return /* [] */0;
  }
}

var perm = generatePermutations(/* :: */[
      0,
      /* :: */[
        1,
        /* :: */[
          2,
          /* :: */[
            3,
            /* :: */[
              4,
              /* [] */0
            ]
          ]
        ]
      ]
    ]);

function partOne(_arr, _maxVal) {
  while(true) {
    var maxVal = _maxVal;
    var arr = _arr;
    var processPerm = function (_arr, _v) {
      while(true) {
        var v = _v;
        var arr = _arr;
        if (arr) {
          var b = arr[1];
          var a = arr[0];
          _v = computer(inputArr, a, v);
          if (b) {
            _arr = b;
            continue ;
          } else {
            _arr = /* [] */0;
            continue ;
          }
        } else {
          return v;
        }
      };
    };
    if (arr) {
      var b = arr[1];
      var a = arr[0];
      if (b) {
        var match = processPerm(a, 0) > maxVal;
        _maxVal = match ? processPerm(a, 0) : maxVal;
        _arr = b;
        continue ;
      } else {
        var match$1 = processPerm(a, 0) > maxVal;
        _maxVal = match$1 ? processPerm(a, 0) : maxVal;
        _arr = /* [] */0;
        continue ;
      }
    } else {
      return maxVal;
    }
  };
}

console.log(partOne(perm, 0));

exports.input = input;
exports.inputArr = inputArr;
exports.computer = computer;
exports.generatePermutations = generatePermutations;
exports.perm = perm;
exports.partOne = partOne;
/* input Not a pure module */
