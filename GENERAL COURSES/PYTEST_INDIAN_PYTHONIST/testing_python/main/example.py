# THIS IS THE MAIN FUNCTION THAT WE'RE going to MOCK
from typing import Tuple


def replace_indiana(message: str, proper_name: str) -> Tuple[str, int]:
    count = message.lower().count("indiana")
    result = (
        message
        .replace("indiana", proper_name)
        .replace("Indiana", proper_name)
    )

    return result, count


if __name__ == "__main__":  # initializer
    greeting, _ = replace_indiana(
        message="Indiana Jones, I presume?",
        proper_name="Dr."
    )
    print(greeting)
