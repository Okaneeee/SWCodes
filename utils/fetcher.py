import requests

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
        Tuple[int, dict]: Status code and response json \n
        (int, {"retCode": int|str, "retMsg": str})

    retCodes:
        100 - success
        (H304) - already used (str)
        (H306) - invalid code (str)
        404 - URL not found (custom)
        503 - invalid id

    retMsg:
        Separator = br
    """
    try:
        body = f"country=US&lang=en&server=europe&hiveid={id}&coupon={code}"
        response = requests.post(URL, headers=HEADERS, data=body)
        return response.status_code, response.json()
    except Exception as e:
        return 404, {"retCode": 404, "retMsg": "URL not found"}