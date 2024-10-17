import json
import logging

# Set up logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda function to process GitHub Webhook events
    """
    try:
        # Log the incoming event
        logger.info(f"Received event: {json.dumps(event)}")

        # Extract relevant GitHub event data
        github_event = event.get("headers", {}).get("X-GitHub-Event", None)
        if github_event == "pull_request":
            # Handle pull request event
            body = json.loads(event["body"])
            action = body.get("action")
            pull_request = body.get("pull_request", {})
            pr_title = pull_request.get("title")
            pr_url = pull_request.get("html_url")

            logger.info(f"Pull Request Action: {action}")
            logger.info(f"PR Title: {pr_title}")
            logger.info(f"PR URL: {pr_url}")

            # Add your logic here (e.g., notify someone, trigger other workflows, etc.)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Webhook processed successfully",
                "event": github_event
            })
        }

    except Exception as e:
        logger.error(f"Error processing event: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Error processing webhook"})
        }

