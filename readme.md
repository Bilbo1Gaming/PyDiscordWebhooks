# Simple Discord Webhooks

A simple Discord webhook solution

Feel free to use this anywhere!

## Features:
 - Very Simple
 - Custom Usernames Per Instance
 - Success messages
 - Error messages
 - Log messages

## Example:
```python
from simpleDiscordWebhooks import webhookController

logger = webhookController("DISCORD WEBHOOK URL", "TEST LOGGER")

logger.success("Success", "Message")
logger.log("Log", "Message")
logger.error("Error", "Message")
```

## Changelog (if I every update this):
### V1.0
 - Custom Usernames Per Instance
 - Success messages
 - Error messages
 - Log messages