__version__ = "0.0.1"
from BootstrapReport import checkers
from BootstrapReport import helpers
from _diagnostics import DiagnosticsMixin
from .package import ObjectOfInterest

"""
    BootstrapReport module
    ============================
    Use it to import very important functions.
    Package structure
    -----------------
    .
    ├── __init__.py
    ├── examples -> Data calculations stored here
        ├── __init__.py
        ├── examples.py -> Examples file
    ├── BootstrapReport.py -> Main functions stored here
    ├── helpers.py -> Helper functions stored here
    ├── checkers.py -> Functions that check certain inputs and outputs stored here
"""
