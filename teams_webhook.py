def Teams_Post():
    return "Webhook_url"

#multiple adaptive card  
def adaptive_card (body: dict):
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
                    "body": body,
                    "actions": [
                        {
                            "type": "Action.OpenUrl",
                            "title": "View Account Status",
                            "url": "https://admin.microsoft.com/#/users"
                        }
                    ]
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