import re

def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Länge prüfen (mindestens 12 Zeichen)
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

print("=== CYBER SECURITY PASSWORD POLICY CHECKER ===")
test_pw = input("Gib ein Test-Passwort zur Prüfung ein: ")
score, tips = check_password_strength(test_pw)

print(f"\nSicherheits-Score: {score}/4")
if score == 4:
    print("Status: STARK (Entspricht modernen Sicherheitsrichtlinien)")
else:
    print("Status: SCHWACH – Verbesserungsvorschläge:")
    for tip in tips:
        print(tip)

