from fakedb import FakeDB
myDB = FakeDB()
myDB.create("name","David")
myDB.create("age",200)
myDB.create("places",["watoto","weight of glory","winners"])
myDB.create("artist","Leonardo DaVinci")
myDB.commit('david.json')
print(myDB.get_objects())
