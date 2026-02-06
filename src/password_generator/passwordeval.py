class PasswordEvaluator:
    def evaluate(self, password):
        """Setzt den sicherheitsstatus des pwds."""
        password_safety = password.get_safety()
        password_base_length = password.get_base_length()
        if password_safety == 3 and password_base_length >= 20:
            password.set_status('high security')
        elif password_safety >= 2 and password_base_length >= 12:
            password.set_status('medium security')
        else: password.set_status('low security')

