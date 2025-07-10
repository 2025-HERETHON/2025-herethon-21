class ClientError(Exception):
    def __init__(self, status_code:int, status_title:str, message:str):
        super().__init__(status_code, status_title, message)
        self.status_code = status_code
        self.status_title = status_title
        self.message = message