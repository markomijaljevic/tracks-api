import os
import json
from tracks_API.settings import BASE_DIR
from tracks_API import models
from datetime import datetime


def load_tracks_in_db():
    tracks_initial_file_path = os.path.join(
        BASE_DIR, "tracks_API", "initial_tracks_data", "tracks.json"
    )
    
    tracks = json.loads(open(tracks_initial_file_path, 'r').read())
    
    # Tracks.objects.bulk_create(tracks)
    for track in tracks:
        track_db = models.Tracks()
        track_db.title = track.get("title", "")
        track_db.artist = track.get("artist", "")
        track_db.duration = float(track.get("duration", 0))
        track_db.last_play = datetime.strptime(track.get("last_play", "0000-00-00 00-00-00"), "%Y-%m-%d %H:%M:%S")
        track_db.save()