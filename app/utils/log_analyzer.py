import json
import ast

LOG_FILE = "app_logs.jsonl"

def analyze_logs():
    unauthorized_attempts = 0
    unique_ips = set()

    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    message_raw = entry.get("message", {})

                    # Si el valor de "message" es un string tipo diccionario, lo convertimos
                    if isinstance(message_raw, str):
                        try:
                            message = ast.literal_eval(message_raw)
                        except Exception:
                            continue
                    else:
                        message = message_raw

                    if isinstance(message, dict) and message.get("event") == "unauthorized_access_attempt":
                        unauthorized_attempts += 1
                        ip = message.get("client_ip")
                        if ip:
                            unique_ips.add(ip)

                except json.JSONDecodeError:
                    continue
    except FileNotFoundError:
        print("⚠️ No hay archivo de logs.")
        return

    if unauthorized_attempts > 0:
        print(f"🚨 Intentos no autorizados detectados: {unauthorized_attempts}")
        print("🧠 IPs únicas involucradas:")
        for ip in unique_ips:
            print(" -", ip)
    else:
        print("✅ Ningún intento no autorizado registrado.")

if __name__ == "__main__":
    analyze_logs()
