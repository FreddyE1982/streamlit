"""Testing utilities for Streamlit.

This package exposes versioned testing APIs. Use :mod:`streamlit.testing.v1`
for helper classes that allow programmatic interaction with Streamlit
applications when writing pytest tests.
"""

from __future__ import annotations

from . import v1

__all__ = ["v1"]
