from flask_restful_swagger_3 import Schema

class BookSchema(Schema):
    type="object"
    properties = {
        "id": {"type": "string"},
        "name": {"type": "string"}
    }
