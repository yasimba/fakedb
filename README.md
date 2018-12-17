Minimal Python library to create Local JSON databases for small applications

Usage:

```python
from fakedb.FakeDB import FakeDB
dave = FakeDB()
dave.create("name","David")
dave.create("age",21)
dave.create("churches",["watoto","weight of glory","winners"])
dave.create("artist","Leonardo DaVinci")
dave.commit('david.json')
print(dave.get_objects())
```
