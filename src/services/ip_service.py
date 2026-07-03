import requests
def request_json(url):

    try:

        response = requests.get(url, timeout=10)

        if response.status_code == 200:

            return response.json()

    except Exception:

        pass

    return None


def ip_scan(ip):

    url = f"https://ipinfo.io/{ip}/json"

    response = requests.get(url, timeout=10)
    print(response.status_code)
    print(response.text)
    data = response.json()

    return {
        "target": ip,
        "scan_type": "IP Intelligence",
        "status": "Completed Successfully",
        "ip": data.get("ip"),
        "city": data.get("city"),
        "region": data.get("region"),
        "country": data.get("country"),
        "org": data.get("org"),
        "timezone": data.get("timezone"),
        "latitude": data.get("loc", "").split(",")[0] if data.get("loc") else None,
        "longitude": data.get("loc", "").split(",")[1] if data.get("loc") else None,
        
    }