from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from app.lib.event_handler import EventHandler
from .data_models import Event


api = Blueprint('api', __name__)


@api.route('/', methods=['GET'])
def index():
    return "Hello World!"


@api.route('/event', methods=['POST'])
def process_event():
    incoming_data = request.get_json()
    try:
        event = Event(**incoming_data)
        if event.is_valid():
            event_handler = EventHandler(event)
            event_handler.process_event()
            return jsonify({'status': 'success'}), 200
    except ValidationError as e:
        return jsonify(e.errors()), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
