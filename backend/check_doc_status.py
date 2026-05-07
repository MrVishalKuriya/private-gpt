import asyncio
import os
import sys
from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.models.document import Document

async def check_docs():
    async with AsyncSessionLocal() as db:
        result = await db.execute(select(Document))
        docs = result.scalars().all()
        print(f"{'ID':<40} | {'Status':<15} | {'Name':<30}")
        print("-" * 90)
        for d in docs:
            print(f"{str(d.id):<40} | {d.processing_status:<15} | {d.original_name:<30}")

if __name__ == "__main__":
    asyncio.run(check_docs())
