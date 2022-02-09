![bestpy-image](bestpy-image.png)

# bestpy

[![License](https://badgen.net/github/license/gustavwilliam/bestpy)](https://github.com/gustavwilliam/bestpy/blob/main/LICENSE)
[![Linting](https://github.com/gustavwilliam/bestpy/actions/workflows/linting.yaml/badge.svg?branch=main)](https://github.com/gustavwilliam/bestpy/actions/workflows/linting.yaml)
[![Testing](https://github.com/gustavwilliam/bestpy/actions/workflows/testing.yaml/badge.svg?branch=main)](https://github.com/gustavwilliam/bestpy/actions/workflows/testing.yaml)
[![Build & Push](https://github.com/gustavwilliam/bestpy/actions/workflows/publish.yml/badge.svg)](https://github.com/gustavwilliam/bestpy/actions/workflows/publish.yml)
[![Coverage Status](https://coveralls.io/repos/github/gustavwilliam/bestpy/badge.svg?branch=main)](https://coveralls.io/github/gustavwilliam/bestpy?branch=main)
[![GitHub stars](https://img.shields.io/github/stars/gustavwilliam/bestpy?style=social&label=Star&maxAge=2592000)](https://github.com/gustavwilliam/bestpy/stargazers/)

A module to prove your friends (or adversaries) wrong.

Ever needed to decide on what is the best thing out? That's exactly what bestpy does.
We may or may not try to make the answers support your view. Here's a quick demo:

```python
>>> best.language
"python"
>>> best.module
"bestpy"
```

## Table of content

- [Installation](#installation)<br>
  - [Dev installation](#dev-installation)<br>
- [Usage](#usage)<br>
  - [Different ways to access items](#different-ways-to-access-items)<br>
  - [Hard coded answers](#hard-coded-answers)<br>
  - [Dynamic answers](#dynamic-answers)<br>
  - [Random answers](#random-answers)<br>
- [Contributing](#contributing)<br>
- [Final words](#final-words)

## Installation
This is simple with pip. Just run the following in your command line or terminal:

```
pip install bestpy
```

You can also use your magic powers to get the module from the latest version of the source code using the following:

```
pip install git+https://github.com/gustavwilliam/bestpy.git@main
```
Note: you will likely need to restart your terminal before using the module

### Dev installation
If you want to contribute to the bot, follow the [dev install instructions](CONTRIBUTING.md#dev-installation) instead.

## Usage
We were kind and made importing it super simple and nice. Just do the following to import bestpy, once the installation is complete:

```python
>>> from bestpy import best
```

Now you'll be ready to take on any of life's greatest challenges, all with the help of bestpy.

### Different ways to access items

You can access items through both attribute and item access.

```python
>>> best.module  # Attribute access
bestpy
>>> best["module"]  # Item access
bestpy
```

### Hard coded answers

Here's how you can find out some hard coded, fundamental laws of the universe:

```py
>>> best.year
1984
>>> best.phone
BlackBerry
```

### Dynamic answers

There are also a few things that may sneakily check your preferences and adjust based on it, like the following.
You'll get your current OS back, since you obviously have a good taste in what OS you use.

```python
>>> best.os
```

### Random answers

There are also a few ones that use randomness to find the truth, from a list of answers.

```py
>>> best.name
Guido
>>> best.name
Gustav
```

If there's something you'd like to see added, feel free to open an issue or submit a PR.
The available categories will expand over time, thanks to our awesome contributors.

## Contributing

Fantastic that you want to be a part of the project! The project is actively maintained, and accepts issues and
pull requests for bug fixes, new "answers" and improvements to the core functionality.

Check out [CONTRIBUTING.md](CONTRIBUTING.md) to get started!

## Final words
Good luck proving what things are actually best. Bestpy is never wrong,
so you now know everything you need to use the single source of truth.
Feel free to share what you create with bestpy. I can't wait to see what you do!

May the bestpy be with you. The bestpy is strong with this one.
