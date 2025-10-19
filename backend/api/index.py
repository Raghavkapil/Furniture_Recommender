# backend/api/index.py
# This file acts as the Vercel entry point.
# It imports your main FastAPI 'app' from your existing 'app.main' file.

import sys
import os

# Add the 'app' directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'app')))

# Import the FastAPI app instance from your main.py
from main import app