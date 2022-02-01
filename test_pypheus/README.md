#Testing PYPHEUS

All PRs must contain matching tests and a PR will not be accepted without passing the entire
test suite.

API calls have been recorded using the vcrpy library.

Travis-CI has been used for continuous testing.

## The VCR tests require environment variables:
```
export HOST='<ip address or FQDN>'
export USERNAME='<username>'
export PASSWORD='<password>'
```
## To run the tests:
```
python3 -m nose test_pypheus_network.py
```
##--------------------------------------------------------------------------------------
After the first run of the nose test, cassettes will be automatically generated
and placed in the cassettes directory.

## Test environment

We acknowledge that different testing environments will have different IP addresses.
To mitigate these differences, we ask that developers place a new entry in their /etc/hosts file
to point the hostname *pypheus-test.local* to the address of their local Morpheus instance.

Note: It is mandatory to use the hostname pypheus-test.local as the vcrpy cassette files are using this hostname
and the Travis CI integration has been setup to use this hostname as well.

If you choose to use a different name the test will fail and your PR will not be accepted.
