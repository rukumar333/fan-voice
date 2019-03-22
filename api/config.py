import os

PORT = os.getenv('PORT', 3030)
DB_USER = os.getenv('DB_USER', 'fv')
DB_PASS = os.getenv('DB_PASS', '')
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
DB_NAME = os.getenv('DB_NAME', 'fanvoice')
