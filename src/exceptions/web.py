
class PageNotFoundError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TokenNoneError(Exception):
    def __init__(self):
        self.message = 'token is none.'
        super().__init__(self.message)

class AuthenticationError(Exception):
    def __init__(self):
        self.message = 'failed during authentication'
        super().__init__(self.message)