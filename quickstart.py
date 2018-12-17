from fakedb import FakeDB
myDB = FakeDB()
myDB.create("name","David")
myDB.create("age",21)
myDB.create("places",["watoto","weight of glory","winners"])
myDB.create("artist","Leonardo DaVinci")
myDB.commit('david.json')
>>> '9ac16b9b'
print(myDB.get_objects())
>>> {'9ac16b9b': {'name': 'David', 'age': '21', 'places': ['watoto', 'weight of glory', 'winners'], 'artist': 'Leonardo DaVinci'}}
print(myDB.update('9ac16b9b',{'time':'never'}))
print(myDB.get_objects())
>>> {'9ac16b9b': {'name': 'David', 'age': '21', 'places': ['watoto', 'weight of glory', 'winners'], 'artist': 'Leonardo DaVinci', 'time': 'never'}}
print(myDB.clear('9ac16b9b'))
print(myDB.get_objects())
>>> {'9ac16b9b': {}}
