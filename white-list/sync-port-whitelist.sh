#!/bin/bash
# sync-port-whitelist.sh
# Reads port-whitelist.conf and applies UFW rules to match.
# Wipes all existing UFW rules for the ports listed in the config,
# then re-adds allow rules per the config. Idempotent.

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CONFIG_FILE="$SCRIPT_DIR/port-whitelist.conf"

if [[ $EUID -ne 0 ]]; then
    echo "Error: must run as root (use sudo)" >&2
    exit 1
fi

if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: config file not found: $CONFIG_FILE" >&2
    exit 1
fi

PORTS=$(grep -vE "^[[:space:]]*(#|$)" "$CONFIG_FILE" | cut -d: -f1 | tr -d " " | sort -u)

if [[ -z "$PORTS" ]]; then
    echo "No ports found in config file"
    exit 0
fi

echo "==> Ports to manage:" $PORTS

# Step 1: remove all existing UFW rules for these ports (v4 and v6)
for PORT in $PORTS; do
    echo ""
    echo "==> Removing existing UFW rules for port $PORT"
    while true; do
        RULE_NUM=$(ufw status numbered 2>/dev/null \
            | grep -E "^\[[ ]*[0-9]+\][ ]+${PORT}[ /]" \
            | head -1 \
            | awk -F"[][]" "{print \$2}" \
            | tr -d " ")
        if [[ -z "$RULE_NUM" ]]; then
            break
        fi
        echo "   deleting rule [$RULE_NUM]"
        ufw --force delete "$RULE_NUM" > /dev/null
    done
done

# Step 2: add new rules from config
echo ""
echo "==> Adding rules from config"
while IFS=: read -r PORT IP; do
    PORT=$(echo "$PORT" | tr -d " ")
    IP=$(echo "$IP" | tr -d " ")
    [[ "$PORT" =~ ^# ]] && continue
    [[ -z "$PORT" || -z "$IP" ]] && continue
    echo "   allow $IP -> port $PORT/tcp"
    ufw allow from "$IP" to any port "$PORT" proto tcp > /dev/null
done < "$CONFIG_FILE"

# Step 3: reload
echo ""
echo "==> Reloading UFW"
ufw reload

echo ""
echo "==> Done. Rules for managed ports:"
for PORT in $PORTS; do
    echo "--- port $PORT ---"
    ufw status numbered | grep -E "^\[[ ]*[0-9]+\][ ]+${PORT}[ /]" || echo "   (no rules — all traffic DENIED by default)"
done
