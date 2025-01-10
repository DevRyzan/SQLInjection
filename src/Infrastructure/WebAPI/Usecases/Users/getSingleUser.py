from src.Infrastructure.WebAPI.Repos.UserRepository import UserRepository

class GetSingleUserUseCase:
    def __init__(self):
        self.user_repository = UserRepository()
        pass

    def execute(self, user_id: int):
        
        try:
            return self.user_repository.find_by_id(user_id)
        except ValueError as e:
            raise e("No user with this id found")
        except Exception as e:
            print(f"Unexpected error: {e}")