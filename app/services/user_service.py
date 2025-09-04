from schemas.user_schema import UserAuth
from models.user_model import User
from core.security import get_password

class UserService:
    @staticmethod
    async def create_user(user_auth: UserAuth):
        user = User(
            username=user_auth.username,
            email=user_auth.email,
            hash_password=get_password(user_auth.password)
        )
        await user.save()
        return user