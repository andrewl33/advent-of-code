filename = "input.txt"

part1 = 0
part2 = 0


def part2rec(mass, acc):
    v = int(int(mass) // 3) - 2
    return part2rec(v, v + acc) if v > 0 else acc


with open(filename) as file:
    for line in file:
        part1 += int(int(line) // 3) - 2
        part2 += part2rec(line, 0)

print("Part 1: " + str(part1))
print("Part 2: " + str(part2))
