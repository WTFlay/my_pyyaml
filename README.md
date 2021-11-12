# MyPyYaml library

A simple library for parsing Yaml writted in Python3.

## Usage

```bash
$ python3
>>> from my_pyyaml import MyPyYaml
>>> parser = MyPyYaml()
>>> parser.parse("name: Jon Snow")
{'name': 'Jon Snow'}
```

## Tests

You can run test by running `test_my_pyyaml.py`:
```bash
$ ./test_my_pyyaml.py 
...
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```
