import os
import json
import uuid
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


SERVICE_NAME = 'DEMO SERVERLESS PROJECT 1'
_STARTUP_IDENTIFIER = uuid.uuid4()


def lambda_handler(event, context):
    msg = f'Hello {event["path"]} from {_STARTUP_IDENTIFIER} ({SERVICE_NAME}) {os.environ}'
    logger.info(msg)
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        'body': json.dumps(msg),
    }
