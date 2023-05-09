from .random import Random
from .recommender import Recommender
import random


class MyRecommender(Recommender):
    """
    Recommend tracks closest to the previous one.
    Fall back to the random recommender if no
    recommendations found for the track.
    """

    def __init__(self, tracks_redis, catalog, k, time_threshold):
        self.tracks_redis = tracks_redis
        self.fallback = Random(tracks_redis)
        self.catalog = catalog
        self.k = k
        self.time_threshold = time_threshold

    def recommend_next(self, user: int, prev_track: int, prev_track_time: float) -> int:
        previous_track = self.tracks_redis.get(prev_track)
        if previous_track is None:
            return self.fallback.recommend_next(user, prev_track, prev_track_time)

        previous_track = self.catalog.from_bytes(previous_track)
        recommendations = previous_track.recommendations
        if recommendations is None or prev_track_time < self.time_threshold:
            return self.fallback.recommend_next(user, prev_track, prev_track_time)

        shuffled = list(recommendations)[:self.k]
        random.shuffle(shuffled)
        return shuffled[0]
