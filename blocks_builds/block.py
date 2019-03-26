class Blocks_class:
    def success_block_preview(self, feed_text, feed_link):
        return [
            {"type": "divider"},
            {"type": "section", "text": {"type": "mrkdwn", "text": f"{feed_text}"}},
            {
                "type": "context",
                "elements": [
                    {"type": "mrkdwn", "text": f"<{feed_link}|*Feed*>: T. M. Schwartz"}
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
                ],
            },
        ]
