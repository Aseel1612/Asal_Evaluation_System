import random
import string


def generate_random_text(length=10):
    letters = string.ascii_letters + string.digits + ' '
    return ''.join(random.choice(letters) for _ in range(length))


def generate_evaluation_data():
    return {
        'like': generate_random_text(10),
        'dislike': generate_random_text(10),
        'suggestion': generate_random_text(10),
        'ratings': generate_random_ratings(18)
    }


def generate_manager_evaluation_data():
    return {
        'strengths': generate_random_text(10),
        'improvements': generate_random_text(10),
        'ratings': generate_random_ratings(18)
    }


def generate_random_ratings(num_criteria, num_divs=6):
    return [random.randint(0, num_divs - 1) for _ in range(num_criteria)]
