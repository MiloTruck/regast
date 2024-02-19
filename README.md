# **regast**

> [!NOTE]
> **regast** has not been maintained since March 2023. If you're trying to run it, it will most probably throw an error during the parsing stage. 
> 
> Nevertheless, feel free to look through the code to get an idea of how to implement your own static analyzer.

**regast** is a static analyzer for identifying security vulnerabilities and gas optimizations in Solidity codebases.

It is heavily inspired by tools such as [Slither](https://github.com/crytic/slither), [solstat](https://github.com/0xKitsune/solstat) and [4naly3er](https://github.com/Picodes/4naly3er), but has the following differences:
* **No compilation:** regast is able to run directly without compilation, making it viable for codebases that are difficult to compile.
* **Easy to customize:** regast is designed for users to easily write and run their own custom detectors.

## Table of Contents
- [**regast**](#regast)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Detectors](#detectors)
    - [Included detectors](#included-detectors)
    - [Writing custom detectors](#writing-custom-detectors)
  - [Sample Reports](#sample-reports)
  - [Implementation](#implementation)
    - [Repository structure](#repository-structure)


## Installation
**regast** requires Python 3.10 or above.

First, clone this repository and its submodules:
```sh
git clone --recurse-submodules https://github.com/MiloTruck/regast.git
cd regast
```

Install **regast** using either `pip` or `setuptools`:
```sh
# Using pip
pip3 install .

# Using setuptools
python3 setup.py install
```

After installation, the repository can be deleted:
```sh
cd ..
rm -r regast
```

## Usage
The `regast` command can be used on either `.sol` file or a folder containing Solidity files:
```
$ regast --help
usage: __main__.py [-h] [-d <detector>] [-c <classifications>] [-s <scope>] [-r <filename>] <contract>

Scan for vulnerabilities based on regex or AST queries.

positional arguments:
  <contract>            .sol file or folder containing .sol files to scan

options:
  -h, --help            show this help message and exit
  -d <detector>, --detectors <detector>
                        .py file or folder containing .py files which implement detectors
  -c <classifications>, --classifications <classifications>
                        Comma-separated list of classifications: GAS, NC, LOW, MEDIUM, HIGH
  -s <scope>, --scope <scope>
                        Text file containing a list of contracts in scope
  -r <filename>, --report <filename>
                        Generate a markdown report in <filename>.md
```

## Detectors

### Included detectors
Below are the currently implemented detectors which **regast** runs by default. Most of the detectors from [4naly3er](https://github.com/Picodes/4naly3er) and [solstat](https://github.com/0xKitsune/solstat) will be included in the future.

| Detector                                                                         | Description                                                               | Classification |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------- | -------------- |
| [`address_balance`](regast/detectors/gas/address_balance.py)                     | Use `selfbalance()` instead of `address(this).balance`.                   | Gas            |
| [`address_zero`](regast/detectors/gas/address_zero.py)                           | Use assembly to check for `address(0)`.                                   | Gas            |
| [`assign_update_array_value`](regast/detectors/gas/assign_update_array_value.py) | Update array values using `arr[i] += n` instead of `arr[i] = arr[i] + n`. | Gas            |
| [`bool_comparison`](regast/detectors/gas/bool_comparison.py)                     | Don\'t compare booleans to `true` or `false`.                             | Gas            |
| [`bool_storage`](regast/detectors/gas/bool_storage.py)                           | Using `bool` for storage incurs overhead.                                 | Gas            |
| [`byte_constant`](regast/detectors/gas/byte_constant.py)                         | `bytes` constants are more efficient than `string` constants.             | Gas            |
| [`cache_array_length`](regast/detectors/gas/cache_array_length.py)               | Cache array length outside of for-loops.                                  | Gas            |
| [`custom_error`](regast/detectors/gas/custom_error.py)                           | Use custom errors instead of `require` statements.                        | Gas            |
| [`initialize_default_value`](regast/detectors/gas/initialize_default_value.py)   | Unnecessary initialization of variables with default values               | Gas            |
| [`long_revert_string`](regast/detectors/gas/long_revert_string.py)               | `require` statements with long error messages.                            | Gas            |
| [`post_increment`](regast/detectors/gas/post_increment.py)                       | `++i` costs less gas than `i++` or `i += 1`.                              | Gas            |
| [`private_constant`](regast/detectors/gas/private_constant.py)                   | Declare constants as `private` instead of non-public to save gas.         | Gas            |
| [`shift_arithmetic`](regast/detectors/gas/shift_arithmetic.py)                   | Use `<<` and `>>` instead of multiplication/division where possible.      | Gas            |
| [`split_require_statements`](regast/detectors/gas/split_require_statements.py)   | Use separate `require` statements instead of `&&`.                        | Gas            |
| [`unchecked_increment`](regast/detectors/gas/unchecked_increment.py)             | 'Increments can be declared `unchecked` in for-loops'.                    | Gas            |
| [`unsigned_comparison`](regast/detectors/gas/unsigned_comparison.py)             | Use `!= 0` instead of `> 0` for unsigned integer comparison.              | Gas            |

### Writing custom detectors

For information on how to write custom detectors, please refer to [`docs/writing-custom-detectors.md`](docs/writing-custom-detectors.md).

## Sample Reports

**regast** is able to generate markdown reports with the issues found. For an example, please refer to the following sample reports:

* [Llama Report](/examples/reports/llama-report.md)
* [Juicebox Report](/examples/reports/juicebox-report.md)

## Implementation
**regast** is built on top of [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python), which provides Python bindings for the [tree-sitter](https://tree-sitter.github.io/tree-sitter/) parsing library. The grammar for Solidity is taken from [tree-sitter-solidity](https://github.com/JoranHonig/tree-sitter-solidity).

`tree-sitter` first converts Solidity source code into multiple abstract syntax trees (AST). **regast** then parses each node in these ASTs into corresponding Python classes. After the parsing is completed, individual detectors query the AST through these Python classes to identify common vulnerability patterns.

### Repository structure
Most of **regast**'s code are in the following directories:
* [`regast/core`](regast/core) contains Python classes which represents parts of the AST.
* [`regast/detectors`](regast/detectors) contains detectors which **regast** runs by default.
* [`regast/parsing`](regast/parsing) contains the logic for parsing the AST from `tree-sitter` into Python classes. 