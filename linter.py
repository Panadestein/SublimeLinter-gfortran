"""Gfortran SublimeLinter4 configuration"""
from SublimeLinter.lint import Linter


class FortLint(Linter):
    """A class defining the linter"""
    cmd = 'gfortran -cpp -fsyntax-only -Wall ${file}'
    multiline = True
    defaults = {
        'selector': 'source.modern-fortran'
    }
    on_stderr = True
    regex = (
        r"^[^:]*:(?P<line>\d+)[:.](?P<col>\d+):"
        r"(?:(\s*.*\s.*\d+\s*))"
        r"(?:(?P<error>Error|Fatal\sError)|(?P<warning>Warning)): (?P<message>.*$)"
    )
