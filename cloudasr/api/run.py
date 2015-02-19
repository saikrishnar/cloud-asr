from flask import Flask, request, jsonify
from flask.ext.socketio import SocketIO, emit, session
from lib import create_frontend_worker, MissingHeaderError, NoWorkerAvailableError, WorkerInternalError
import os
app = Flask(__name__)
app.secret_key = "12345"
app.config['DEBUG'] = True
socketio = SocketIO(app)


@app.route("/recognize", methods=['POST'])
def recognize_batch():
    data = {
        "model": request.args.get("lang", "en-GB"),
        "wav": request.data
    }

    try:
        worker = create_frontend_worker(os.environ['MASTER_ADDR'])
        return jsonify(worker.recognize_batch(data, request.headers))
    except MissingHeaderError:
        return jsonify({"status": "error", "message": "Missing header Content-Type"}), 400
    except NoWorkerAvailableError:
        return jsonify({"status": "error", "message": "No worker available"}), 503

@socketio.on('begin')
def begin_online_recognition(message):
    try:
        worker = create_frontend_worker(os.environ['MASTER_ADDR'])
        worker.connect_to_worker(message["model"])

        session["worker"] = worker
    except NoWorkerAvailableError:
        emit('server_error', {"status": "error", "message": "No worker available"})

@socketio.on('chunk')
def recognize_chunk(message):
    try:
        if "worker" not in session:
            emit('server_error', {"status": "error", "message": "No worker available"})
            return

        response = session["worker"].recognize_chunk(message["chunk"], message["frame_rate"])
        emit('result', response)
    except WorkerInternalError:
        emit('server_error', {"status": "error", "message": "Internal error"})
        del session["worker"]

@socketio.on('end')
def end_recognition(message):
    if "worker" not in session:
        emit('server_error', {"status": "error", "message": "No worker available"})
        return

    response = session["worker"].end_recognition()
    del session["worker"]
    emit('final_result', response)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=80)
