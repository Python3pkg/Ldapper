class LdapperException(Exception):
    pass

class LdapperInterface(object):
    @staticmethod
    def define(searchBase, primarySearch, **kwargs):
        return LdapperModelDefinition(searchBase, primarySearch, **kwargs)


class LdapperModelDefinition(object):
    def __init__(self, searchBase, primarySearch, attributes=['*'], connection=None):
        self.wrap = False
        self._searchBase = searchBase
        if "(" not in primarySearch:
            primarySearch = "(%s)" % primarySearch
        self._primarySearch = primarySearch
        self._attributes = attributes
        self._connection = connection
    def using(self, connection):
        return LdapperModelDefinition(self._searchBase,
                self._primarySearch,
                attributes=self._attributes,
                connection=connection)

    def get(self, primary):
        if not self._connection:
            raise LdapperException()
        self._connection.search(self._searchBase, self._primarySearch % primary, attributes=self._attributes)
        if len(self._connection.entries) != 1:
            return None
        else:
            return self._connection.entries[0]

    def find(self, **kwargs):
        search = "(&"
        for pair in kwargs.items():
            search += "(%s=%s)" % pair
        search += ")"
        return self.find_raw(search)

    def find_raw(self, search):
        self._connection.search(self._searchBase, search, attributes=self._attributes)
        return self._connection.entries
