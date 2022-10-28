from dataclasses import dataclass


@dataclass
class NewPost:
    title: str
    body: str
    userId: int

@dataclass
class PatchPost:
    title: str
    body: str
