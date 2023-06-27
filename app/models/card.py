from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)

    # TODO: Decide if this needs to be added? Would need to do flask db migrate, then upgrade again
    # TODO: Would need to add foreign key in card.py, and relationship to board
    # board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    # board = db.relationship("Board", back_populates="cards")