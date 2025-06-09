class InternalServerError(Exception):
    def __init__(self):
        self.message = f"An unknown error occured while trying to complete this operation"
        super().__init__(self.message)

class BadRequestError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
