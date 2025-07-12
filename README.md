# Meraki API Automation with Postman

This project demonstrates the use of the Cisco Meraki Dashboard API using Postman collections and (optionally) automation scripts.

## 🚀 What’s Included

- ✅ Collection to:
  - List organizations
  - List networks per organization
  - Get connected clients and devices
  - Change switch port configurations
- ✅ Uses collection/environment variables for `api_key`, `org_id`, and `network_id`
- ✅ Ready for export to CSV or scripting extensions

## 📂 Files

| File | Description |
|------|-------------|
| `meraki-api-collection.postman_collection.json` | Main Postman collection |
| `postman_environment_template.json` | Example Postman environment (API key redacted) |
| `sample-output.json` | Example output from API requests |
| `scripts/` | (Optional) Python/Node scripts to run requests |

## 🛠️ How to Use

1. 🔑 [Get your Meraki API key](https://documentation.meraki.com/General_Administration/Other_Topics/Cisco_Meraki_Dashboard_API)
2. 🧪 Import the collection into Postman:
    - File → Import → Select `meraki-api-collection.postman_collection.json`
3. Set your environment variable `api_key` with your Meraki Dashboard API key.
4. Use `GET https://api.meraki.com/api/v1/organizations` to list your accessible orgs.
5. Fill in the `org_id` from the response, and use it to access networks, clients, and devices.

## 📸 Screenshots

![Request in Postman](screenshots/get-devices.png)

## 🌐 Optional: Postman Public Link

> You can also view and use this collection from Postman’s public workspace (no login required):

[🔗 View in Postman](https://www.postman.com/your-public-workspace-link)

## 🧠 Learning Outcomes

- Understand RESTful interaction with Cisco Meraki APIs
- Practice secure API key handling with Postman variables
- Automate network visibility, reporting, and config changes

## 🧱 Built With

- [Postman](https://www.postman.com/)
- Cisco Meraki Dashboard API v1

## 📜 License

MIT — free to use for learning or portfolio purposes.


