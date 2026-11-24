"""
Advanced REST API Client and Multi-Endpoint Integration Module.

This module implements an object-oriented REST API client (`PokeApiClient`) for querying
the public PokéAPI endpoints (`/pokemon/{name}` and `/ability/{name}`).

Features:
- Encapsulated REST client architecture
- Multiple resource endpoints routing
- HTTP status validation and error exceptions
- Data normalization and clean error messaging

PEP 8 compliant, type-annotated, compatible with Python 2.7 - 3.13.
"""

# Standard library imports for JSON processing, URL handling, and HTTP calls
import json
import sys
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional


class PokeApiError(Exception):
    """Custom exception raised when PokéAPI requests encounter failures."""
    pass


class PokeApiClient:
    """
    Object-oriented client for interacting with PokéAPI REST endpoints.
    """

    BASE_URL = "https://pokeapi.co/api/v2"

    def __init__(self, base_url: Optional[str] = None, timeout: int = 10) -> None:
        """
        Initializes PokeApiClient instance.

        Args:
            base_url (Optional[str]): Base URL for PokéAPI (defaults to https://pokeapi.co/api/v2).
            timeout (int): Request timeout in seconds (default: 10).
        """
        self.base_url = (base_url or self.BASE_URL).rstrip("/")
        self.timeout = timeout

    def _get(self, endpoint: str) -> Dict[str, Any]:
        """
        Internal helper to execute GET HTTP requests to specified endpoint.

        Args:
            endpoint (str): Relative API path (e.g. '/pokemon/ditto').

        Returns:
            Dict[str, Any]: Decoded JSON payload dictionary.

        Raises:
            PokeApiError: If HTTP status is non-200 or request fails.
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "Python-PokeAPI-Client/1.0"}
        )

        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                status_code = response.getcode()
                if status_code != 200:
                    raise PokeApiError(f"HTTP Status {status_code} for endpoint: {url}")
                content = response.read().decode("utf-8")
                return json.loads(content)
        except Exception as err:
            raise PokeApiError(f"Failed API request to '{url}': {err}") from err

    def get_pokemon(self, name: str) -> Dict[str, Any]:
        """
        Fetches detailed information for a specific Pokémon by name or ID.

        Args:
            name (str): Pokémon identifier (e.g., 'ditto', 'pikachu').

        Returns:
            Dict[str, Any]: Formatted Pokémon details dictionary.
        """
        raw_data = self._get(f"pokemon/{name.lower()}")
        return {
            "name": raw_data.get("name", "").upper(),
            "id": raw_data.get("id"),
            "height": raw_data.get("height"),
            "weight": raw_data.get("weight"),
            "base_experience": raw_data.get("base_experience"),
        }

    def get_ability(self, ability_name: str) -> Dict[str, Any]:
        """
        Fetches ability details from the ability endpoint.

        Args:
            ability_name (str): Ability name (e.g., 'battle-armor').

        Returns:
            Dict[str, Any]: Formatted ability details dictionary.
        """
        raw_data = self._get(f"ability/{ability_name.lower()}")
        return {
            "name": raw_data.get("name", "").upper(),
            "id": raw_data.get("id"),
            "is_main_series": raw_data.get("is_main_series"),
            "generation": raw_data.get("generation", {}).get("name"),
        }


if __name__ == "__main__":
    client = PokeApiClient()
    pokemon_list = ["ditto", "pikachu"]

    print("Fetching Pokémon Details from PokéAPI:")
    for poke in pokemon_list:
        try:
            info = client.get_pokemon(poke)
            print(f"  Name: {info['name']} (ID: {info['id']}) | Height: {info['height']} | Weight: {info['weight']}")
        except PokeApiError as err:
            print(f"  Error fetching '{poke}': {err}")
