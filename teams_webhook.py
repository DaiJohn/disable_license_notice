def Teams_Post():
    return "Webhook_URL"

def Adaptive_Card_Mulit_Region (body: dict, user_count: int, region: str, time: str):
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
                            "text": "📅 " + time,
                            "wrap": True,
                            "weight": "Bolder",
                            "size": "Large",
                            "color": "Attention",
                            "separator": False
                        },
                        {
                            "type": "TextBlock",
                            "text": "🚨 Account Disable Notification Total: " + str(user_count),
                            "wrap": True,
                            "weight": "Bolder",
                            "size": "Large",
                            "color": "Attention",
                            "separator": False
                        },
                        {
                            "type": "TextBlock",
                            "text": "🏙️ Region: " + region,
                            "wrap": True,
                            "weight": "Bolder",
                            "size": "Large",
                            "color": "Attention",
                            "separator": False
                        },
                        *body  # expend user_disable card block
                    ],
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
