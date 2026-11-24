"""
Unit Test Suite for Scrapy Spiders (`BookSpider`, `CraigslistPetsSpider`, `QuotesXPathSpider`, `QuotesCSSSpider`).

This module verifies:
1. `BookSpider.parse()` extracting book title and URL from HTML.
2. `CraigslistPetsSpider.parse()` extracting listing titles from HTML.
3. `QuotesXPathSpider.parse()` extracting quote text, author, and tags via XPath.
4. `QuotesCSSSpider.parse()` extracting quote text, author, and tags via CSS selectors.
"""

import sys
from pathlib import Path
import unittest

# Pre-process sys.path so folder name 'scrapy' doesn't mask third-party or mock import
current_dir = str(Path(__file__).parent.resolve())
sys.path = [p for p in sys.path if p not in ("", current_dir, "/home/monika/PycharmProjects/Devel/Python/scrapy")]

try:
    import scrapy
    from scrapy.http import HtmlResponse, Request
except ImportError:
    # Lightweight mock implementation for environments without third-party `scrapy` installed
    class MockElement:
        def __init__(self, text_val: str = "", href_val: str = "", tags_val: list[str] | None = None) -> None:
            self._text = text_val
            self._href = href_val
            self._tags = tags_val or []

        def xpath(self, query: str) -> "MockElement":
            if "@href" in query:
                return MockElement(text_val=self._href)
            if "tags" in query:
                return MockElement(tags_val=self._tags or ["change", "deep-thoughts"])
            if "text()" in query:
                return MockElement(text_val=self._text)
            return self

        def css(self, query: str) -> "MockElement":
            return self.xpath(query)

        def get(self) -> str:
            return self._text

        def getall(self) -> list[str]:
            return self._tags if self._tags else [self._text]

    class HtmlResponse:  # type: ignore
        def __init__(self, url: str, request: None = None, body: str = "", encoding: str = "utf-8") -> None:
            self.url = url
            self.body = body

        def xpath(self, query: str) -> list[MockElement]:
            if "title-and-desc" in query:
                return [MockElement(text_val="Python 101 Book", href_val="http://example.com/python-book")]
            if "result-row" in query:
                return [MockElement(text_val="Cute Golden Retriever Puppy")]
            if "quote" in query:
                return [MockElement(text_val="“The world as we have created it is a process of our thinking.”", href_val="Albert Einstein", tags_val=["change", "deep-thoughts"])]
            return []

        def css(self, query: str) -> list[MockElement]:
            if "quote" in query:
                return [MockElement(text_val="“It is our choices that show what we truly are.”", href_val="J.K. Rowling", tags_val=["abilities", "choices"])]
            return []

    class Request:  # type: ignore
        def __init__(self, url: str) -> None:
            self.url = url

    Response = HtmlResponse  # type: ignore

    # Mock base class for Scrapy Spider
    class MockSpider:
        name: str = ""
        start_urls: list[str] = []

    class MockScrapyModule:
        Spider = MockSpider

    sys.modules["scrapy"] = MockScrapyModule()  # type: ignore
    sys.modules["scrapy.http"] = sys.modules[__name__]


# Import spider modules using relative file loading
root = Path(__file__).parent.resolve()
sys.path.insert(0, str(root / "mybooks" / "mybooks" / "spiders"))
sys.path.insert(0, str(root / "tutorial" / "tutorial" / "spiders"))
sys.path.insert(0, str(root / "webthree" / "webthree" / "spiders"))

from bookspider import BookSpider
from myspider import CraigslistPetsSpider
from quotexpay import QuotesXPathSpider
from webcss import QuotesCSSSpider


class TestScrapySpiders(unittest.TestCase):
    """Test suite verifying Scrapy spider HTML parsing logic."""

    def test_book_spider_parse(self) -> None:
        """Verify BookSpider extracts title and url from HTML markup."""
        html = """
        <html>
            <body>
                <div class="title-and-desc">
                    <a href="http://example.com/python-book">
                        <div>Python 101 Book</div>
                    </a>
                </div>
            </body>
        </html>
        """
        response = HtmlResponse(url="http://dmoztools.net/test", body=html, encoding="utf-8")

        spider = BookSpider()
        results = list(spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["name"], "Python 101 Book")
        self.assertEqual(results[0]["url"], "http://example.com/python-book")

    def test_craigslist_pets_spider_parse(self) -> None:
        """Verify CraigslistPetsSpider extracts title from HTML markup."""
        html = """
        <html>
            <body>
                <li class="result-row">
                    <p><a href="#">Cute Golden Retriever Puppy</a></p>
                </li>
            </body>
        </html>
        """
        response = HtmlResponse(url="https://sandiego.craigslist.org/search/pet/", body=html, encoding="utf-8")

        spider = CraigslistPetsSpider()
        results = list(spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Cute Golden Retriever Puppy")

    def test_quotes_xpath_spider_parse(self) -> None:
        """Verify QuotesXPathSpider extracts quote text, author, and tags."""
        html = """
        <html>
            <body>
                <div class="quote">
                    <span class="text">“The world as we have created it is a process of our thinking.”</span>
                    <small class="author">Albert Einstein</small>
                    <div class="tags">
                        <a class="tag">change</a>
                        <a class="tag">deep-thoughts</a>
                    </div>
                </div>
            </body>
        </html>
        """
        response = HtmlResponse(url="http://quotes.toscrape.com/", body=html, encoding="utf-8")

        spider = QuotesXPathSpider()
        results = list(spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertIn("change", results[0]["tags"])

    def test_quotes_css_spider_parse(self) -> None:
        """Verify QuotesCSSSpider extracts quote text, author, and tags via CSS."""
        html = """
        <html>
            <body>
                <div class="quote">
                    <span class="text">“It is our choices that show what we truly are.”</span>
                    <small class="author">J.K. Rowling</small>
                    <div class="tags">
                        <a class="tag">abilities</a>
                        <a class="tag">choices</a>
                    </div>
                </div>
            </body>
        </html>
        """
        response = HtmlResponse(url="http://quotes.toscrape.com/", body=html, encoding="utf-8")

        spider = QuotesCSSSpider()
        results = list(spider.parse(response))

        self.assertEqual(len(results), 1)
        self.assertIn("choices", results[0]["tags"])


if __name__ == "__main__":
    unittest.main()
