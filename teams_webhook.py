def Teams_Post():
    return "Webhook_URL"

#multiple adaptive card  
def adaptive_card (body: dict, user_count: int):
    return {
                "type":"message",
                "attachments":[
                {
                    "contentType":"application/vnd.microsoft.card.adaptive",
                    "contentUrl":"",
                    "content":{
                    "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
                    "type":"AdaptiveCard",
                    "version":"1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": "🚨 Account Disable Notification Total: " + str(user_count),
                            "wrap": True,
                            "weight": "Bolder",
                            "size": "Large",
                            "color": "Attention",
                            "separator": True
                        },
                        *body  # expend user_disable list card block
                    ],
                    }
                }
                ]
    }


#single adaptive card
def Adaptive_Card_Single(upn: str, user_id: str, license: str ):
    return  {
                "type":"message",
                "attachments":[
                {
                    "contentType":"application/vnd.microsoft.card.adaptive",
                    "contentUrl":"",
                    "content":{
                    "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
                    "type":"AdaptiveCard",
                    "version":"1.2",
                    "body": [
                        {
                            "type": "TextBlock",
                            "text": "⚠️ Account Disable Notification",
                            "wrap": True,
                            "weight": "Bolder",
                            "size": "Large",
                            "color": "Attention"
                        },
                        {
                            "type": "FactSet",
                            "facts": [
                            {
                                "title": "Account:",
                                "value": upn
                            },
                            {
                                "title": "Status:",
                                "value": "🔒 Disabled"
                            }
                            ]         
                        },
                        {
                            "type": "TextBlock",
                            "text": "📌 ** Have License**",
                            "wrap": True,
                            "weight": "Bolder",
                            "spacing": "Medium"
                        },
                        {
                            "type": "TextBlock",
                            "text": license,
                            "wrap": True,
                            "weight": "Bolder"
                        }
                    ],
                    "actions": [
                        {
                            "type": "Action.OpenUrl",
                            "title": "View Account Status",
                            "url": f"https://admin.microsoft.com/#/users/:/UserDetails/{user_id}/LicensesAndApps"
                        }
                    ]
                }
            }
        ]
    }

def target_sku_part():
    return [
        "STANDARDPACK","ENTERPRISEPACK", "SPE_E3", "SPE_E5"
    ]

def LICENSE_NAME_MAP():
    return {
    "STANDARDPACK": "Office 365 E1",
    "ENTERPRISEPACK": "Office 365 E3",
    "SPE_E3": "Microsoft 365 E3",
    "SPE_E5": "Microsoft 365 E3",
}
