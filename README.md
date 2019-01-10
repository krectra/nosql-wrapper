# nosql-wrapper
NoSQL wrapper

I created this to lessen the need to recreate instances of connection to NoSQL databases.
Basically all python dependency per NoSQL would be handle by this library.

Version:

- **Python 3**

### Databases
Supported:
- [x] MongoDB

To-Do:
- [ ] Cassandra
- [ ] Redis
- [ ] Riak
- [ ] DynamoDB

### MongoDB
For MongoDB, we are using `pymongo` library

#### Initialize
```python
from nosql_wrapper import MongoDB
database = MongoDB(url='mongodb://<HOST>:<PORT>/')
```

or

```python
from nosql_wrapper import MongoDB
database = MongoDB(port=<PORT>, host=<HOST>)
```

#### Retrieve client
```python
client = database.get_client()
```

From here you can now perform `pymongo` library commands
##### Example
Getting a Database
```python
db = client.mydatabase
```

or

```python
db = client["mydatabase"]
```


##### Notes
- My Release Notes for now: [Changelog](CHANGELOG.md)
- This is just an initial implementation and will be further improved in the future