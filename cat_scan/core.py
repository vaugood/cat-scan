import requests

def get_document(url:str) -> str:
    try:
        res = requests.get(url, timeout=2)
        print(f"Fetched {url}")
        return res.text
    except requests.ReadTimeout:
        print(f"Read Timeout {url}")
        return None
    except Exception as e:
        print(e)
        return None
