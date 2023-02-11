from dataclasses import dataclass


@dataclass
class Message:
    entry_type: str
    temperature: float
    humidity: float


def parse_request_data(request_json: dict) -> Message:
    return Message(
        entry_type=request_json['entry_type'],
        temperature=request_json.get('temperature', ''),
        humidity=request_json.get('humidity', '')
    )
