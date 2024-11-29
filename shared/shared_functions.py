from flask import jsonify

def json_response(data, status, error_msg):
    response = {
        "data": data,
        "status": status,
        "error": error_msg
    }
    return jsonify(response)

def is_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False