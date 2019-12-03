const fs = require("fs");
const readline = require("readline");

const manhattanDistance = (x, y, a, b) => Math.abs(x - a) + Math.abs(y - b);

const rl = readline.createInterface({
  input: fs.createReadStream("./2019/day-03/input.txt")
});

// Part 1
const a = new Set();
const res = new Set();

// Part 2
const b = {};
const resPartTwo = {};

let filledFirst = false;
let curPtx = 0;
let curPty = 0;

rl.on("line", l => {
  const list = l.split(",");
  let stepCount = 1;
  for (let i = 0; i < list.length; i++) {
    const c = list[i].slice(0, 1);
    const num = parseInt(list[i].slice(1));

    let x = 0;
    let y = 0;

    switch (c) {
      case "R":
        x = 1;
        break;
      case "L":
        x = -1;
        break;
      case "U":
        y = -1;
        break;
      case "D":
        y = 1;
        break;
    }

    for (let j = 0; j < num; j++) {
      curPtx += x;
      curPty += y;
      if (!filledFirst) {
        if (!a.has(`${curPtx}_${curPty}`)) {
          a.add(`${curPtx}_${curPty}`);
          b[`${curPtx}_${curPty}`] = stepCount;
        }
      } else {
        if (a.has(`${curPtx}_${curPty}`) && !res.has(`${curPtx}_${curPty}`)) {
          res.add(`${curPtx}_${curPty}`);
          resPartTwo[`${curPtx}_${curPty}`] =
            stepCount + b[`${curPtx}_${curPty}`];
        }
      }
      stepCount++;
    }
  }

  filledFirst = true;

  curPtx = 0;
  curPty = 0;
});

rl.on("close", () => {
  let minDistance = Number.MAX_SAFE_INTEGER;
  for (let i of res) {
    const [x, y] = i.split("_");
    const val = manhattanDistance(0, 0, parseInt(x), parseInt(y));
    if (val < minDistance) {
      minDistance = val;
    }
  }

  const s = [];

  for (let r in resPartTwo) {
    s.push([r, resPartTwo[r]]);
  }

  s.sort((a, b) => {
    return a[1] - b[1];
  });

  const [j, k] = s[0][0].split("_");

  console.log(s);

  console.log("Part 1: " + minDistance);
  console.log("Part 2: " + manhattanDistance(0, 0, parseInt(j), parseInt(k)));
});
