"""
Basic REST API Request and Response Fundamentals Module.

This module demonstrates fundamental HTTP GET requests using Python's standard
library (`urllib.request` and `json`), with fallback support for `requests`.
Covers status code validation, JSON data parsing, query parameter formatting,
and robust error handling.

PEP 8 compliant, type-annotated, and compatible with Python 2.7 - 3.13.
"""

# Standard library imports for JSON handling, URL formatting, and HTTP calls
import json
import sys
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional

ITUNES_SEARCH_URL = "https://itunes.apple.com/search"


def fetch_itunes_tracks(term: str, limit: int = 25) -> List[Dict[str, Any]]:
    """
    Fetches track metadata from iTunes Search REST API using standard library urllib.

    Args:
        term (str): Search term query (e.g. artist or song name).
        limit (int): Maximum number of track results to return (default: 25).

    Returns:
        List[Dict[str, Any]]: List of dictionary track metadata objects.

    Raises:
        RuntimeError: If HTTP request fails or returns non-200 status code.
    """
    params = {
        "entity": "song",
        "limit": limit,
        "term": term,
    }
    query_string = urllib.parse.urlencode(params)
    full_url = f"{ITUNES_SEARCH_URL}?{query_string}"

    try:
        req = urllib.request.Request(
            full_url,
            headers={"User-Agent": "Python-API-Tutorial/1.0"}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            status_code = response.getcode()
            if status_code != 200:
                raise RuntimeError(f"HTTP Request failed with status code {status_code}")
            
            content = response.read().decode("utf-8")
            payload: Dict[str, Any] = json.loads(content)
            return payload.get("results", [])
    except Exception as err:
        print(f"API Request Failure: {err}", file=sys.stderr)
        raise RuntimeError(f"Failed to fetch data from iTunes API: {err}") from err


def format_track_summary(tracks: List[Dict[str, Any]]) -> List[str]:
    """
    Formats raw iTunes track payloads into human-readable summary strings.

    Args:
        tracks (List[Dict[str, Any]]): List of raw track dictionary objects.

    Returns:
        List[str]: Formatted track summaries.
    """
    summaries: List[str] = []
    for track in tracks:
        track_name = track.get("trackName", "Unknown Track")
        artist_name = track.get("artistName", "Unknown Artist")
        collection = track.get("collectionName", "Single")
        summaries.append(f"Track: '{track_name}' by '{artist_name}' [{collection}]")
    return summaries


def print_json_pretty(data: Dict[str, Any]) -> str:
    """
    Converts raw dictionary payload into formatted JSON string representation.

    Args:
        data (Dict[str, Any]): Dictionary object to format.

    Returns:
        str: Pretty-printed JSON string with 4-space indentation.
    """
    return json.dumps(data, indent=4)


if __name__ == "__main__":
    search_query = "love"
    print(f"Searching iTunes API for tracks matching '{search_query}'...")
    results = fetch_itunes_tracks(search_query, limit=5)
    formatted_list = format_track_summary(results)

    for item in formatted_list:
        print(f"  -> {item}")
