// let wires = Node.Fs.readFileAsUtf8Sync("./src/day03input.txt");
 // let manhattanDistance = x => y => a => b => Pervasives.abs(x-a) + Pervasives.abs(y-b);
 // let mdCenter = manhattanDistance(0)(0);
 // let parse = w => {
 //     let rec changeDataType = (a, acc) => {
 //         let aux = v => (
 //             Js.String.slice(~from=0, ~to_=1, v),
 //             Pervasives.int_of_string(Js.String.sliceToEnd(~from=1, v))
 //             );
 //         switch a {
 //             | [] => []
 //             | [a] => [aux(a)]@acc
 //             | [a, ...b] => changeDataType(b, [aux(a)]@acc)
 //         }
 //     }
 //     let rec splitArr = (a, acc) => {
 //         switch a {
 //             | [] => []
 //             | [a] => changeDataType(ArrayLabels.to_list(Js.String.split(",", a)), [])@acc
 //             | [a, ...b] => splitArr(b, changeDataType(ArrayLabels.to_list(Js.String.split(",", a)), [])@acc)
 //         }
 //     }
 //     splitArr(w, []);
 // }
 // let wireArrs = parse(ArrayLabels.to_list(Js.String.split("\n", wires)));
 // let solver = w => {
 //     let setDirection = a => {
 //         switch a {
 //             | "R" => (1,0)
 //             | "L" => (-1, 0)
 //             | "U" => (0, -1)
 //             | "D" => (0, 1)
 //             | _ => (100, 100)
 //         }
 //     }
 //     let h = Hashtbl.create(300);
 //     let results = Hashtbl.create(300);
 //     switch w {
 //         | [] => []
 //         | [a] => []
 //     }
 //     results;
 /* */
