#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Entry point for Space Typing Game executable.
This file ensures proper package imports when running as .exe
"""

import sys
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run main
from src.main import main

if __name__ == "__main__":
    main()
