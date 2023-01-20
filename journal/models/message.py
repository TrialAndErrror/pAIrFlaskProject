from dataclasses import dataclass


@dataclass
class Message:
    entry_type: str
    amount: float
    name: str


def parse_request_data(request_json: dict) -> Message:
    return Message(
        entry_type=request_json['entry_type'],
        amount=request_json['amount'],
        name=request_json.get('name', '')
    )
