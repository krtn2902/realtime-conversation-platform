from waitress import serve
from a_core.asgi import application
import os
import sys

port = int(sys.argv[1]) if len(sys.argv) > 1 else 8000
print(f"Starting server on port {port}...")
serve(application, host="0.0.0.0", port=port)
