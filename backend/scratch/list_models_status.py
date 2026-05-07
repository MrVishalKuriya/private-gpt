import boto3
import os
from dotenv import load_dotenv

load_dotenv()

session = boto3.Session(
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=os.getenv("AWS_REGION", "us-east-1")
)

client = session.client("bedrock")

try:
    models = client.list_foundation_models()
    claude_models = [
        m for m in models["modelSummaries"] 
        if "anthropic.claude" in m["modelId"]
    ]
    print(f"{'Model ID':<50} | {'Status':<15}")
    print("-" * 70)
    for m in claude_models:
        # Some older boto3 versions might not have 'modelStatus' in summary
        status = m.get("modelStatus", "Unknown")
        print(f"{m['modelId']:<50} | {status:<15}")
except Exception as e:
    print(f"Error: {e}")
