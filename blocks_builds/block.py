class Blocks_class:
    def success_block_preview(self, **kwargs):

        # feed_subtext, feed_link, feed_title, feed_summary, feed_entry_link
        block = [
            {"type": "divider"},
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*Feed Summary*\n\n> {kwargs['feed_subtext']}\n\n*<{kwargs['feed_entry_link']}|Last post>*\n\n>>> {kwargs['feed_summary']}",
                },
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": f"<{kwargs['feed_link']}|*Feed*>: {kwargs['feed_title']}",
                    }
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
                        "action_id": kwargs["feed_link"],
                    },
                    {
                        "type": "button",
                        "text": {"type": "plain_text", "text": "Cancel"},
                        "value": "cancel",
                    },
                ],
            },
        ]
        return block
