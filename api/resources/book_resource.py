from flask import request
from flask_restful import Resource, marshal_with
from api.db_models.book_model import Books
from api.db_models.user_model import Users
from api.structures.book_structure import individual_book_structure
from extensions import db


class Book(Resource):
    @marshal_with(individual_book_structure)
    def get(self, book_id=None):
        if book_id:
            return Books.query.filter_by(id=book_id).first_or_404()
        data = request.get_json()
        return Books.query.filter_by(**data).all() if data and any(data.values()) else Books.query.all()

    def post(self):
        data = request.get_json()
        if data:
            db.session.add(Books(**data))
            db.session.commit()
            return 200
        return 'All fields should be fulfilled'

    def put(self, book_id=None):
        data = request.get_json()
        if book_id and data:
            book_to_update = Books.query.filter_by(id=book_id).first_or_404()
            for key, value in data.items():
                setattr(book_to_update, key, value)
            return 200
        return 'Sorry something went wrong'

    def patch(self, book_id=None):
        data = request.get_json()
        if book_id and data:
            book_to_update = Books.query.filter_by(id=book_id).first_or_404()
            for key, value in data.items():
                setattr(book_to_update, key, value)
            db.session.commit()
            return 200
        return 'Sorry something went wrong'

    def delete(self, book_id=None):
        if book_id:
            book_to_delete = Books.query.filter_by(id=book_id).first_or_404()
            db.session.delete(book_to_delete)
            db.session.commit()
            return 200
        return 'Sorry something went wrong'
