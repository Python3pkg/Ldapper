# Ldapper
Model Interface for ldap3 pyhon module


### Example Usage
```python
from ldapper import LdapperInterface as Ldapper
conn = Connection(...)

User = Ldapper.define("ou=People,dc=example,dc=com", "uid=%s")

user = User.using(conn).get("user1")

activeUsers = User.using(conn).find(active='TRUE')
```


