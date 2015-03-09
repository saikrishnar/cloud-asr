import json
import wave
from cloudasr.schema import WorkerType, User, Recording, Hypothesis, Transcription


class WorkerTypesModel:

    def __init__(self, session):
        self.session = session

    def get_models(self):
        return self.session.query(WorkerType).all()

    def get_available_workers(self):
        workers = []

        for worker in self.session.query(WorkerType).all():
            workers.append({
                'id': worker.id,
                'name': worker.name,
                'description': worker.description
            })

        return workers

    def get_worker_type(self, id):
        return self.session.query(WorkerType).get(id)

    def upsert_worker_type(self, id):
        worker_type = self.get_worker_type(id)

        if not worker_type:
            worker_type = WorkerType(id = id)
            self.session.add(worker_type)
            self.session.commit()

        return worker_type

    def edit_worker(self, id, name, description):
        worker = self.upsert_worker_type(id)
        worker.name = name
        worker.description = description

        self.session.commit()

class RecordingsModel:

    def __init__(self, session, worker_types_model, path = None, url = None):
        self.session = session
        self.worker_types_model = worker_types_model
        self.url = url

        if path is not None:
            self.file_saver = FileSaver(path)

    def get_recordings(self, model):
        return Recording.query.filter(Recording.model == model)

    def get_recording(self, id):
        return self.session.query(Recording).get(int(id))

    def get_random_recording(self, model):
        from sqlalchemy import func
        return self.session.query(Recording) \
            .filter(Recording.model == model) \
            .order_by(Recording.rand_score) \
            .limit(1) \
            .one()

    def save_recording(self, id, part, model, body, frame_rate, alternatives):
        (path, url) = self.file_saver.save_wav(id, part, model, body, frame_rate)
        self.save_recording_to_db(id, part, model, path, url, alternatives)

    def save_recording_to_db(self, id, part, model, path, url, alternatives):
        worker_type = self.worker_types_model.upsert_worker_type(model)

        recording = Recording(
            uuid = id,
            part = part,
            path = path,
            url = self.url + url,
            score = alternatives[0]["confidence"],
            rand_score = alternatives[0]["confidence"]
        )

        worker_type.recordings.append(recording)

        for alternative in alternatives:
            recording.hypotheses.append(Hypothesis(
                text = alternative["transcript"],
                confidence = alternative["confidence"]
            ))

        self.session.add(recording)
        self.session.commit()

    def add_transcription(self, user, id, transcription, native_speaker, offensive_language, not_a_speech):
        transcription = Transcription(
            user_id = user.get_id(),
            text = transcription,
            native_speaker = native_speaker,
            offensive_language = offensive_language,
            not_a_speech = not_a_speech
        )

        recording = self.get_recording(id)
        recording.transcriptions.append(transcription)
        recording.update_score()
        self.session.commit()


class FileSaver:

    def __init__(self, path):
        self.path = path

    def save_wav(self, id, part, model, body, frame_rate):
        path = '%s/%s-%d-%d.wav' % (self.path, model, id, part)
        url = '/static/data/%s-%d-%d.wav' % (model, id, part)

        wav = wave.open(path, 'w')
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(frame_rate)
        wav.writeframes(body)
        wav.close()

        return (path, url)


class UsersModel:

    def __init__(self, session):
        self.session = session

    def get_user(self, id):
        return self.session.query(User).get(int(id))

    def upsert_user(self, userinfo):
        user = self.get_user(userinfo['id'])

        if user:
            user.email = userinfo['email']
            user.name = userinfo['name']
            user.avatar = userinfo['picture']
        else:
            user = User(
                id = int(userinfo['id']),
                email = userinfo['email'],
                name = userinfo['name'],
                avatar = userinfo['picture']
            )

        self.session.add(user)
        self.session.commit()

        return user


