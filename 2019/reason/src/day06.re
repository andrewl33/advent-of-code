// Process file
let input = Node.Fs.readFileAsUtf8Sync("./src/day06input.txt");
// let input = Node.Fs.readFileAsUtf8Sync("./src/day06test.txt");
let arr =
  ArrayLabels.to_list(
    Array.map(
      a => ArrayLabels.to_list(Js.String.split(")", a)),
      Js.String.split("\r\n", input),
    ),
  ); // windows specific

module AdjSet =
  Map.Make({
    type t = Js.String.t;
    let compare = Pervasives.compare;
  });

module AdjSetValues =
  Set.Make({
    type t = Js.String.t;
    let compare = Pervasives.compare;
  });

// Type casting is broken
let rec fillAdjSet = (adjSet, arr: list(list(Js.String.t))) => {
  let put = pair => {
    // lol yikes
    let k = List.hd(pair);
    let v = List.nth(pair, 1);

    if (AdjSet.exists((key, _) => k == key, adjSet)) {
      AdjSet.add(
        k,
        AdjSetValues.(AdjSet.find(k, adjSet) |> add(v)),
        adjSet,
      );
    } else {
      AdjSet.add(k, AdjSetValues.(empty |> add(v)), adjSet);
    };
  };

  switch (arr) {
  | [] => adjSet
  | [a] => put(a)
  | [a, ...b] => fillAdjSet(put(a), b)
  };
};

// Get adj set working
let adjSet = fillAdjSet(AdjSet.empty, arr);

// AdjSet printout
// AdjSet.iter(
//   (k, v) => {
//     Js.log(k);
//     Js.log(AdjSetValues.elements(v));
//   },
//   adjSet,
// );

let orbitCount = adjSet => {
  // DFS, visited is just counted once
  // Cannot handle cyclical
  let rec aux = (head, counter) =>
    if (!AdjSet.exists((key, _) => head == key, adjSet)) {
      counter;
    } else {
      let searchSet = AdjSet.(adjSet |> find(head));
      List.fold_left(
        (acc, el) => acc + el,
        0,
        List.map(
          i => aux(i, counter + 1),
          AdjSetValues.(searchSet |> elements),
        ),
      )
      + counter;
    };

  aux("COM", 0);
};

Js.log("Part 1: " ++ Pervasives.string_of_int(orbitCount(adjSet)));

// Modify AdjSet to have bidirectional edgelist
// Type casting is broken
let rec fillAdjSetBiDir = (adjSet, arr: list(list(Js.String.t))) => {
  let put = pair => {
    let k = List.hd(pair);
    let v = List.nth(pair, 1);

    let fill = (k, v, adjSet) =>
      if (AdjSet.exists((key, _) => k == key, adjSet)) {
        AdjSet.add(
          k,
          AdjSetValues.(AdjSet.find(k, adjSet) |> add(v)),
          adjSet,
        );
      } else {
        AdjSet.add(k, AdjSetValues.(empty |> add(v)), adjSet);
      };

    fill(k, v, fill(v, k, adjSet));
  };

  switch (arr) {
  | [] => adjSet
  | [a] => put(a)
  | [a, ...b] => fillAdjSetBiDir(put(a), b)
  };
};

let adjSet = fillAdjSetBiDir(AdjSet.empty, arr);

let orbitalTransfers = adjSet => {
  // Traverse from YOU to SAN, edgeCount - 2

  // NOT PURE
  let q = Queue.create();
  let s = AdjSetValues.empty;
  let rec countTransfers = (cur, count, set) => {
    let rec fillQueue = (arr, s) =>
      switch (arr) {
      | [] => s
      | [a] when !AdjSetValues.exists(t => t == a, s) =>
        Queue.add((a, count), q);
        AdjSetValues.add(a, s);
      | [a, ...b] when !AdjSetValues.exists(t => t == a, s) =>
        Queue.add((a, count), q);
        fillQueue(b, AdjSetValues.add(a, s));
      | [a, ...b] when AdjSetValues.exists(t => t == a, s) =>
        fillQueue(b, AdjSetValues.add(a, s))
      | _ => s
      };

    if (cur == "SAN") {
      count;
    } else {
      let newSet =
        fillQueue(AdjSetValues.elements(AdjSet.(adjSet |> find(cur))), set);
      if (!Queue.is_empty(q)) {
        let (cur, count) = Queue.pop(q);
        countTransfers(cur, count + 1, newSet);
      } else {
        (-1);
      };
    };
  };

  countTransfers("YOU", 0, AdjSetValues.empty);
};

Js.log(
  "Part 2: " ++ Pervasives.string_of_int(orbitalTransfers(adjSet) - 2),
);
