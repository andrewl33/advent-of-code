'''
immune system: army with several groups
infection same

units in a group
same hp
same ad
same attack type
initiative (precedence for attacking and winning ties)
?weaknesses
?immunities

group
effective power = # units in a group * attack damage
-never have negative; only can be removed from combat

fight
2 phase: target selection, attacking

choose targets sorted by highest attack power
  this is chosen account weaknesses and immunities, not accounting for the defending group has enough units
  chooses highest attacking power of enemy in a tie
  chooses highest init if tie

  if no damage, don't attack

Groups then attack based on initiative

hp dealt
effective power is base
immune = no dmg
weak = double dmg

defending always loses whole units, overflow dmg but not kill is nullified

how many units does the remaining army have

SPLIT UP THE FUNCTIONS THIS TIME
'''
import copy

ID = 0
U_TYPE = 1
A_TYPE = 2
AD = 3
HP = 4
COUNT = 5
INIT = 6
IMMUNE = 7
WEAK = 8

IMMUNE_TYPE = 0
INFECTION_TYPE = 1


def input_parser(file_name):
    '''
    returns array of arrays
    sub array: [id, unit type, attack type, ad, health, unit numbers, initiative, set(immunities),  set(weaknesses), appended on id of enemy]
    '''
    groups = []
    person_type = 0
    id_count = 0

    for line in open(file_name).read().strip().split("\n"):
        if len(line.strip()) == 0:
            continue
        elif "Immune" in line:
            person_type = IMMUNE_TYPE
        elif "Infection" in line:
            person_type = INFECTION_TYPE
        else:
            line = line.split(" ")
            digits = [int(s) for s in line if s.isdigit()]
            # find weaknesses
            def_start_weak = -1
            def_start_immune = -1
            def_colon = -1
            def_end_parens = 0
            for i, s in enumerate(line):
                if s.find('weak') != -1:
                    def_start_weak = i
                elif s.find('immune') != -1:
                    def_start_immune = i
                elif s.find(')') != -1:
                    def_end_parens = i
                    break
            immune_set = set()
            weak_set = set()
            if def_start_immune != -1:

                def_end = def_end_parens

                if def_colon != -1 and def_start_immune < def_colon:
                    def_end = def_colon

                for i in range(def_start_immune, def_end+1):
                    for atk_type in ["fire", "radiation", "slashing", "cold", "bludgeoning"]:
                        if line[i].find(atk_type) != -1:
                            immune_set.add(atk_type)

            if def_start_weak != -1:
                def_end = def_end_parens

                if def_colon != -1 and def_start_weak < def_colon:
                    def_end = def_colon

                for i in range(def_start_weak, def_end+1):
                    for atk_type in ["fire", "radiation", "slashing", "cold", "bludgeoning"]:
                        if line[i].find(atk_type) != -1:
                            weak_set.add(atk_type)

            attack_type = ""
            for i in range(def_end_parens+1, len(line)):
                for atk_type in ["fire", "radiation", "slashing", "cold", "bludgeoning"]:
                    if line[i].find(atk_type) != -1:
                        attack_type = atk_type
                        break

            groups.append([id_count, person_type, attack_type,
                           digits[2], digits[1], digits[0], digits[3], immune_set, weak_set])
            id_count += 1
    return groups


def effective_power(group):
    if group[COUNT] < 1:
        return 0
    else:
        return group[COUNT] * group[AD]


def damage(attacker, defender):
    modifier = 1

    if attacker[A_TYPE] in defender[WEAK]:
        modifier = 2
    elif attacker[A_TYPE] in defender[IMMUNE]:
        modifier = 0

    return modifier * effective_power(attacker)


def deal_dmg(attacker, groups):

    if attacker[-1] == -1:
        return

    defender = []

    for g in groups:
        if g[ID] == attacker[-2]:
            defender = g
            break

    dmg = damage(attacker, defender)
    count = dmg // defender[HP]
    defender[COUNT] -= count


def find_enemy(attacker, groups, visited):

    defender_id = -1
    prospective_defenders = []

    for g in groups:
        if attacker == g or attacker[U_TYPE] == g[U_TYPE] or g[ID] in visited:
            continue
        else:
            dmg = damage(attacker, g)
            if dmg > 0:
                prospective_defenders.append((g, dmg))
    if prospective_defenders:
        # by max damage done
        if len(prospective_defenders) > 1:
            prospective_defenders.sort(key=lambda x: x[1], reverse=True)
            prospective_defenders = [i for i in prospective_defenders if i[1] == max(
                [j[1] for j in prospective_defenders])]
            # by max damage of defender
            if len(prospective_defenders) > 1:
                prospective_defenders = sorted([(i[0], effective_power(i[0])) for i in prospective_defenders],
                                               key=lambda x: x[1], reverse=True)
                prospective_defenders = [i for i in prospective_defenders if i[1] == max(
                    [j[1] for j in prospective_defenders])]

                # by max initiative
                if len(prospective_defenders) > 1:
                    prospective_defenders.sort(
                        key=lambda x: x[0][INIT], reverse=True)
                    defender_id = prospective_defenders[0][0][ID]
                else:
                    defender_id = prospective_defenders[0][0][ID]
            else:
                defender_id = prospective_defenders[0][0][ID]
        else:
            defender_id = prospective_defenders[0][0][ID]

    if defender_id == -1:
        return -1, -1

    visited.add(prospective_defenders[0][0][ID])

    return defender_id, damage(attacker, prospective_defenders[0][0])


def clean(groups):
    return [i[:-2] for i in groups if i[COUNT] > 0]


def part1(f_name):
    groups = input_parser(f_name)

    while True:
        groups.sort(key=lambda x: (effective_power(x), x[INIT]), reverse=True)
        visited = set()

        for g in groups:
            g.extend(find_enemy(g, groups, visited))

        groups.sort(key=lambda x: x[INIT], reverse=True)

        for g in groups:
            deal_dmg(g, groups)
        groups = clean(groups)
        # check if done
        immune_count = len([i for i in groups if i[U_TYPE] == IMMUNE_TYPE])
        if immune_count == len(groups) or immune_count == 0:
            print(sum([i[COUNT] for i in groups]))
            break


def part2(f_name):
    initial_state = input_parser(f_name)
    additional_dmg = 119
    # part 2
    infection_wins = False
    for _ in range(1):
        groups = copy.deepcopy(initial_state)

        for g in groups:
            if g[U_TYPE] == IMMUNE_TYPE:
                g[AD] += additional_dmg

        while True:
            groups.sort(key=lambda x: (
                effective_power(x), x[INIT]), reverse=True)
            visited = set()

            for g in groups:
                g.extend(find_enemy(g, groups, visited))

            groups.sort(key=lambda x: x[INIT], reverse=True)

            for g in groups:
                deal_dmg(g, groups)
            groups = clean(groups)
            # check if done
            immune_count = len([i for i in groups if i[U_TYPE] == IMMUNE_TYPE])
            if immune_count == len(groups):
                print("Immune", sum([i[COUNT]
                                     for i in groups]), additional_dmg)
                break
            if immune_count == 0:
                print("Infection", sum([i[COUNT] for i in groups]))
                infection_wins = True
                break
        if infection_wins:
            print(additional_dmg+1)
            break
        else:
            additional_dmg -= 1


# part1("test.txt")
part1("input.txt")

# part2("test.txt")
part2("input.txt")
