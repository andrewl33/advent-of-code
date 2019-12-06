// Process file
let input = Node.Fs.readFileAsUtf8Sync("./src/day05input.txt");
let arr =
  Array.map(a => Pervasives.int_of_string(a), Js.String.split(",", input)); // windows specific

let computer = arr => {
  // instructions, takes the value
  let one = (a, b, c) => arr[c] = arr[a] + arr[b];
  let two = (a, b, c) => arr[c] = arr[a] * arr[b];
  let three = (instructionPtr, callback) => {
    Js.log("Input number: ");
    Readline.readline(input => {
      arr[instructionPtr] = Pervasives.int_of_string(input);
      Readline.close();
      callback();
    });
  };
  let four = instructionPtr =>
    Js.log(
      "diagnostic code: " ++ Pervasives.string_of_int(arr[instructionPtr]),
    );
  let five = (ip, a, b, r) =>
    arr[a] != 0 && ip != arr[b] ? r(arr[b]) : r(ip + 3);

  let six = (ip, a, b, r) =>
    arr[a] == 0 && ip != arr[b] ? r(arr[b]) : r(ip + 3);

  let seven = (a, b, c) => arr[c] = arr[a] < arr[b] ? 1 : 0;
  let eight = (a, b, c) => arr[c] = arr[a] == arr[b] ? 1 : 0;
  let error = () => {
    Js.log("error");
  };

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

  let rec runner = instructionPtr => {
    let parsed = parseOpcode(arr[instructionPtr]);
    let indexes = setIndex(List.tl(parsed), instructionPtr);

    switch (List.hd(parsed)) {
    | 1 =>
      let [a, b, c] = indexes;
      one(a, b, c);
      runner(instructionPtr + 4);
    | 2 =>
      let [a, b, c] = indexes;
      two(a, b, c);
      runner(instructionPtr + 4);
    | 3 => three(List.hd(indexes), () => runner(instructionPtr + 2))
    | 4 =>
      four(List.hd(indexes));
      runner(instructionPtr + 2);
    | 5 =>
      let [a, b] = indexes;
      five(instructionPtr, a, b, runner);
    | 6 =>
      let [a, b] = indexes;
      six(instructionPtr, a, b, runner);
    | 7 =>
      let [a, b, c] = indexes;
      seven(a, b, c);
      runner(instructionPtr + 4);
    | 8 =>
      let [a, b, c] = indexes;
      eight(a, b, c);
      runner(instructionPtr + 4);
    | 99 => Js.log("Halted")
    | _ => Js.log("Error")
    };
  };

  runner(0);
};

computer(arr);
