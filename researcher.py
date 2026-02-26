import os
import asyncio
import httpx
from dotenv import load_dotenv

load_dotenv()

# Configuración desde .env
HELIUS_URL = f"https://mainnet.helius-rpc.com/?api-key={os.getenv('HELIUS_API_KEY')}"
TG_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("MY_CHAT_ID")

async def send_tg_alert(message):
    """Envía alertas a tu Telegram"""
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, json={"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"})
        except Exception as e:
            print(f"❌ Error enviando Telegram: {e}")

async def get_latest_signatures(address):
    """Obtiene las últimas transacciones de un programa (Launchpad)"""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "getSignaturesForAddress",
        "params": [address, {"limit": 5}]
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(HELIUS_URL, json=payload)
            return response.json().get("result", [])
        except:
            return []

async def main():
    print("🚀 Agente de Investigación Solana v1.1 - ACTIVO")
    print(f"📡 Monitorizando Launchpads en IP: 46.225.109.134")
    
    # ID de ejemplo: Smithii o Pump.fun (se pueden añadir más)
    launchpads = ["6EF8rrecthR5DkMgz37Wp8m6gxQD2A5CT4Tf6oDpump"] 

    while True:
        for lp in launchpads:
            sigs = await get_latest_signatures(lp)
            if sigs:
                print(f"🔍 Detectadas {len(sigs)} nuevas firmas en launchpad...")
                # Aquí aplicaremos la lógica BURGER SNIPER v4.0 para filtrar
        
        await asyncio.sleep(20) # Pausa para no quemar créditos del RPC

if __name__ == "__main__":
    asyncio.run(main())