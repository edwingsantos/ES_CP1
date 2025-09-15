#ES 1 crews share

print("The crew earned a whole bunch of money on the last outing but the captain didn't have time to divvy it all up before release everyone to port. He gave each member of the crew 500 dollars for the evening and then sat down with his first mate to properly divide the shares. ")
money_earned = float(input("choose how much money you want the crew to find: "))
crew_num = int(input("How many people do you want in the crew not counting the capitan and first share?: "))

share = (money_earned / (crew_num + 10))

cap_share = share * 7
first_mate = share * 3

final_share = share - 500

print(f"the crew still need to get paid ${final_share:.2f}")
print(f"the capitan gets ${cap_share:.2f}")
print(f"the first mate gets ${first_mate:.2f}")