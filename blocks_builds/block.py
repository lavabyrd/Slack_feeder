success_block = [
    {
        "type": "section",
        "block_id": "add_decline",
        "text": {"type": "mrkdwn", "text": "Pick an item from the dropdown list"},
        "accessory": {
            "type": "static_select",
            "placeholder": {"type": "plain_text", "text": "Pick an option"},
            "options": [
                {
                    "text": {"type": "plain_text", "text": "Add Feed"},
                    "value": "add_rss_feed",
                },
                {"text": {"type": "plain_text", "text": "Cancel"}, "value": "cancel"},
            ],
        },
    }
]

success_block_preview = [
    {"type": "divider"},
    {
        "type": "section",
        "text": {"type": "mrkdwn", "text": "Pick an item from the dropdown list"},
    },
    {
        "type": "context",
        "elements": [{"type": "mrkdwn", "text": "*Feed Link:* T. M. Schwartz"}],
    },
    {"type": "divider"},
    {
        "type": "actions",
        "block_id": "add_decline",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Add"},
                "value": "add_rss_feed",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Cancel"},
                "value": "cancel",
            },
        ],
    },
]
