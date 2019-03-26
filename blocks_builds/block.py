class Blocks_class:
    def success_block_preview(
        self, feed_subtext, feed_link, feed_title, feed_summary, feed_entry_link
    ):
        return [
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Feed Summary*\n\n> {feed_subtext}\n\n*<{feed_entry_link}|Last post>*\n\n>>> {feed_summary} ",
                },
            },
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f"<{feed_link}|*Feed*>: {feed_title}"}
                ],
            },
            {"type": "divider"},
            {
                "type": "actions",
                "block_id": "add_decline",
                "elements": [
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Subscribe"},
                        "value": "add_rss_feed",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Cancel"},
                        "value": "cancel",
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Preview"},
                        "value": feed_url,
                    },
                ],
            },
        ]
