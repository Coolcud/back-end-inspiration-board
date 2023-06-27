from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card


"""
boards demo URL: https://backend-inspiration-board.onrender.com

ENDPOINTS --- Boards

loading the website lists all boards:
GET URL/boards

creating a new board:
OPTIONS URL/boards # maybe a CORS thing?
POST URL/boards
	Request body =
    {
		"owner": "Coolcud",
        "title": "Testing"
	}

----------------------------------------------------------

ENDPOINTS --- Boards and Cards

clicking on a board loads all cards for that board:
GET URL/boards/<board_id>/cards

adding a new card:
OPTIONS URL/boards/<board_id>/cards # maybe a CORS thing?
POST URL/boards/<board_id>/cards
	Request body =
    {
		"message": "Test 1"
	}

delete all boards and cards:
OPTIONS URL/destroy_all # maybe a CORS thing?
DELETE URL/destroy_all

----------------------------------------------------------

ENDPOINTS --- Cards

deleting a card:
OPTIONS URL/cards/<card_id> # maybe a CORS thing?
DELETE URL/cards/<card_id>
	returns:
	{
        "details": "Card 156 \"postman test\" successfully deleted"
	}

liking a card:
OPTIONS URL/cards/<card_id>/like # maybe a CORS thing?
PUT URL"url/cards/<card_id>/like"
"""

# --------------------------BOARD ROUTES--------------------------

# example_bp = Blueprint('example_bp', __name__)
boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")


def validate_model_item(model, item_id):
    """Validate that model item exists in database."""
    try:
        item_id = int(item_id)
    except:
        abort(make_response({"message": f"ID '{item_id}' invalid"}, 400))

    item = model.query.get(item_id)
    if not item:
        abort(make_response({"message": f"ID '{item_id}' not found"}, 404))

    return item


@boards_bp.route("", methods=["GET"])
def get_all_boards():
    """Retrieve all boards from database."""
    all_boards = Board.query.all()

    # Create list of board dictionaries based on db data
    response = [board.to_dict() for board in all_boards]

    return jsonify(response), 200


@boards_bp.route("", methods=["POST"])
def create_board():
    """Add new board to database."""
    request_body = request.get_json()

    # TODO: 'Submit query' disabled if title and owner's name are empty (false)
    # https://stackoverflow.com/questions/5614399/disabling-submit-button-until-all-fields-have-values
    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return {"board": new_board.to_dict()}, 201


@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards_of_board(board_id):
    """Retrieve all cards of board via board_id."""
    board = validate_model_item(Board, board_id)

    # Create list of board dictionaries based on db data
    response = [card.to_dict() for card in board.cards]

    # TODO: Determine if jsonify is needed
    return jsonify(response), 200


# --------------------------CARD ROUTES--------------------------
cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")


@cards_bp.route("", methods=["POST"])
def create_card():
    request_body = request.get_json()

    new_card = Card.from_dict(request_body)

    db.session.add(new_card)
    db.session.commit()

    return {"card": new_card.to_dict()}, 201

@cards_bp.route("/<card_id>/like", methods=["PUT"])
def increment_likes(card_id):
    card = validate_model_item(Card, card_id)
    card.likes_count += 1

    db.session.commit()
    return jsonify(card.to_dict()), 200


@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):

    card = validate_model_item(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return jsonify({"message": f"Card {card_id} has been successfully deleted!"})

    
