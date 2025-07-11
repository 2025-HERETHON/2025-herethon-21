class CACHE_KEY:
    def __init__(self, username=None):
        self.EXERCISE_ROUTINE = f'exercise_routine_{username}'
        self.EXERCISE_HISTORY_ID = f'exercise_history_id_{username}'
        
class CACHE_KEY_SIGNUP:
    def __init__(self, username=None):
        self.SIGNUP_EMAIL = f'signup_email_{username}'
        self.SIGNUP_PW1 = f'signup_pw1_{username}'
        self.SIGNUP_PW2 = f'signup_pw2_{username}'