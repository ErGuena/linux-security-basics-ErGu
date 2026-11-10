# Linux Security Basics & Audit Tools

Dieses Repository enthält meine ersten eigenen Bash- und Python-Skripte für **System Hardening**, **Security Audits** und **Passwort-Richtlinienprüfungen** unter Ubuntu Linux.

## Enthaltene Tools

### 1. `system_audit.sh` (Bash)
Ein automatisiertes System-Audit-Skript zur schnellen Sicherheitsprüfung einer Linux-Umgebung:
- **Benutzer & Berechtigungen:** Überprüfung der aktuellen User-ID und Gruppenmitgliedschaften (`id`).
- **Firewall-Status:** Kontrolle der aktiven UFW-Regeln (`ufw status`).
- **Netzwerk & offene Ports:** Analyse lauschender TCP/UDP-Dienste (`ss -tuln`).
- **Login-Historie:** Auswertung der letzten Authentifizierungs-Events über `systemd-logind`.

**Ausführung:**
```bash
chmod +x system_audit.sh
./system_audit.sh
```

### 2. `password_checker.py` (Python)
Ein interaktives CLI-Tool zur Prüfung von Passwörtern gegen moderne Unternehmens-Sicherheitsrichtlinien (angelehnt an BSI / ISO 27001):
- Abgleich gegen eine **Blacklist** häufig erratener Passwörter.
- Prüfung auf Mindestlänge (12 Zeichen), Groß-/Kleinschreibung, Zahlen und Sonderzeichen.
- Interaktive Schleife mit direktem Sicherheits-Score (0–4) und konkreten Handlungsempfehlungen.

**Ausführung:**
```bash
python3 password_checker.py
```
