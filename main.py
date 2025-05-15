import requests
from msal import ConfidentialClientApplication
import teams_webhook as teams

# 設定變數：請填上你自己的資料
client_id = "app client id"
client_secret = 'client secrect'
tenant_id = 'tenant id'

# MSAL 設定
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
    print("❌ 無法取得 access token")
    exit()

# 設定 headers
headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# 呼叫 Microsoft Graph API - 查詢已停用帳戶
url = "https://graph.microsoft.com/v1.0/users?$filter=accountEnabled eq false"
response = requests.get(url, headers=headers)

license_url = "https://graph.microsoft.com/v1.0/subscribedSkus"
license_response = requests.get(license_url, headers=headers)
license = license_response.json().get("value", [])
#all_sku_name = ""
#all_sku_ids = [entry['skuId'] for entry in license]
#print(all_sku_ids.count("6fd2c87f-b296-42f0-b197-1e91e994b900"))

if response.status_code != 200:
    print(f"❌ 查詢失敗: {response.status_code}")
    print(response.text)
    exit()

users = response.json().get("value", [])

#print(f"🔎 找到 {len(users)} 個停用帳號：\n")
user_disable = [{
      "type": "TextBlock",
      "text": "This Week Account Disabled",
      "wrap": True,
      "weight": "Bolder",
      "size": "Large",
      "color": "Accent"
    }]

index = 0
# 檢查每個使用者是否有 license
for user in users:
    upn = user.get("userPrincipalName", "N/A")
    display_name = user.get("displayName", "N/A")
    user_id = user.get("id")

    #print(f"🧑‍💼 {display_name} ({upn})")

    # 查詢 license 狀態
    license_url = f"https://graph.microsoft.com/v1.0/users/{user_id}/licenseDetails"
    license_response = requests.get(license_url, headers=headers)
    if license_response.status_code == 200:
        license_data = license_response.json().get("value", [])
        sku_info = [entry['skuPartNumber'] for entry in license_data]
        if license_data:
            #print(sku_info)
            license_text = "\n".join(f"- {license}" for license in sku_info)
            #adaptive_card_single = teams.Adaptive_Card_Single(upn, user_id, license_text)
            #data = requests.post(teams.Teams_Post(),json = adaptive_card_single)
            index = index + 1
            user_container = {
                                "type": "Container",
                                "separator": index > 0,  # 從第2筆開始加分隔線
                                "items": [
                                {
                                    "type": "TextBlock",
                                    "text": "⚠️ 使用者帳號停用通知",
                                    "wrap": True,
                                    "weight": "Bolder",
                                    "size": "Medium",                                       
                                    "color": "Attention"
                                },
                                {
                                    "type": "FactSet",
                                    "facts": [
                                                {"title": "帳號:", "value": upn},
                                                {"title": "狀態:", "value": "🔒 Disabled"}
                                    ]
                                },                                    
                                {
                                    "type": "TextBlock",
                                    "text": "📌 **仍授予的授權**",
                                    "wrap": True,
                                    "weight": "Bolder",
                                    "spacing": "Small"
                                },
                                {
                                    "type": "FactSet",
                                    "facts": [
                                    {"title": "•", "value": license} for license in sku_info]
                                }
                                ]
                            } 
            user_disable.append(user_container)

#adaptive_card_json = json.dumps(user_disable, ensure_ascii=False, indent=2)
data = requests.post(teams.Teams_Post(), json= teams.adaptive_card(user_disable))
print(data.status_code)