import passwordeval
import secrets
import string

class PasswordGen:
    """Erzeugt zufällige Passwörter basierend auf Länge und Sicherheitsstufe."""
    def generate_password(self, base_length, safety):
        """
        Generiert ein zufälliges Passwort basierend auf der angegebenen
        Basislänge und Sicherheitsstufe.

        Sicherheitsstufen:
        1 = nur Buchstaben
        2 = Buchstaben und Ziffern
        3 = Buchstaben, Ziffern und Sonderzeichen

        :param base_length: Gewünschte Länge des Passworts
        :param safety: Sicherheitsstufe (1–3)
        :return: Generiertes Passwort als String oder None bei ungültigen Parametern
        """
        if safety == 1 and base_length >= 1:
            password_chars = []
            chars = string.ascii_letters
            for i in range(base_length):
                password_chars.append(secrets.choice(chars))
        elif safety == 2 and base_length >= 2:
            chars_letters = string.ascii_letters
            chars_digits = string.digits
            all_chars = chars_letters + chars_digits
            password_chars = [secrets.choice(chars_letters), secrets.choice(chars_digits)]
            for i in range(base_length-2):
                password_chars.append([secrets.choice(all_chars)])
            secrets.SystemRandom().shuffle(password_chars)
        elif safety == 3 and base_length >= 3:
            chars_letters = string.ascii_letters
            chars_digits = string.digits
            chars_punctuation = string.punctuation
            all_chars = chars_letters + chars_digits + chars_punctuation
            password_chars = [secrets.choice(chars_letters), secrets.choice(chars_digits), secrets.choice(chars_punctuation)]
            for i in range(base_length-3):
                password_chars.append(secrets.choice(all_chars))
            secrets.SystemRandom().shuffle(password_chars)
        else:
            return None
        return ''.join(password_chars)

class Password:
    """Repräsentiert ein Passwort inklusive Sicherheitsbewertung."""
    __passwordgen = PasswordGen()
    __evaluator = passwordeval.PasswordEvaluator()

    def __init__(self, base_length, safety):
        """
        Erstellt ein neues Password-Objekt und generiert automatisch
        ein Passwort mit anschließender Bewertung.

        :param base_length: Länge des Passworts
        :param safety: Sicherheitsstufe (1–3)
        """
        self.status = None
        self.base_length = base_length
        self.safety = safety
        self.password = Password.__passwordgen.generate_password(self.base_length, self.safety)
        Password.__evaluator.evaluate(self)

    def new_password(self):
        """
        Generiert ein neues Passwort mit den bestehenden
        Längen- und Sicherheitseinstellungen und bewertet es neu.
        """
        self.password = Password.__passwordgen.generate_password(self.base_length, self.safety)
        Password.__evaluator.evaluate(self)

    def get_password(self):
        return self.password

    def set_status(self, status):
        self.status = status

    def get_status(self):
        return self.status

    def get_safety(self):
        return self.safety

    def set_password(self, password):
        self.password = password

    def get_base_length(self):
        return self.base_length

    @staticmethod
    def create_password(pwd):
        """
        Erstellt aus einem vom Benutzer eingegebenen Passwort
        ein vollständiges Password-Objekt inklusive Sicherheitsbewertung.

        Die Sicherheitsstufe wird anhand der enthaltenen Zeichentypen
        (Buchstaben, Ziffern, Sonderzeichen) ermittelt.

        :param pwd: Vom Benutzer eingegebenes Passwort
        :return: Password-Objekt
        """
        safety = 0
        base_length = len(pwd)
        if any(c in string.ascii_letters for c in pwd):
            safety += 1
        if any(c in string.digits for c in pwd):
            safety += 1
        if any(c in string.punctuation for c in pwd):
            safety += 1
        password = Password(base_length, safety)
        password.status = passwordeval.PasswordEvaluator().evaluate(password)
        password.set_password(pwd)
        return password


