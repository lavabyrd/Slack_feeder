success_block = [
    {
        "type":"section",
        "text":{
            "type":"mrkdwn",
            "text":"Pick an item from the dropdown list"
        },
        "accessory":{
            "type":"static_select",
            "placeholder":{
                "type":"plain_text",
                "text":"Pick an option"
                
            },
            "options":[
                {
                    "text":{
                        "type":"plain_text",
                        "text":"Add Feed"
                        
                    },
                    "value":"add_rss_feed"
                },
                {
                    "text":{
                        "type":"plain_text",
                        "text":"Cancel"
                        
                    },
                    "value":"cancel"
                }
            ]
        }
    }
]