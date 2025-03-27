import os
import sys
from pathlib import Path


# def create_root_path():
#     root_path = Path(__file__).parent.resolve()
#     print(root_path)
#     if root_path not in sys.path:
#         sys.path.insert(0, os.path.join(root_path))
#
#
# create_root_path()
from create_app import create_app
from app.api.api import router as api_router

app = create_app()

app.include_router(api_router)

