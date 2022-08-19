# easy-choose

### It can easily help you choose!

<br>

## Installation
Use pip:

`pip install --upgrade easy-choose`

<br>

## Usage
It's particularly simple to use. The code is as follows:

`>>>import easy_choose as ec`

`>>>ec.choose(2, "A", "B", "C")`

`["A", "C"]`

Of course, you can also use lists:

`>>> ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]`

`>>> ec.choose(5, *ls)`

`[1, 4, 4, 7, 5]`

You can also keep them from duplicate elements:

`>>> ec.choose(5, only=True,  *ls)`

`[1, 4, 7, 5]`

## Tests

You can use ready-made test functions – just test and play!

Here's how:

`>>> from easy_choose import tests as te`

`>>> te.testnumbers(number=5, num=3)`

`[1, 3, 3, 1, 2]`

<br>
<br>

#### Version: 1.0.9

#### Author: Raskora

#### Github: [https://github.com/Raskora/easy-choose](https://github.com/Raskora/easy-choose)