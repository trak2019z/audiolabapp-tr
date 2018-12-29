import random
from time import time

from ..fact import fake


def create_record(count=1, uid=None, series_uid=None, current_series_uid=None,
                  start_time=None, uploaded_at=None, filepath=None,
                  label=None):
    return [{
        "uid": uid or fake.uuid4(),
        "series_uid": series_uid or create_series()["uid"],
        "start_time": start_time or time() - 300,
        "uploaded_at": uploaded_at,
        "label_uid": label
    } for _ in range(count)]


def create_recorder(count=1, uid=None, location_description=None,
                    current_series_uid=None):
    return [{
        "uid": uid or fake.uuid4(),
        "location_description": location_description or fake.sentence()
    } for _ in range(count)]


def create_recording_parameters(count=1, uid=None, samplerate=None,
                                channels=None, duration=None,
                                amplification=None):
    return [{
        'uid': uid or fake.uuid4(),
        'samplerate': samplerate or random.randrange(1, 100000),
        'channels': channels or random.randrange(1, 10),
        'duration': round(duration or random.random() * 10, 5),
        'amplification': round(amplification or random.random() * 3, 5)
    }]


def create_series(count=1, uid=None, description=None, recorder_uid=None,
                  parameters=None):
    return [{
        'uid': uid or fake.uuid4(),
        'description': description or fake.sentence(),
        'recorder_uid': recorder_uid or create_recorder()[0]["uid"],
        'parameters': parameters or create_recording_parameters()[0]
    }]
