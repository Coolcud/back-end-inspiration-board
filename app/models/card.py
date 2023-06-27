from app import db

class Card(db.Model):
    # Columns
    card_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    message = db.Column(db.String)
    likes_count = db.Column(db.Integer)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))

    # Relationship
    board = db.relationship("Board", back_populates="cards")

    def to_dict(self):
        card_dict = {
            "card_id": self.card_id,
            "message": self.message,
            "likes_count": self.likes_count
        }

        # Associate board_id to card
        if self.board_id:
            card_dict["board_id"] = self.board_id

        return card_dict

    @classmethod
    def from_dict(cls, card_data):
        return cls(
            message=card_data["message"]
        )
