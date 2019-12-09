// Process file
let input = Node.Fs.readFileAsUtf8Sync("./src/day08input.txt");
// let input = Node.Fs.readFileAsUtf8Sync("./src/day08test.txt");

let strToIntList = s => {
  let rec aux = (count, acc) =>
    switch (count) {
    | (-1) => acc
    | 0 => [Pervasives.int_of_string(Js.String.get(s, count))] @ acc
    | _ =>
      aux(
        count - 1,
        [Pervasives.int_of_string(Js.String.get(s, count))] @ acc,
      )
    };

  aux(Js.String.length(s) - 1, []);
};

let fewestZeros = (width, height, data) => {
  let layerCount = width * height;
  let rec aux =
          (
            c,
            curZeros,
            minZeros,
            data,
            curOnes,
            curTwos,
            savedOnes,
            savedTwos,
          ) => {
    switch (c == layerCount - 1, data) {
    | (_, []) => savedOnes * savedTwos
    | (_, [a]) when a == 0 =>
      aux(
        0,
        0,
        curZeros + 1 < minZeros ? curZeros + 1 : minZeros,
        [],
        0,
        0,
        curZeros + 1 < minZeros ? curOnes : savedOnes,
        curZeros + 1 < minZeros ? curTwos : savedTwos,
      )
    | (_, [a]) when a != 0 =>
      aux(
        0,
        0,
        curZeros < minZeros ? curZeros : minZeros,
        [],
        0,
        0,
        curZeros < minZeros ? a == 1 ? curOnes + 1 : curOnes : savedOnes,
        curZeros < minZeros ? a == 2 ? curTwos + 1 : curTwos : savedTwos,
      )
    | (true, [a, ...b]) when a == 0 =>
      aux(
        0,
        0,
        curZeros + 1 < minZeros ? curZeros + 1 : minZeros,
        b,
        0,
        0,
        curZeros + 1 < minZeros ? curOnes : savedOnes,
        curZeros + 1 < minZeros ? curTwos : savedTwos,
      )
    | (true, [a, ...b]) when a != 0 =>
      aux(
        0,
        0,
        curZeros < minZeros ? curZeros : minZeros,
        b,
        0,
        0,
        curZeros < minZeros ? a == 1 ? curOnes + 1 : curOnes : savedOnes,
        curZeros < minZeros ? a == 2 ? curTwos + 1 : curTwos : savedTwos,
      )
    | (false, [a, ...b]) when a != 0 =>
      aux(
        c + 1,
        curZeros,
        minZeros,
        b,
        a == 1 ? curOnes + 1 : curOnes,
        a == 2 ? curTwos + 1 : curTwos,
        savedOnes,
        savedTwos,
      )
    | (false, [a, ...b]) when a == 0 =>
      aux(
        c + 1,
        curZeros + 1,
        minZeros,
        b,
        curOnes,
        curTwos,
        savedOnes,
        savedTwos,
      )
    | (_, [_, ..._]) => (-1)
    };
  };

  aux(0, 0, Pervasives.max_int, data, 0, 0, 0, 0);
};

let encoding = strToIntList(input);

Js.log(
  "Part 1: " ++ Pervasives.string_of_int(fewestZeros(25, 6, encoding)),
);

let renderImage = (encoding, width, height) => {
  // top down fill
  // while 2, continue
  // else, place it in the array, and go to next iteration
  // LMAO
  let arr = [|
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
    [|
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
      2,
    |],
  |];

  let rec aux = (encoding, w, h) => {
    switch (encoding) {
    | [] => arr
    | [a] =>
      arr[h][w] = arr[h][w] == 2 ? a : a == 2 ? arr[h][w] : a;
      aux(
        [],
        w - 1 < 0 ? width - 1 : w - 1,
        w - 1 < 0 ? h - 1 < 0 ? height - 1 : h - 1 : h,
      );
    | [a, ...b] =>
      arr[h][w] = arr[h][w] == 2 ? a : a == 2 ? arr[h][w] : a;
      aux(
        b,
        w - 1 < 0 ? width - 1 : w - 1,
        w - 1 < 0 ? h - 1 < 0 ? height - 1 : h - 1 : h,
      );
    };
  };

  aux(List.rev(encoding), width - 1, height - 1);
};

let rendered = renderImage(encoding, 25, 6);

Js.log("Part 2:");
for (x in 0 to 5) {
  Js.log(rendered[x]);
};
