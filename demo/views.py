from flask_restful_swagger_3 import swagger, Resource
from .models import BookSchema


list_of_books = [
    {
        "id": "1",
        "name": "Harry Potter"
    }
]

@swagger.tags("Books")
class BooksResouce(Resource):
    @swagger.reorder_list_with(BookSchema, response_code=200)
    def get(self):
        """List products"""
        products = list(map(lambda book: BookSchema(**book), list_of_books))
        return products, 200


        