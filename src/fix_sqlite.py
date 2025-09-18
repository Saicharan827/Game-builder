# fix_sqlite.py
import sys
import types

# Fake sqlite3 module for Chroma
sqlite3_fake = types.ModuleType("sqlite3")
sqlite3_fake.sqlite_version = "3.40.0"  # any version >= 3.35
sqlite3_fake.sqlite_version_info = (3, 40, 0)

# Inject into sys.modules
sys.modules["sqlite3"] = sqlite3_fake
