Minimal Python library to create Local JSON databases for small applications

Usage:

img: '/img/fakedb.png'

```python
from fakedb import FakeDB
myDB = FakeDB()
myDB.create("name","David")
myDB.create("age",21)
myDB.create("places",["watoto","weight of glory","winners"])
myDB.create("artist","Leonardo DaVinci")
myDB.commit('david.json')
print(myDB.get_objects())
```
