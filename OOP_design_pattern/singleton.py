def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper


@singleton
class DBConnection(object):

    def __init__(self):
        """Initialize your database connection here."""
        pass

    def __str__(self):
        return 'Database connection object'


db = DBConnection()
db2 = DBConnection()
db3 = DBConnection()

db4 = DBConnection()

print(id(db))
print(id(db2))
print(id(db3))
print(id(db4))