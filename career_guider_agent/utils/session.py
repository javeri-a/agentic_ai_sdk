user_sessions = {}

def init_session(user_id):
    user_sessions[user_id] = {"step": 0, "answers": {}}

def get_session(user_id):
    return user_sessions.get(user_id)

def update_session(user_id, field, value):
    session = user_sessions[user_id]
    session["answers"][field] = value
    session["step"] += 1

def reset_session(user_id):
    init_session(user_id)
