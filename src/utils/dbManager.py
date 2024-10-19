import json

DB = "./db/ids.json"

def __createDB():
    """Create a new database file"""
    with open(DB, "w") as f:
        json.dump({}, f)

def addID(HiveID: str, DiscordID: int) -> str:
    """Add a new ID to the database

    Args:
        HiveID (str): Hive ID
        DiscordID (int): Discord ID

    Returns:
        str: Success message
    """
    try:
        with open(DB, "r") as f:
            db: dict = json.load(f)
    except FileNotFoundError:
        __createDB()
        with open(DB, "r") as f:
            db: dict = json.load(f)
    
    db[HiveID] = DiscordID

    with open(DB, "w") as f:
        json.dump(db, f, indent=4)

    return "ID successfully added"

def removeID(HiveID: str) -> str:
    """Remove an ID from the database

    Args:
        HiveID (str): Hive ID

    Returns:
        str: Success or error message
    """
    try:
        with open(DB, "r") as f:
            db: dict = json.load(f)
    except FileNotFoundError:
        return "Error: no registered IDs"
    
    try:
        del db[HiveID]
    except KeyError:
        return "Error: ID not found"
    
    with open(DB, "w") as f:
        json.dump(db, f, indent=4)

    return "ID successfully removed"