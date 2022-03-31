import os

class Config(obj):
  SECRET = os.environ.get("SECRET") or "junoah-that-its-gonna-be-good"
  DEBUG = bool(os.environ.get("DEBUG")) or True
