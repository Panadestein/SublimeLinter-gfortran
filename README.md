-----------------------------------------------------------------

SublimeLinter-gfotran
================================

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to [gfotran](https://gcc.gnu.org/wiki/GFortran). It will be used with files that have the “FORTRAN” syntax (free format). This is highly inpired by the [SublimeFortran](https://github.com/315234/SublimeFortran.git) package's linter, however some changes have been introduced to simplify and improve the regex matching.

*Warning:* Only tested in an Arch Linux box with GNU Fortran 9.3.0 and Sublime Text Build 3211.

## Installation

SublimeLinter must be installed in order to use this plugin. 

Please clone this repo into your `Packages` directory.

Before installing this plugin, you must ensure that `gfotran` is installed on your system.

In order for `gfotran` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
