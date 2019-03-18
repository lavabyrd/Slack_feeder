successful_add_block = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Pick an item from the dropdown list"
        },
        "accessory": {
            "type": "static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Pick an option",
                "emoji": true
            },
            "options": [
                {
                    "text": {
                        "type": "plain_text",
                        "text": "Add Feed",
                        "emoji": true
                    },
                    "value": "add_rss_feed"
                },
                {
                    "text": {
                        "type": "plain_text",
                        "text": "Cancel",
                        "emoji": true
                    },
                    "value": "cancel"
                }
            ]
        }
]