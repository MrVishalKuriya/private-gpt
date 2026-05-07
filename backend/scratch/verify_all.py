import asyncio
import os
import sys
import boto3
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env"))

async def verify():
    print("🚀 Starting PrivateGPT System Verification...\n")

    # 1. Database Check
    try:
        from app.db.session import AsyncSessionLocal
        from sqlalchemy import select
        from app.models.user import User
        async with AsyncSessionLocal() as db:
            await db.execute(select(User).limit(1))
        print("✅ PostgreSQL: Connected successfully.")
    except Exception as e:
        print(f"❌ PostgreSQL: Failed! Error: {e}")

    # 2. Redis Check
    try:
        from redis import Redis
        from app.core.config import settings
        redis = Redis.from_url(settings.REDIS_URL)
        redis.ping()
        print("✅ Redis: Connected successfully.")
    except Exception as e:
        print(f"❌ Redis: Failed! (Check if local Redis is running or if Render URL is public) Error: {e}")

    # 3. Neo4j Check
    try:
        from app.db.neo4j import get_neo4j_session
        async with get_neo4j_session() as session:
            await session.run("RETURN 1")
        print("✅ Neo4j: Connected successfully.")
    except Exception as e:
        print(f"❌ Neo4j: Failed! Error: {e}")

    # 4. AWS Bedrock Check
    try:
        client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
        # Use a very cheap model for connectivity test
        client.converse(
            modelId="amazon.titan-text-lite-v1",
            messages=[{"role": "user", "content": [{"text": "ping"}]}]
        )
        print("✅ AWS Bedrock: Connection and Credentials verified.")
        print("⚠️  Note: Claude models still require 'Model Access' in the AWS Console.")
    except Exception as e:
        if "ResourceNotFoundException" in str(e) or "AccessDeniedException" in str(e):
             print("✅ AWS Bedrock: Connection successful, but Model Access is required in Console.")
        else:
             print(f"❌ AWS Bedrock: Credential Error! {e}")

    print("\n✨ Verification Complete!")

if __name__ == "__main__":
    asyncio.run(verify())
