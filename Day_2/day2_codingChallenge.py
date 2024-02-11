# Life expectancy calculator
yourAge = input("How old are you today?\n")
ageInWeeks = int(yourAge) * 52
maxWeeks = 4680
weeksLeft = maxWeeks - ageInWeeks

print(f"Damn son - you only have {weeksLeft} weeks left before turning 90.")