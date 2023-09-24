import datetime, random


def getBirthdays(NumBirthdays):
    birthdays = []
    for i in range(NumBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None

    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA


print("Birthday Paradox, shows odds of two people having matching birthday in a group of people")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays to generate?")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        numBdays = int(response)
        break
print()

print(f"Here are {numBdays} birthdays")
birthdays = getBirthdays(numBdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(',', end="")
        monthName = MONTHS[birthday.month - 1]
        dateText = '{} {}'.format(monthName, birthday.day)
        print(dateText, end="")
print()
print()

match = getMatch(birthdays)

print('In this simulation, ', end="")
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print('multiple people have a birthday on', dateText)
else:
    print("no matching birthdays")
print()

print('generating')
input("press enter to begin")

simMatch = 0
for i in range(100_000):
    if i % 10_000 == 0:
        print(i, 'simulations run')
    birthdays = getBirthdays(numBdays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("simulations complete")
probability = round((simMatch / 100_000) * 100, 2)
print(f"probability comes out to {probability}")
