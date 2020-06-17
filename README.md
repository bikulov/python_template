### Features

* you may run as ordinary python script or use compiled version
* building with clang
* has subprograms: example includes common and special for subprograms cli arguments
* has logging with verbose switch
* includes testing


### Prerequisites

For compilation:

```
apt install python3-dev clang cython
```

For pytest running without compilation:

```
apt install python3-pytest
```

### How to try

Clone repository:

```
git clone git@github.com:bikulov/python_template.git
```


#### If you want to try binary build

Compile and run:
``` bash
make

$ ./python_template first_module --name ksar
[(unknown file):0] INFO     [2019-02-22 00:30:43]  ksar
```

To execute tests:

``` bash
make test
```

#### If you want to run python script without compilation

Run program:

```
$ ./python_template.py first_module --name ksar
[python_template.py:56] INFO     [2020-06-17 23:54:14]  ksar
```

Run tests:

```
py.test-3
```

