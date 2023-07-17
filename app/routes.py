from flask import Blueprint, request, jsonify, make_response, abort
from app import db
from app.models.board import Board
from app.models.card import Card
from dotenv import load_dotenv
import os
import requests

boards_bp = Blueprint("boards_bp", __name__, url_prefix="/boards")
cards_bp = Blueprint("cards_bp", __name__, url_prefix="/cards")

def validate_model_item(model, item_id):
    """Validate model item exists in database."""
    try:
        item_id = int(item_id)
    except:
        abort(make_response({"message": f"ID '{item_id}' invalid"}, 400))

    item = model.query.get(item_id)
    if not item:
        abort(make_response({"message": f"ID '{item_id}' not found"}, 404))

    return item


# --------------------------BOARD ROUTES--------------------------

@boards_bp.route("", methods=["GET"])
def get_all_boards():
    """Retrieve all boards from database."""
    all_boards = Board.query.all()

    response = [board.to_dict() for board in all_boards]

    return jsonify(response), 200


@boards_bp.route("", methods=["POST"])
def create_board():
    """Add new board to database."""
    request_body = request.get_json()

    new_board = Board.from_dict(request_body)

    db.session.add(new_board)
    db.session.commit()

    return {"board": new_board.to_dict()}, 201

@boards_bp.route("/<board_id>", methods=["DELETE"])
def delete_board(board_id):
    """Delete board via board_id."""
    board = validate_model_item(Board, board_id)

    db.session.delete(board)
    db.session.commit()

    return jsonify({"message": f"Board {board_id} has been successfully deleted!"}), 200


# ---------------------BOARD & CARD ROUTES---------------------
def send_post_to_slack(card):
    load_dotenv()
    slack_bot_token = os.environ.get('SLACK_BOT_TOKEN')
    slack_channel = 'byte-sized-inspiration'
    text = f"A new card was created with this message:\'{card.message}\'"
    headers = {'Authorization': f"Bearer {slack_bot_token}"}
    data = {
        'channel': slack_channel,
        'text': text
    }
    response = requests.post(
        'https://slack.com/api/chat.postMessage', headers=headers, json=data)


@boards_bp.route("/<board_id>/cards", methods=["GET"])
def get_all_cards_of_board(board_id):
    """Retrieve all cards of board via board_id."""
    board = validate_model_item(Board, board_id)

    # Create list of board dictionaries based on db data
    response = [card.to_dict() for card in board.cards]

    return jsonify(response), 200


@boards_bp.route("/<board_id>/cards", methods=["POST"])
def create_card(board_id):
    """Add new card to board and database."""
    board = validate_model_item(Board, board_id)

    request_body = request.get_json()
    new_card = Card.from_dict(request_body)
    new_card.board = board

    db.session.add(new_card)
    db.session.commit()

    send_post_to_slack(new_card)

    return {"card": new_card.to_dict()}, 201


# --------------------------CARD ROUTES--------------------------

@cards_bp.route("/<card_id>/like", methods=["PUT"])
def increment_likes(card_id):
    """Increase card's like count by 1."""
    card = validate_model_item(Card, card_id)

    card.likes_count += 1

    db.session.commit()
    return jsonify(card.to_dict()), 200


@cards_bp.route("/<card_id>", methods=["DELETE"])
def delete_card(card_id):
    """Delete card via card_id."""
    card = validate_model_item(Card, card_id)

    db.session.delete(card)
    db.session.commit()

    return jsonify({"message": f"Card {card_id} has been successfully deleted!"}), 200
