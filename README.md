# pypheus


A python3 API for interacting with the Morpheus RESt client

## Configuration

Simple installation:

```
pip3 install pypheus
```
Each element of the above can be independently overridden using the "connection_data" object parameter for each action.

**Note** :you will import pypheus into your python script.

```
from pypheus.storage import Storage

# Create an instance of the storage class, pass credentials
storage = Storage(host,username,password)

# Call the API
info = storage.get_all_volumes()

# Return will be json
for v in info['storageVolumes']:
    print(v)
```

## Documentation
[Documentation for pypheus can be found here](http://apidocs.morpheusdata.com)

## Functions

* `network.py` - Various network API calls
* `storage.py` - Get storage buckets and volumes
* `monitoring.py` - Alerts, incidents, contacts, checks
* `logs.py` - Log dump
