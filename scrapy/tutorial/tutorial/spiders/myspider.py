"""
Craigslist Pets Web Scraping Spider (`CraigslistPetsSpider`).

This module implements a Scrapy Spider for extracting listing titles from classifieds.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import scrapy`: Scrapy crawling framework for web data extraction.
# - `from scrapy.http import Response`: Type annotation for Scrapy HTTP response object.
# - `from typing import Generator, Dict, Any`: PEP 484 type hint generics.
# =========================================================================
from typing import Any, Dict, Generator
import scrapy
from scrapy.http import Response


class CraigslistPetsSpider(scrapy.Spider):
    """Spider for crawling Craigslist pet listing titles."""

    name: str = "toget-title"
    start_urls: list[str] = ["https://sandiego.craigslist.org/search/pet/"]

    def parse(self, response: Response) -> Generator[Dict[str, Any], None, None]:
        """Parse Craigslist search response and yield listing titles.

        Args:
            response (Response): Scrapy HTTP response object.

        Yields:
            Generator[Dict[str, Any], None, None]: Extracted title item dictionary.
        """
        for title in response.xpath("//li[@class='result-row']//p"):
            yield {
                "title": title.xpath("a/text()").get(),
            }
