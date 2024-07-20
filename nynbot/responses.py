from random import choice, randint 


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return 'Vocẽ está quieto igual um ratinho!'
    elif 'Ola' in lowered:
        return 'Oieee!'