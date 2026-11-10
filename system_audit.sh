#!/bin/bash

echo "========================================="
echo "   LINUX SECURITY AUDIT - $(date +%Y-%m-%d)"
echo "========================================="
echo ""
echo "[1] Angemeldeter Benutzer & Rechte:"
id
echo ""
echo "[2] Firewall-Status (UFW):"
sudo ufw status
echo ""
echo "[3] Aktive Netzwerkverbindungen & offene Ports:"
ss -tuln
echo ""
echo "[4] Letzte 5 System-Logins:"
journalctl -n 5 -u systemd-logind --no-pager
echo ""
echo "Audit abgeschlossen."

