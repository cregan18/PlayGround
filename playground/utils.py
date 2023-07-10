import os as _os


def get_playground_path():
    """
    Function to dynamically grab the path to the playground directory to use in other files when necessary.
    :return: [str] path to playground
    """
    playground_path = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
    return playground_path


if __name__ == "__main__":
    print(get_playground_path())