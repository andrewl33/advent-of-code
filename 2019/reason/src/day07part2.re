// Process file
let input = Node.Fs.readFileAsUtf8Sync("./src/day07input.txt");
// let input = Node.Fs.readFileAsUtf8Sync("./src/day07test.txt");
let inputArr =
  Array.map(a => Pervasives.int_of_string(a), Js.String.split(",", input)); // windows specific

type computerState = {
  arr: array(int),
  ip: int,
};

let cs = [|
  {arr: Array.copy(inputArr), ip: 0},
  {arr: Array.copy(inputArr), ip: 0},
  {arr: Array.copy(inputArr), ip: 0},
  {arr: Array.copy(inputArr), ip: 0},
  {arr: Array.copy(inputArr), ip: 0},
|];

let computer = (state, phase, ip, input) => {
  let arr = Array.copy(cs[state].arr);
  let phase = ip == 0 ? phase : input;
  // instructions, takes the value
  let one = (a, b, c) => arr[c] = arr[a] + arr[b];
  let two = (a, b, c) => arr[c] = arr[a] * arr[b];
  let three = (instructionPtr, p, callback) => {
    arr[instructionPtr] = p;
    callback();
  };
  let four = instructionPtr => arr[instructionPtr];
  let five = (ip, a, b, r) =>
    arr[a] != 0 && ip != arr[b] ? r(arr[b]) : r(ip + 3);

  let six = (ip, a, b, r) =>
    arr[a] == 0 && ip != arr[b] ? r(arr[b]) : r(ip + 3);

  let seven = (a, b, c) => arr[c] = arr[a] < arr[b] ? 1 : 0;
  let eight = (a, b, c) => arr[c] = arr[a] == arr[b] ? 1 : 0;

  // parse opcode
  // returns a list format opcode, mode, mode, etc
  let parseOpcode = opcode => {
    // aux finishes off the mode values
    let rec aux = (modes, parsed, counter) =>
      switch (counter) {
      | 0 => parsed
      | _ => aux(modes / 10, [modes mod 10] @ parsed, counter - 1)
      };

    // handle opcode values 0-99 first
    let oc = opcode mod 100;

    let paramSize =
      switch (oc) {
      | 1
      | 2
      | 7
      | 8 => 3
      | 3
      | 4 => 1
      | 5
      | 6 => 2
      | 99 => 0
      | _ => 0
      };

    List.rev(aux(opcode / 100, [opcode mod 100], paramSize));
  };

  // setIndex returns an array with
  // [opcode, arrayValues...]
  // as if everything is in parameter mode 1
  // recieves the modes and performs lookups
  let setIndex = (opcodeArr, instructionPtr) => {
    let rec aux = (opcodeArr, acc, counter) => {
      let setIdx = mode => {
        switch (mode) {
        | 0 => arr[instructionPtr + counter]
        | 1 => instructionPtr + counter
        | _ => (-10000000)
        };
      };

      switch (opcodeArr) {
      | [] => acc
      | [a] => aux([], [setIdx(a)] @ acc, counter + 1)
      | [a, ...b] => aux(b, [setIdx(a)] @ acc, counter + 1)
      };
    };

    List.rev(aux(opcodeArr, [], 1));
  };
  let rec runner = (output, i, instructionPtr) => {
    let parsed = parseOpcode(arr[instructionPtr]);
    let indexes = setIndex(List.tl(parsed), instructionPtr);

    switch (List.hd(parsed)) {
    | 1 =>
      let [a, b, c] = indexes;
      one(a, b, c);
      runner(output, i, instructionPtr + 4);
    | 2 =>
      let [a, b, c] = indexes;
      two(a, b, c);
      runner(output, i, instructionPtr + 4);
    | 3 =>
      three(List.hd(indexes), i, () =>
        runner(output, input, instructionPtr + 2)
      )
    | 4 =>
      cs[state] = {arr, ip: instructionPtr + 2};
      four(List.hd(indexes));
    | 5 =>
      let [a, b] = indexes;
      five(instructionPtr, a, b, runner(output, i));
    | 6 =>
      let [a, b] = indexes;
      six(instructionPtr, a, b, runner(output, i));
    | 7 =>
      let [a, b, c] = indexes;
      seven(a, b, c);
      runner(output, i, instructionPtr + 4);
    | 8 =>
      let [a, b, c] = indexes;
      eight(a, b, c);
      runner(output, i, instructionPtr + 4);
    | 99 => Pervasives.min_int
    | _ => output
    };
  };

  runner(0, phase, ip);
};

let rec generatePermutations = values => {
  let ins_all_positions = (x, l) => {
    let rec aux = (prev, acc) =>
      fun
      | [] => [prev @ [x], ...acc] |> List.rev
      | [hd, ...tl] as l =>
        aux(prev @ [hd], [prev @ [x] @ l, ...acc], tl);

    aux([], [], l);
  };
  switch (values) {
  | [] => []
  | [a] => [[a]]
  | [a, ...b] =>
    List.fold_left(
      (acc, p) => acc @ ins_all_positions(a, p),
      [],
      generatePermutations(b),
    )
  };
};

let perm = generatePermutations([5, 6, 7, 8, 9]);

let rec partTwo = (arr, maxVal) => {
  let processPerm = arr => {
    let arr = ArrayLabels.of_list(arr);
    cs[0] = {arr: Array.copy(inputArr), ip: 0};
    cs[1] = {arr: Array.copy(inputArr), ip: 0};
    cs[2] = {arr: Array.copy(inputArr), ip: 0};
    cs[3] = {arr: Array.copy(inputArr), ip: 0};
    cs[4] = {arr: Array.copy(inputArr), ip: 0};
    let state = ref(0);
    let curVal = ref(0);
    let value = ref(computer(state^, arr[0], cs[state^].ip, 0));
    while (value^ != Pervasives.min_int) {
      curVal := state^ == 4 ? value^ : curVal^;
      state := state^ == 4 ? 0 : state^ + 1;
      value := computer(state^, arr[state^], cs[state^].ip, value^);
    };

    curVal^;
  };

  switch (arr) {
  | [] => maxVal
  | [a] => partTwo([], processPerm(a) > maxVal ? processPerm(a) : maxVal)
  | [a, ...b] =>
    partTwo(b, processPerm(a) > maxVal ? processPerm(a) : maxVal)
  };
};

Js.log(partTwo(perm, 0));
