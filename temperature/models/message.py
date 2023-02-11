from dataclasses import dataclass


@dataclass
class Message:
    temperature: float
    humidity: float


def parse_request_data(request_json: dict) -> Message:
    return Message(
        temperature=request_json.get('temperature', ''),
        humidity=request_json.get('humidity', '')
    )
