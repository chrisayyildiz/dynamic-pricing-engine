import requests
import os
from dotenv import load_dotenv
load_dotenv()

RAPID_KEY = os.getenv("RAPID_API_KEY")

print(RAPID_KEY)