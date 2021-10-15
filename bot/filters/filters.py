from dataclasses import dataclass


@dataclass
class Filters:
    text: [str, None]
    regexp: [str, None]
    state: [str, None]


