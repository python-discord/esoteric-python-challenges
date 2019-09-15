# Challenge 10 - Code Obfuscator

## Challenge Overview

On the day I joined this server, I had an idea to create a program which obfuscates strings. For this challenge, I think it would be quite cool to see what other types of obfuscation that you people can come up with. Your code submission should be able to obfuscate strings or code in a unique way while still keeping functionality fully in tact. It would also be nice to see some example code along with your submission which makes use of this obfuscation. Try to make it as interesting and funky as possible! :)

### Examples

Here is the sort of obfuscation that my program created:

```py
bytes([(True << (True ^ True << True) ^ True << (True ^ True << (True << True)) ^ True << (True << True ^ True << (True << True))), (True ^ True << (True << True) ^ True << (True ^ True << (True << True)) ^ True << (True << True ^ True << (True << True))), (True << (True << True) ^ True << (True ^ True << True) ^ True << (True ^ True << (True << True)) ^ True << (True << True ^ True << (True << True))), (True << (True << True) ^ True << (True ^ True << True) ^ True << (True ^ True << (True << True)) ^ True << (True << True ^ True << (True << True))), (True ^ True << True ^ True << (True << True) ^ True << (True ^ True << True) ^ True << (True ^ True << (True << True)) ^ True << (True << True ^ True << (True << True)))]).decode()
```

That whole mess simply evaluates to a single string: `"hello"`. Of course, this is only an example. Do try to think of a unique way of obfuscating things!

## Restrictions

None!

## Submissions Guidelines

* Submit your code as a python file named `<yourname>.py` in the `solutions` directory. If your implementation is too big or you simply prefer splitting the code into several files, submit a directory named `<yourname>` with the code inside. See the `README.md` file in the root of the repository for more information on contributing solutions.

Happy Hacking ❤️ Shawn (aka Zhawn) and Juanita

# Licensing Information

## By contributing to this repository, you understand and agree that all code in this repository is licensed under the [GNU General Public License, Version 3 (GPLv3)](https://www.gnu.org/licenses/gpl-3.0.html).
