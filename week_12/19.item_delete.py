# 항목 삭제하기
capitals = {}
capitals['Korea'] = 'Seoul'
capitals['USA'] = 'Washington'
capitals['UK'] = 'London'
capitals['France'] = 'Paris'
print(capitals)

city = capitals.pop('UK')
if 'UK' in capitals:
    capitals.pop('UK')
