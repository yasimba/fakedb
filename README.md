![](/img/fakedb.png)

Minimal Python library to create Local JSON databases for small applications

Usage:

```python
>>> from fakedb import FakeDB
>>> myDB = FakeDB()
>>> myDB.create("name","David")
>>> myDB.create("age",200)
>>> myDB.create("places",["watoto","weight of glory","winners"])
>>> myDB.create("artist","Leonardo DaVinci")
>>> myDB.commit('david.json')
>>> print(myDB.get_objects())
{'9ac16b9b': {'name': 'David', 'age': '200', 'places': ['watoto', 'weight of glory', 'winners'], 'artist': 'Leonardo DaVinci'}}
>>> myDB.update('9ac16b9b',{'time':'never'})
>>> print(myDB.get_objects())
{'9ac16b9b': {'name': 'David', 'age': '200', 'places': ['watoto', 'weight of glory', 'winners'], 'artist': 'Leonardo DaVinci', 'time': 'never'}}
>>> myDB.clear('9ac16b9b')
>>> print(myDB.get_objects())
{'9ac16b9b': {}}
```
