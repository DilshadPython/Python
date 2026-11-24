"""
Unit Test Suite for Basic REST API Fundamentals Module.

Mocks external HTTP requests using unittest.mock to test API response handling,
payload parsing, track summary formatting, and error exceptions.
"""

import io
import json
import unittest
from unittest.mock import MagicMock, patch
from typing import Any, Dict, List

from basic_api_requests import (
    fetch_itunes_tracks,
    format_track_summary,
    print_json_pretty,
)


class TestApiFundamentals(unittest.TestCase):
    """Test cases for iTunes REST API fetch and parsing functions."""

    @patch("basic_api_requests.urllib.request.urlopen")
    def test_fetch_itunes_tracks_success(self, mock_urlopen: MagicMock) -> None:
        """Verify successful API fetch and JSON payload parsing."""
        mock_payload = {
            "resultCount": 2,
            "results": [
                {"trackName": "Love Story", "artistName": "Taylor Swift", "collectionName": "Fearless"},
                {"trackName": "Bleeding Love", "artistName": "Leona Lewis", "collectionName": "Spirit"},
            ],
        }
        json_bytes = json.dumps(mock_payload).encode("utf-8")

        mock_cm = MagicMock()
        mock_cm.getcode.return_value = 200
        mock_cm.read.return_value = json_bytes
        mock_cm.__enter__.return_value = mock_cm

        mock_urlopen.return_value = mock_cm

        tracks = fetch_itunes_tracks("love", limit=2)
        self.assertEqual(len(tracks), 2)
        self.assertEqual(tracks[0]["trackName"], "Love Story")
        self.assertEqual(tracks[1]["artistName"], "Leona Lewis")

    @patch("basic_api_requests.urllib.request.urlopen")
    def test_fetch_itunes_tracks_error(self, mock_urlopen: MagicMock) -> None:
        """Verify RuntimeError is raised when HTTP request fails."""
        mock_urlopen.side_effect = Exception("Connection timeout")

        with self.assertRaises(RuntimeError):
            fetch_itunes_tracks("invalid_query")

    def test_format_track_summary(self) -> None:
        """Verify track payload formatting into summary text."""
        raw_data: List[Dict[str, Any]] = [
            {"trackName": "Yellow", "artistName": "Coldplay", "collectionName": "Parachutes"},
        ]
        summary = format_track_summary(raw_data)
        self.assertEqual(len(summary), 1)
        self.assertEqual(summary[0], "Track: 'Yellow' by 'Coldplay' [Parachutes]")

    def test_print_json_pretty(self) -> None:
        """Verify pretty printing dictionary to formatted JSON string."""
        sample_dict = {"status": "success", "code": 200}
        json_output = print_json_pretty(sample_dict)
        self.assertIn('"status": "success"', json_output)
        self.assertIn('"code": 200', json_output)


if __name__ == "__main__":
    unittest.main()
