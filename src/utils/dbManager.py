import json
import os, errno

DB = "./db/ids.json"

def mkdir_p(path):
    try:
        os.makedirs(path, exist_ok=True)  # Python>3.2
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

def __createDB():
    """Create a new database file"""
    mkdir_p("./db")
    with open(DB, "w") as f:
        json.dump({}, f)

def addID(HiveID: str, DiscordID: int) -> int:
    """Add a new ID to the database

    Args:
        HiveID (str): Hive ID
        DiscordID (int): Discord ID

    Returns:
        int: Success or error code

    Codes:
        200: ID successfully added
        409: ID already exists
    """
    try:
        with open(DB, "r") as f:
            db: dict = json.load(f)
    except FileNotFoundError:
        __createDB()
        with open(DB, "r") as f:
            db: dict = json.load(f)
    
    if HiveID in db:
        return 409
    db[HiveID] = DiscordID

    with open(DB, "w") as f:
        json.dump(db, f, indent=4)

    return 200

def removeID(HiveID: str, DiscordID: int) -> int:
    """Remove an ID from the database

    Args:
        HiveID (str): Hive ID
        DiscordID (int): Discord ID

    Returns:
        int: Success or error code

    Codes:
        200: ID successfully removed
        401: Unauthorized (Discord ID did not register the Hive ID)
        404: ID not found
        500: No registered IDs
    """
    try:
        with open(DB, "r") as f:
            db: dict = json.load(f)
    except FileNotFoundError:
        return 500
    
    try:
        if db[HiveID] != DiscordID:
            return 401
        del db[HiveID]
    except KeyError:
        return 404
    
    with open(DB, "w") as f:
        json.dump(db, f, indent=4)

    return 200