import sys
try:
    import pysqlite3
    sys.modules["sqlite3"] = sys.modules.pop("pysqlite3")
except Exception as e:
    print("Could not patch sqlite3 with pysqlite3:", e)
