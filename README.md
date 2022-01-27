# pypheus


A python3 API for interacting with the Morpheus RESt client

## Configuration

Simple installation:

```
pip3 install pypheus
```
Each element of the above can be independently overridden using the "connection_data" object parameter for each action.

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** :you will import pypheus into your python script.

```
from pypheus.storage import Storage
storage = Storage(host,username,password)
info = storage.get_all_volumes()
for v in info['storageVolumes']:
    print(v)
```

## Functions

* `network.py` - Various network API calls
* `storage.py` - Get storage buckets and volumes
* `monitoring.py` - Alerts, incidents, contacts, checks
* `logs.py` - Log dump
