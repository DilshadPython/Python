"""
Unit Test Suite for Advanced REST API Client Module.

Mocks urllib.request.urlopen to test PokeApiClient endpoints (/pokemon/{name},
/ability/{name}), status handling, custom PokeApiError exceptions, and data extraction.
"""

import json
import unittest
from unittest.mock import MagicMock, patch
from typing import Any, Dict

from advanced_api_client import PokeApiClient, PokeApiError


class TestAdvancedApiClient(unittest.TestCase):
    """Test cases for PokeApiClient REST API client."""

    def setUp(self) -> None:
        """Initialize PokeApiClient instance before each test."""
        self.client = PokeApiClient()

    @patch("advanced_api_client.urllib.request.urlopen")
    def test_get_pokemon_success(self, mock_urlopen: MagicMock) -> None:
        """Verify successful Pokémon endpoint data fetching and parsing."""
        mock_payload: Dict[str, Any] = {
            "name": "pikachu",
            "id": 25,
            "height": 4,
            "weight": 60,
            "base_experience": 112,
        }
        json_bytes = json.dumps(mock_payload).encode("utf-8")

        mock_cm = MagicMock()
        mock_cm.getcode.return_value = 200
        mock_cm.read.return_value = json_bytes
        mock_cm.__enter__.return_value = mock_cm

        mock_urlopen.return_value = mock_cm

        info = self.client.get_pokemon("pikachu")
        self.assertEqual(info["name"], "PIKACHU")
        self.assertEqual(info["id"], 25)
        self.assertEqual(info["height"], 4)
        self.assertEqual(info["weight"], 60)

    @patch("advanced_api_client.urllib.request.urlopen")
    def test_get_ability_success(self, mock_urlopen: MagicMock) -> None:
        """Verify successful Ability endpoint fetching."""
        mock_payload: Dict[str, Any] = {
            "name": "battle-armor",
            "id": 4,
            "is_main_series": True,
            "generation": {"name": "generation-iii"},
        }
        json_bytes = json.dumps(mock_payload).encode("utf-8")

        mock_cm = MagicMock()
        mock_cm.getcode.return_value = 200
        mock_cm.read.return_value = json_bytes
        mock_cm.__enter__.return_value = mock_cm

        mock_urlopen.return_value = mock_cm

        ability = self.client.get_ability("battle-armor")
        self.assertEqual(ability["name"], "BATTLE-ARMOR")
        self.assertEqual(ability["id"], 4)
        self.assertTrue(ability["is_main_series"])
        self.assertEqual(ability["generation"], "generation-iii")

    @patch("advanced_api_client.urllib.request.urlopen")
    def test_api_error_raised_on_failure(self, mock_urlopen: MagicMock) -> None:
        """Verify PokeApiError is raised on HTTP network failure."""
        mock_urlopen.side_effect = Exception("404 Not Found")

        with self.assertRaises(PokeApiError):
            self.client.get_pokemon("unknown_pokemon")


if __name__ == "__main__":
    unittest.main()
