food_cost = int(input("음식 비용: "))

tip_percentage = input("팁 비율: ")
tip_percentage = int(tip_percentage.replace('%', ''))

tip = int(food_cost * tip_percentage / 100)

total_cost = food_cost + tip

print(f"총액: {total_cost} 달러")