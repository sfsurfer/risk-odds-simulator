from random import randint
import sys

# roll([1|2|3],[1|2]), returns [attackLoss, defenseLoss]
def roll(attack, defense):
    #print("attacking with: " + str(attack))
    #print("defending with: " + str(defense))
    attackRolls = []
    defenseRolls = []
    for i in range(attack):
        attackRolls.append(randint(1,6))
    for i in range(defense):
        defenseRolls.append(randint(1,6))
    #print("Attacker rolled" + str(attackRolls))
    #print("Defense rolled" + str(defenseRolls))
    aLosses = 0
    dLosses = 0
    for a,d in zip(sorted(attackRolls,reverse=True),sorted(defenseRolls,reverse=True)):
        if a > d:
            dLosses += 1
        else:
            aLosses += 1
    return [aLosses,dLosses]

def attack(attackDice, defenseDice):
    while attackDice > 1 and defenseDice > 0:
        if attackDice > 3 and defenseDice > 2:
            res = roll(3,2)
        elif attackDice > 3:
            res = roll(3,defenseDice)
        elif defenseDice > 0:
            res = roll(attackDice,2)
        else:
            res = roll(attackDice,defenseDice)
        # print(res)
        attackDice -= res[0]
        defenseDice -= res[1]
    return [attackDice,defenseDice]


rounds = 1000
attackWins = 0
defenseWins = 0

attackWinsLeft = []
defenseWinsLeft = []

attackDice = int(sys.argv[1])
defenseDice = int(sys.argv[2])

for i in range(rounds):
    result = attack(attackDice, defenseDice)
    if result[0] == 1:
        # print("Defense won")
        defenseWins += 1
        defenseWinsLeft.append(result[1])
    if result[1] == 0:
        # print("Attack won")
        attackWins += 1
        attackWinsLeft.append(result[0])

winPercent = (attackWins * 100)/float(rounds)

print("Attack Wins = " + str(attackWins))
print("Attacker won " + str(winPercent) + "%")

if len(attackWinsLeft) > 0:
    print("Average Attackers Left: " + str(reduce(lambda x, y: x + y, attackWinsLeft)/float(len(attackWinsLeft))))
else:
    print("Average Attackers Left: 0")
if len(defenseWinsLeft) > 0:
    print("Average Defenders Left: " + str(reduce(lambda x, y: x + y, defenseWinsLeft)/float(len(defenseWinsLeft))))
else:
    print("Average Defenders Left: 0")