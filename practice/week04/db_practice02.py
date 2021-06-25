from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.get_database('person')

# db.users.insert_one({'name': '덤블도어', 'age': 116})
# db.users.insert_one({'name': '맥고나걸', 'age': 85})
# db.users.insert_one({'name': '스네이프', 'age': 60})
# db.users.insert_one({'name': '해리', 'age': 40})
# db.users.insert_one({'name': '허마이오니', 'age': 40})
# db.users.insert_one({'name': '론', 'age': 40})

all_users = list(db.users.find({}))

print(all_users[0])  # 0번째 결과값을 보기
see_all = db.users.find_one({'name': '덤블도어'}, {"_id" : False})
print(see_all)

upAge = db.users.update_many({'age': 60}, { '$set': {'age': 50}})

findAge = list(db.users.find({'age': 50}, {'_id': False}))
print(findAge)

db.users.delete_one({'name': '론'})
print(list(db.users.find({})))


