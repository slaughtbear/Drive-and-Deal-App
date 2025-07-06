from src.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = settings.MONGODB_URL # Constante con la url de MongoDB Atlas
client = AsyncIOMotorClient(MONGODB_URL) # Cliente de conexión con la base de datos


# PRUEBA DE CONEXIÓN
# Ejecuta en la terminal: python -m src.database.db
async def test_connection() -> None:
    try:
        result = await client.admin.command('ping')
        print("Conexión exitosa:", result)
    except Exception as e:
        print("Error de conexión:", e)


if __name__ == "__main__":
    import asyncio
    asyncio.run(test_connection())