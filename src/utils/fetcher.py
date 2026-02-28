import requests
from requests.exceptions import HTTPError
import json
from utils.logger import Logger

LOGGER = Logger()

URL = "https://event.withhive.com/ci/smon/evt_coupon/useCoupon"

HEADERS = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "en-US,en;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "pragma": "no-cache",
    "sec-ch-ua": "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    "Referer": "https://event.withhive.com/ci/smon/evt_coupon",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

def fetch(id: str, code: str):
    """Make a request to use a coupon code

    Args:
        id (str): Hive ID
        code (str): Coupon code

    Returns:
        Tuple[int, str]: Status code and response \n
        (int, {"retCode": int|str, "retMsg": str})

    retCodes:
        100 - success
        302 - invalid code (changed from (H302) - str)
        304 - already used (changed from (H304) - str)
        305 - invalid code
        306 - invalid code (changed from (H306) - str)
        404 - URL not found (custom)
        503 - invalid HiveID
    """
    try:
        body = f"country=US&lang=en&server=europe&hiveid={id}&coupon={code}"
        response = requests.post(URL, headers=HEADERS, data=body)
        rJson = response.json()
        
        # Removing (H) from retCode
        if type(rJson["retCode"]) == str: # Avoid error if retCode is int
            rJson["retCode"] = rJson["retCode"].translate(str.maketrans({"(": "", ")": "", "H": ""}))

        retCode = int(rJson["retCode"])

        if retCode == 302 or retCode == 306:
            return retCode, "Invalid code, it might be expired, invalid or usage limit reached"
        elif retCode == 304:
            return retCode, "already used the code."
        elif retCode == 305:
            return retCode, "Invalid code, please check again."
        elif retCode == 503:
            return retCode, "has registered an invalid Hive ID."
        elif retCode == 100:
            return retCode, "successfully used the code."
        else:
            LOGGER.log(f"Unknown retCode: {retCode} with message: {rJson['retMsg']}", "ERROR")
            return 500, "Unknown error, contact the developer"
    except HTTPError as http_err:
        LOGGER.log(f"HTTP error occurred: {http_err}", "ERROR")
        return 404, "URL not found, contact the developer"
    except Exception as e:
        LOGGER.log(f"An error occurred: {e}", "ERROR")
        return 500, "Unknown error, contact the developer"


DB = "./db/ids.json"

def multiFetch(code: str) -> tuple:
    """Make a request to use a coupon code for multiple users

    Args:
        code (str): Coupon code

    Returns:
        dict: {id: (status code, response json)}
    """
    try:
        with open(DB, "r") as f: 
            db: dict = json.load(f)
    except FileNotFoundError:
        return 404, "No IDs found, please register at least one ID first."
    
    ids = list(db.keys())

    errors = []
    noErrors: int = 0
    for id in ids:
        rCode, resp = fetch(id, code)
        if rCode in [302, 305, 306, 404, 500]:
            return rCode, resp
        elif rCode in [304, 503]:
            errors.append(f"{db[id]} {resp}")
        elif rCode == 100:
            noErrors += 1
        else:
            errors.append(f"{db[id]} has encountered an unknown error.")

    response = noErrors
    if errors:
        return response, errors
    return response, None