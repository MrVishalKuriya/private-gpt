import asyncio
from app.db.session import AsyncSessionLocal
from app.models.user import User, RoleEnum
from app.core.security import get_password_hash
from sqlalchemy.future import select

async def create_admin():
    async with AsyncSessionLocal() as db:
        try:
            # Check if admin already exists
            result = await db.execute(select(User).filter(User.email == "admin@regenesys.com"))
            user = result.scalars().first()
            
            if user:
                print("Admin user already exists. Updating password...")
                user.password_hash = get_password_hash("admin123")
                user.is_verified = True
                user.role = RoleEnum.admin
            else:
                print("Creating admin user...")
                user = User(
                    email="admin@regenesys.com",
                    password_hash=get_password_hash("admin123"),
                    is_verified=True,
                    is_active=True,
                    role=RoleEnum.admin
                )
                db.add(user)
            
            await db.commit()
            print("✅ Admin user setup successful!")
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(create_admin())
