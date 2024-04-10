# Calculation notation converter

## INDEX
- [Description](#description)
- [Purpose](#purpose)
- [How to Install](#how-to-install)
- [How to Use](#how-to-use)
- [Known Bugs](#known-bugs)
- [Implementation Request](#implementation-request)
- [Contact](#contact)

## Description:
A CLI application to convert calculation notations between prefixes, infixes, and postfixes/suffixes.

###### [(Return to index)](#index)
## Purpose
The purpose or purpose of this repository is to show my way of coding and organizing/writing documentation.

The intention is for it to count as a portfolio project.

###### [(Return to index)](#index)
## How to install
Now to install it, follow these steps.
> REQUIRED:
> - Git or GitHub CLI
> - Python 3.7+

1. Clone the repository.
```sh
$> git clone https://github.com/livecodelns/calcs_conversion_python.git
```
2. Enter the directory.
```sh
$> cd calcs_conversion_python
```
3. Run [(See How to use)](#how-to-use)

###### [(Return to index)](#index)
## How to use
Currently it can only be run through python 3.7+.

> We need:
> - The initial calculation or expression
> - The notation we want to obtain

We use the `--initial-calculation` flag (Abbreviated: `-ic`) to specify the calculation and the `--target-notation` flag (Abbreviated: `-tn`) to specify the notation we want to return.

> Supported values for *-tn*:

     1 (PREFIX)
     2 (INFIX)
     3 (POSTFIX/SUFFIX)

> Examples:
```sh
$> py main.py -ic '((3*4)+5^6-7)/8' -tn 1
```
```sh
$> py main.py -ic '((2^3)/4+5-6)*7' -tn 3
```

###### [(Return to index)](#index)
## Known Bugs
The conversion of the notations is still in development, if attempted it causes an error.
- Prefix => Infix
- Prefix => Postfix
- Postfix => Infix
- Postfix => Prefix

###### [(Return to index)](#index)
## Implementation Request
For any request you can create `Issues`.

###### [(Return to index)](#index)
## Contact
You can contact me to send comments, donations, project proposals, ideas, personalized classes, etc.

*NOTE*: In case of donations, please consult in advance to guide and facilitate the process.

Everything is welcome and adds up, I appreciate it.

* WhatsApp: +54 9 11 3845 3811
* Mail: _livecodelns@gmail.com_
* YouTube: [*_YouTube_* Channel](https://YouTube.com/@livecodelns)
* Twitch: [*_Twitch_* Channel](https://Twitch.tv/LiveCodeLNS)
* Instagram: [*_Instagram_* profile](https://www.instagram.com/livecodelns)

###### [(Return to index)](#index)