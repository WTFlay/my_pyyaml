# MyPyYaml library

A simple library for parsing Yaml writted in Python3.

## Usage

```bash
$ python3
>>> from my_pyyaml import MyPyYaml
>>> yaml = MyPyYaml()
>>> yaml.load("name: Jon Snow")
{'name': 'Jon Snow'}
```

## Tests

You can run test by running `test_my_pyyaml.py` from command line:
```bash
$ ./test_my_pyyaml.py 
......
----------------------------------------------------------------------
Ran 6 tests in 0.003s

OK
```
