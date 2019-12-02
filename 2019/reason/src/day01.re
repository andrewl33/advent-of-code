let fuelReads = Node.Fs.readFileAsUtf8Sync("./src/day01input.txt");

let requiredFuel = mass => mass / 3 - 2;

let rec recursiveFuel = mass => acc => {
    let v = requiredFuel(mass);
    v > 0 ? recursiveFuel(v)(v+acc) : acc;
}

let arr = Js.String.split("\r\n", fuelReads);

let rec readlinePart1 = arr => acc =>
    switch (arr) {
        | [] => acc
        | [a, ...b] => readlinePart1(b)(acc + requiredFuel(Pervasives.int_of_string(a)))
    };

    let rec readlinePart2 = arr => acc =>
    switch (arr) {
        | [] => acc
        | [a, ...b] => readlinePart2(b)(acc + recursiveFuel(Pervasives.int_of_string(a))(0))
    };


Js.log("Part 1: " ++ Pervasives.string_of_int(readlinePart1(ArrayLabels.to_list(arr))(0)));
Js.log("Part 2: " ++ Pervasives.string_of_int(readlinePart2(ArrayLabels.to_list(arr))(0)));