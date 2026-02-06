# Password Generator & Evaluator

Ein kleines Python-Projekt zur **Generierung** und **Bewertung von Passwörtern**.  
Passwörter werden zufällig erzeugt und anhand von Länge sowie verwendeten Zeichentypen in Sicherheitsstufen eingeteilt.

---

## Features

- Generierung sicherer Zufallspasswörter mit `secrets`
- Drei Sicherheitsstufen:
  - **Level 1**: Buchstaben
  - **Level 2**: Buchstaben + Zahlen
  - **Level 3**: Buchstaben + Zahlen + Sonderzeichen
- Automatische Bewertung der Passwortsicherheit:
  - `low security`
  - `medium security`
  - `high security`
- Möglichkeit, benutzerdefinierte Passwörter zu evaluieren (basierend auf Sicherheitsstufen und Länge)

---

## Projektstruktur

```text
.
├── passwordgen.py
├── password.py
├── passwordeval.py
└── README.md
```

## Voraussetzungen
- Python 3.8+
- Keine externen Abhängigkeiten (nur Standardbibliothek)
