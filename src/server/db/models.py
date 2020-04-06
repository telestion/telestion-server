from server.app import db


class ModelWithMethods(db.Model):
    __abstract__ = True

    def get(self, id):
        return self.query.get(id)

    def exists(self, id):
        return self.query.get(id) is not None

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


class Answer(ModelWithMethods):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    created_by = db.Column(db.String, index=True, nullable=False)
    text = db.Column(db.String, nullable=False)
