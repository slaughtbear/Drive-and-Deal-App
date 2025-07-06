import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient


load_dotenv() # Se cargan las variables de entorno en el script
MONGODB_URL = os.getenv('MONGODB_URL') # Constante con la url de MongoDB Atlas
client = AsyncIOMotorClient(MONGODB_URL) # Cliente de conexión con la base de datos