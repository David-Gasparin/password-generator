class PasswordEvaluator:
    def evaluate(self, password):
        password_safety = password.get_safety()
        password_base_length = password.get_base_length()
        if password_safety == 3 and password_base_length >= 20:
            return 'high security'
        elif password_safety >= 2 and password_base_length >= 12:
            return 'medium security'
        return "low security"

