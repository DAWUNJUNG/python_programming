# 항목 방문하기
capitals = {'Korea': 'Seoul', 'USA': 'Washington', 'UK': 'London'}
for key in capitals:
    print(key, ':', capitals[key])

capitals = {'Korea': 'Seoul', 'USA': 'Washington', 'UK': 'London'}
for key, value in capitals.items():
    print(key, ':', value)

capitals = {'Korea': 'Seoul', 'USA': 'Washington', 'UK': 'London'}
print(capitals.keys())
print(capitals.values())

for key in sorted(capitals.keys()):
    print(key, end=' ')
