import os
import getpass

def get_username() -> dict:
    """
    Returns:
        dict: A dictionary with the key 'output' and the value as the current user's name.
    
    """
    try:
        username = os.getlogin()
    except OSError:
        username = getpass.getuser()
    return {'output': username}

