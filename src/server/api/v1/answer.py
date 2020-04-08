from flask_restful import Resource, reqparse, abort
from datetime import datetime

from server.core import Parser, ValidatorAnswer, NotFoundError
from server.db import Answer as AnswerDB

post_parser = reqparse.RequestParser()
post_parser.add_argument('question_id', location='json', required=True)
post_parser.add_argument('text', location='json', required=True)


class AnswerParser(Parser):
    def is_valid(self) -> ValidatorAnswer:
        if not self._validate_question_id():
            return ValidatorAnswer(400, 'invalid question_id argument')
        if not self._validate_text():
            return ValidatorAnswer(400, 'invalid text argument')
        return ValidatorAnswer()

    # TODO: - Complete validators
    def _validate_question_id(self):
        return True

    def _validate_text(self):
        return True


def post_answer(p: AnswerParser) -> dict:
    created_by = 1  # TODO: - Get user_id from token
    answer = AnswerDB(question_id=p.question_id,
                      created_by=created_by,
                      text=p.text,
                      date=datetime.now())
    answer.add_and_commit()
    return dict(answer)


def get_answer(id: int) -> dict:
    answer = AnswerDB.get(id)
    if answer is None:
        raise NotFoundError('answer with specified id doesn\'t exist')
    return dict(answer)


def delete_answer(id: int) -> dict:
    answer = AnswerDB.get(id)
    if answer is None:
        raise NotFoundError('answer with specified id doesn\'t exist')
    data = dict(answer)
    answer.delete_and_commit()
    data['id'] = 'DELETED'
    return data


class Answer(Resource):
    def get(self, id):
        try:
            answer = get_answer(id)
        except NotFoundError as e:
            abort(e.status_code, error=e.message)
        else:
            return answer, 200

    def delete(self, id):
        try:
            answer = delete_answer(id)
        except NotFoundError as e:
            abort(e.status_code, error=e.message)
        else:
            return answer, 200

    def post(self):
        # TODO: - Check if answer posted by person to whom question was addressed
        p = AnswerParser(post_parser.parse_args())
        valid = p.is_valid()
        if not valid:
            abort(valid.code, error=valid.error)
        answer = post_answer(p)
        return answer, 201
