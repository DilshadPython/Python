"""
Book Resource Web Scraping Spider (`BookSpider`).

This module implements a Scrapy Spider for crawling and extracting Python book titles
and URLs using XPath selectors.
"""

# =========================================================================
# MODULE IMPORT EXPLANATION & PURPOSE:
# - `import scrapy`: Scrapy web scraping and crawling framework.
# - `from scrapy.http import Response`: Type annotation object for HTTP response handling.
# - `from typing import Generator, Dict, Any`: PEP 484 type hint generics.
# =========================================================================
from typing import Any, Dict, Generator
import scrapy
from scrapy.http import Response


class BookSpider(scrapy.Spider):
    """Spider for crawling Python programming books and resources directory."""

    name: str = "books"
    start_urls: list[str] = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/",
    ]

    def parse(self, response: Response) -> Generator[Dict[str, Any], None, None]:
        """Parse HTML response and extract book titles and URLs.

        Args:
            response (Response): Scrapy HTTP response object.

        Yields:
            Generator[Dict[str, Any], None, None]: Extracted item dictionary.
        """
        for book in response.xpath('//div[@class="title-and-desc"]/a'):
            yield {
                "name": book.xpath("div/text()").get(),
                "url": book.xpath("@href").get(),
            }
