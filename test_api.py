import requests

BASE = "http://localhost:8000"

def test_health():
    r = requests.get(BASE + "/docs")
    assert r.status_code == 200

if __name__ == "__main__":
    test_health()
    print("✅ API is reachable")
