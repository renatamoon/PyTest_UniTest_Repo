from .database import check_availability


def is_available():
    # some code that checks for database availability
    print("Database service")
    return check_availability()
