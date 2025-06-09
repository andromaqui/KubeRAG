class UserNotFoundError(Exception):
    def __init__(self, user_id: int):
        self.user_id = user_id
        self.message = f"No user found with ID {user_id}"
        super().__init__(self.message)

class InternalServerError(Exception):
    def __init__(self):
        self.message = f"An unknown error occured while trying to complete this operation"
        super().__init__(self.message)
