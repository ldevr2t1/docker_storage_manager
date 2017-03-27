def create_json(uid, version, body):
    #gotta check if the body is valid jsonc
    return jsonify({"problem_id":str(uid), "version": version, "body":body})


def insert_json(uid, version, body):
    db.posts.insert_one({"problem_id": str(uid), "version": version, "body":body})


def get_status(status, message):
    return jsonify({"Status": status, "Message": message})


def root_get():
    return 'This is version 2.0'