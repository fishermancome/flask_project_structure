from app import db


class Index(db.Model):
    __tablename__ = "index"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), default="")

    def __str__(self):
        return self.name