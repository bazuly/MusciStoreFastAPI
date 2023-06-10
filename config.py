from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASS')

SMTP_USER = 'baliozsergej@gmail.com'
SMTP_USER_1 = 'serejka50@gmail.com'
SMTP_PASSWORD = 123

