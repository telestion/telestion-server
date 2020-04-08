from server.app import db


class ModelWithMethods(db.Model):
    __abstract__ = True

    @staticmethod
    def get(id):
        raise NotImplementedError('get() abstract method must be implemented')

    @staticmethod
    def exists(id):
        raise NotImplementedError('exists() abstract method must be implemented')

    def add(self):
        db.session.add(self)

    def add_and_commit(self):
        db.session.add(self)
        db.session.commit()


class Question(ModelWithMethods):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    created_by = db.Column(db.String, index=True, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def get(id):
        return Question.query.get(id)

    @staticmethod
    def exists(id):
        return Question.get(id) is not None


class Answer(ModelWithMethods):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    created_by = db.Column(db.String, index=True, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    @staticmethod
    def get(id):
        return Answer.query.get(id)

    @staticmethod
    def exists(id):
        return Answer.get(id) is not None
