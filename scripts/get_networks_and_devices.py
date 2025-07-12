import requests
import json
import os

# ---------------------------------------
# SETUP
# ---------------------------------------

# Load your API key securely from env var
API_KEY = os.getenv("MERAKI_API_KEY")

if not API_KEY:
    raise Exception("Please set the MERAKI_API_KEY environment variable.")

BASE_URL = "https://api.meraki.com/api/v1"
HEADERS = {
    "X-Cisco-Meraki-API-Key": API_KEY,
    "Content-Type": "application/json"
}

# ---------------------------------------
# FUNCTIONS
# ---------------------------------------

def get_organizations():
    url = f"{BASE_URL}/organizations"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_networks(org_id):
    url = f"{BASE_URL}/organizations/{org_id}/networks"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def get_devices(network_id):
    url = f"{BASE_URL}/networks/{network_id}/devices"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json()

# ---------------------------------------
# MAIN
# ---------------------------------------

def main():
    print("📡 Fetching organizations...")
    orgs = get_organizations()
    if not orgs:
        print("❌ No organizations found.")
        return

    # Just use the first org for now
    org_id = orgs[0]["id"]
    org_name = orgs[0]["name"]
    print(f"✅ Found org: {org_name} (ID: {org_id})")

    print("🔍 Fetching networks...")
    networks = get_networks(org_id)

    for net in networks:
        print(f"\n🌐 Network: {net['name']} ({net['id']})")

        devices = get_devices(net["id"])
        if not devices:
            print("  ⚠️  No devices found.")
            continue

        for device in devices:
            print(f"  📦 {device.get('name', 'Unnamed')} | {device['model']} | Serial: {device['serial']}")

if __name__ == "__main__":
    main()
