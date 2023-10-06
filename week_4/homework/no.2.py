num_chickens = input("닭의 수: ")
num_pigs = input("돼지의 수: ")
num_cows = input("소의 수: ")

chicken_legs = int(num_chickens) * 2

pig_legs = int(num_pigs) * 4

cow_legs = int(num_cows) * 4

total_legs = chicken_legs + pig_legs + cow_legs

print(f"전체 다리의 수: {total_legs}")