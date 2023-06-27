from app import db

class Board(db.Model):
    # Columns
    board_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    owner = db.Column(db.String)

    # Relationship
    cards = db.relationship("Card", back_populates="board")

    def to_dict(self):
        board_dict = {
            "board_id": self.board_id,
            "owner": self.owner,
            "title": self.title
        }

        return board_dict

    @classmethod
    def from_dict(cls, board_data):
        return cls(
            owner=board_data["owner"],
            title=board_data["title"]
        )
