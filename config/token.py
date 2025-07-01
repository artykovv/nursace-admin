import asyncio
import aiohttp
from fastapi import Request
from config.config import site_url_and_port


async def validate_token(token: str):
    url = f"{site_url_and_port}/auth/validate-token"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            return response.status  # Возвращает статус-код

async def get_user_id_by_token(request: Request):
    token=request.cookies.get("Bearer")
    
    if token:
        url = f"{site_url_and_port}/user/me"  # убери двойной слэш //
        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {token}"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("id")  # вот так правильно
                else:
                    return None

    else:
        return None