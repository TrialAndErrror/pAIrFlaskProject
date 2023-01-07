from dataclasses import dataclass


@dataclass
class ResponseMessage:
    success: bool
    message: str
