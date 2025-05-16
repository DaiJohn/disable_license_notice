import concurrent.futures
import requests
from msal import ConfidentialClientApplication
import teams_webhook as teams
from dotenv import load_dotenv
import os

load_dotenv()

tenant_id = os.getenv('tenant_id')
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

# MSAL setting
authority = f"https://login.microsoftonline.com/{tenant_id}"
scope = ["https://graph.microsoft.com/.default"]

app = ConfidentialClientApplication(
    client_id=client_id,
    client_credential=client_secret,
    authority=authority
)

token_response = app.acquire_token_for_client(scopes=scope)
access_token = token_response.get("access_token")

if not access_token:
    print("❌ Can't get access token")
    exit()

# Setting headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

def fetch_license(user):
    user_id = user.get("id")
    upn = user.get("userPrincipalName", "N/A")
    display_name = user.get("displayName", "N/A")

    license_url = f"https://graph.microsoft.com/v1.0/users/{user_id}/licenseDetails"
    license_response = requests.get(license_url, headers=headers)

    if license_response.status_code == 200:
        license_data = license_response.json().get("value", [])
        sku_info = [entry['skuPartNumber'] for entry in license_data]
        if any(license in teams.target_sku_part() for license in sku_info):
            return {
                "type": "Container",
                "separator": True,
                "items": [
                    #{
                    #    "type": "TextBlock",
                    #    "text": "⚠️ Account Disable Notification",
                    #    "wrap": True,
                    #    "weight": "Bolder",
                    #    "size": "Medium",                                       
                    #    "color": "Attention"
                    #},
                    {
                        "type": "FactSet",
                        "facts": [
                            {"title": "Account:", "value": f"{display_name} ({upn})"},
                            {"title": "Status:", "value": "🔒 Disabled"}
                        ]
                    },
                    {
                        "type": "TextBlock",
                        "text": "📌 **Granted authorization**",
                        "wrap": True,
                        "weight": "Bolder",
                        "spacing": "Small"
                    },
                    {
                        "type": "FactSet",
                        "facts": [
                            {
                                "title": "•",
                                "value": teams.LICENSE_NAME_MAP().get(license, license)
                            }
                            for license in sku_info
                            if license in teams.target_sku_part()
                        ]
                    }
                ]
            }
    return None

url = "https://graph.microsoft.com/v1.0/users?$filter=accountEnabled eq false"
#response = requests.get(url, headers=headers)
while url:
    response = requests.get(url, headers=headers)
    data = response.json()

    all_users.extend(data.get("value", []))

    # Check have more info
    url = data.get("@odata.nextLink", None)

# Retrieve license information for all accounts in parallel
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_license, all_users))

# Filter None result
user_disable = [r for r in results if r]
print(user_disable, len(user_disable))
data = requests.post(teams.Teams_Post(), json= teams.adaptive_card(user_disable, len(user_disable)))
print(data.status_code)
