import requests as req
import warnings

import statsbombpy.entities as ents

from statsbombpy.config import OPEN_DATA_PATHS


def competitions():
    competitions = req.get(OPEN_DATA_PATHS["competitions"]).json()
    competitions = ents.competitions(competitions)
    return competitions


def matches(competition_id: int, season_id: int) -> dict:
    matches = req.get(
        OPEN_DATA_PATHS["matches"].format(
            competition_id=competition_id, season_id=season_id
        )
    ).json()
    matches = ents.matches(matches)
    return matches


def lineups(match_id: int):
    lineups = req.get(OPEN_DATA_PATHS["lineups"].format(match_id=match_id)).json()
    lineups = ents.lineups(lineups)
    return lineups


def events(match_id: int) -> dict:
    events = req.get(OPEN_DATA_PATHS["events"].format(match_id=match_id)).json()
    events = ents.events(events, match_id)
    return events


def frames(match_id: int) -> dict:
    frames = {}
    warnings.warn("There is currently no open 360 data, returning empty dict")
    return frames


def player_match_stats(match_id: int) -> dict:
    player_match_stats = {}
    warnings.warn("There is currently no open data for aggregated stats, returning empty dict")
    return player_match_stats


def player_season_stats(competition_id: int, season_id: int) -> dict:
    player_season_stats = {}
    warnings.warn("There is currently no open data for aggregated stats, returning empty dict")
    return player_season_stats


def team_season_stats(competition_id: int, season_id: int) -> dict:
    team_season_stats = {}
    warnings.warn("There is currently no open data for aggregated stats, returning empty dict")
    return team_season_stats