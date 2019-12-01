def count(file_name):
    with open(file_name) as file:
        i_a = []
        for line in file:
            for i in list(line):
                i_a.append(i)

        print(file_name, " Rooms: ", i_a.count("."),
              "Doors: ", i_a.count("|") + i_a.count("-"))


count("test1out.txt")
count("test2out.txt")
count("test3out.txt")
count("test4out.txt")

print(len(open("input.txt").read()))
