def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return "Hi there!"
    
    if p_message == 'help':
        return "Help is on the way!"
    
    return "I don't know what you said, can you please try to rephrase your message?"
