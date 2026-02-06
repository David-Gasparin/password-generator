class PasswordEvaluator:
    """Bewertet die Sicherheit eines Passworts anhand definierter Kriterien."""
    def evaluate(self, password):
        """
        Bewertet ein Password-Objekt und setzt dessen Sicherheitsstatus.

        Die Bewertung erfolgt anhand der Sicherheitsstufe (Zeichentypen)
        sowie der Basislänge des Passworts.

        Kriterien:
        - high security: Sicherheitsstufe 3 und Länge ≥ 20
        - medium security: Sicherheitsstufe ≥ 2 und Länge ≥ 12
        - low security: alle anderen Fälle

        :param password: Password-Objekt, dessen Sicherheit bewertet wird
        """
        password_safety = password.get_safety()
        password_base_length = password.get_base_length()
        if password_safety == 3 and password_base_length >= 20:
            password.set_status('high security')
        elif password_safety >= 2 and password_base_length >= 12:
            password.set_status('medium security')
        else: password.set_status('low security')

