import passwordeval
import secrets
import string

class PasswordGen:
    def generate_password(self, base_length, safety):

        if safety == 1:
            chars = string.ascii_letters
        elif safety == 2:
            chars = string.ascii_letters + string.digits
        elif safety == 3:
            chars = string.ascii_letters + string.digits + string.punctuation
        else:
            return None

        password = ''.join(secrets.choice(chars) for _ in range(base_length))
        return password

class Password:
    def __init__(self, base_length, safety):
        self.base_length = base_length
        self.safety = safety
        self.password = None
        self.status = None

    def new_password(self):
        passwordgen = PasswordGen()
        self.password = passwordgen.generate_password(self.base_length, self.safety)
        self.status = passwordeval.PasswordEvaluator().evaluate(self)

    def get_password(self):
        return self.password

    def get_status(self):
        return self.status

    def get_safety(self):
        return self.safety

    def set_password(self, password):
        self.password = password

    def get_base_length(self):
        return self.base_length

    @staticmethod
    def create_password(input):
        safety = 0
        base_length = len(input)
        if any(c in string.ascii_letters for c in input):
            safety += 1
        if any(c in string.digits for c in input):
            safety += 1
        if any(c in string.punctuation for c in input):
            safety += 1
        password = Password(base_length, safety)
        password.status = passwordeval.PasswordEvaluator().evaluate(password)
        password.set_password(input)
        return password


