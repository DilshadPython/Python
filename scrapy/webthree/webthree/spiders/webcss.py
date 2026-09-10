"""
Quotes Scraper Spider using CSS Selectors (`QuotesCSSSpider`).

This module demonstrates web scraping quote text, authors, and tag lists using Scrapy CSS selectors.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import scrapy`: Scrapy crawling framework for HTML parsing.
# - `from scrapy.http import Response`: Type hint for HTTP response.
# - `from typing import Generator, Dict, Any`: PEP 484 type hint generics.
# =========================================================================
from typing import Any, Dict, Generator
import scrapy
from scrapy.http import Response


class QuotesCSSSpider(scrapy.Spider):
    """Spider for crawling quotes.toscrape.com using CSS selectors."""

    name: str = "toscrap-css"
    start_urls: list[str] = ["http://quotes.toscrape.com/"]

    def parse(self, response: Response) -> Generator[Dict[str, Any], None, None]:
        """Parse quotes response using CSS selectors and yield structured items.

        Args:
            response (Response): Scrapy HTTP response object.

        Yields:
            Generator[Dict[str, Any], None, None]: Quote item dictionary.
        """
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags > a.tag::text").getall(),
            }
