from django.http import HttpRequest, HttpResponse
from django.views import View
from . import models
from . import forms
import json


class TracksViews(View):
    def get(self, request: HttpRequest, track_id: int = None) -> HttpResponse:

        if track_id:
            track = models.Tracks.objects.filter(id=track_id)

            if track.exists():
                context = {
                    "title": track[0].title,
                    "artist": track[0].artist,
                    "duration": track[0].duration,
                    "last_play": track[0].last_play,
                }
                return HttpResponse(json.dumps(context, default=str))

        return HttpResponse("Not found")

    def post(self, request: HttpRequest) -> HttpResponse:
        form = forms.CreateTrackForm(json.loads(request.body))

        if form.is_valid():
            form.save()
            return HttpResponse("Success")

        return HttpResponse("Failed")


class TracksMostRecentViews(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        tracks = models.Tracks.objects.all().order_by("-last_play")

        most_recent_tracks = []
        for track in tracks[:100]:
            context = {
                "title": track.title,
                "artist": track.artist,
                "duration": track.duration,
                "last_play": track.last_play,
            }
            most_recent_tracks.append(context)

        return HttpResponse(json.dumps(most_recent_tracks, default=str))


class TracksFilterByNameViews(View):
    def get(self, request: HttpRequest, track_title: str = "") -> HttpResponse:

        tracks = models.Tracks.objects.filter(title=track_title)

        tracks_with_same_name = []
        for track in tracks[:100]:
            context = {
                "title": track.title,
                "artist": track.artist,
                "duration": track.duration,
                "last_play": track.last_play,
            }
            tracks_with_same_name.append(context)

        return HttpResponse(json.dumps(tracks_with_same_name, default=str))


class ArtistsViews(View):
    def get(self, request: HttpRequest) -> HttpResponse:

        artists = models.Tracks.objects.all().values("artist").distinct()

        results = []
        for artist in artists:
            context = {
                "artist_name": artist["artist"],
                "total tracks": models.Tracks.objects.filter(
                    artist=artist["artist"]
                ).count(),
                "recently_played_track": models.Tracks.objects.filter(
                    artist=artist["artist"]
                )
                .order_by("-last_play")[0]
                .title,
            }
            results.append(context)

        return HttpResponse(json.dumps(results, default=str))
