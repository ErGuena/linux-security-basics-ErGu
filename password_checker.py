import re

# Sperrliste für häufig erratene Passwörter (in Kleinschreibung)
BLACKLIST = ["passwort123!", "admin2026!", "sommer2026!", "krankenhaus1!", "qwertz12345!"]

def check_password_strength(password):
    # Zuerst prüfen, ob das Passwort auf der Sperrliste steht
    if password.lower() in BLACKLIST:
        return 0, ["- WARNUNG: Dieses Passwort steht auf der Sperrliste (zu leicht zu erraten)!"]

    score = 0
    feedback = []

    # 1. Länge prüfen
    if len(password) >= 12:
        score += 1
    else:
        feedback.append("- Mindestens 12 Zeichen verwenden.")

    # 2. Groß- und Kleinbuchstaben prüfen
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("- Groß- und Kleinbuchstaben kombinieren.")

    # 3. Zahlen prüfen
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("- Mindestens eine Zahl einbauen.")

    # 4. Sonderzeichen prüfen
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("- Mindestens ein Sonderzeichen nutzen.")

    return score, feedback

print("=== CYBER SECURITY PASSWORD POLICY CHECKER v2.0 ===")
print("(Tippe 'exit' zum Beenden)\n")

# Endlosschleife: läuft so lange, bis der Nutzer 'exit' eingibt
while True:
    test_pw = input("Passwort zum Prüfen eingeben: ")
    
    if test_pw.lower() == "exit":
        print("Programm beendet.")
        break

    score, tips = check_password_strength(test_pw)

    print(f"Sicherheits-Score: {score}/4")
    if score == 4:
        print("Status: STARK\n")
    else:
        print("Status: SCHWACH – Verbesserungsvorschläge:")
        for tip in tips:
            print(tip)
        print("")
