from app import db

class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer, default=0)

    # TODO: Decide if this needs to be added? Would need to do flask db migrate, then upgrade again
    # TODO: Would need to add foreign key in card.py, and relationship to board
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        card_dict = {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }

        # Set relationship between board and card
        if self.board_id:
            card_dict["board_id"] = self.board_id

        return card_dict

    @classmethod
    def from_dict(cls, card_data):
        return cls(
            message=card_data["message"]
        )