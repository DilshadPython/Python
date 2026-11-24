"""
Quotes Scraper Spider using XPath Selectors (`QuotesXPathSpider`).

This module demonstrates web scraping quote text, authors, and tag lists using Scrapy XPath queries.
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


class QuotesXPathSpider(scrapy.Spider):
    """Spider for crawling quotes.toscrape.com using XPath expressions."""

    name: str = "toscrap-xpath"
    start_urls: list[str] = ["http://quotes.toscrape.com/"]

    def parse(self, response: Response) -> Generator[Dict[str, Any], None, None]:
        """Parse quotes response using XPath expressions and yield structured items.

        Args:
            response (Response): Scrapy HTTP response object.

        Yields:
            Generator[Dict[str, Any], None, None]: Quote item dictionary.
        """
        for quote in response.xpath('//div[@class="quote"]'):
            yield {
                "text": quote.xpath('./span[@class="text"]/text()').get(),
                "author": quote.xpath('.//small[@class="author"]/text()').get(),
                "tags": quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall(),
            }
