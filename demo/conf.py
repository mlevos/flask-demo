import os

PORT=os.getenv('PORT', "8080")
HOST=os.getenv('HOST', "localhost")
PROTOCOL=os.getenv('PROTOCOL', "http")

APP_NAME=os.getenv('APP_NAME', "Demo")

SWAGGER_URL = '/api/doc'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'swagger.json'  # Our API url (can of course be a local resource)