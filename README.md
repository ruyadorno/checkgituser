# checkgituser

Checks a folder to find .git/config files without an [user] field declared


## Usage

Just invoke the script pointing to a folder to browse for `.git/config` files.
If any .git/config file does not have a [user] property declared, its path will be printed.

    $ ./checkgituser.py ~/


## Installation

You can install this script by simply linking it to any `bin/` folder available on your `$PATH` variable.

    $ sudo ln -s checkgituser/checkgituser.py /usr/bin/checkgituser


## License

MIT
