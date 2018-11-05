import scrapy


class BookSpider(scrapy.Spider):
    name = 'books'
    start_urls = [
        'http://dmoztools.net/Computers/Programming/Languages/Python/Books/',
        'http://dmoztools.net/Computers/Programming/Languages/Python/Resources/',
    ]

    def parse(self, response):
        for book in response.xpath('//div[@class="title-and-desc"]/a'):
            yield {
                'name': book.xpath('div/text()').extract_first(),
                'url': book.xpath('@href').extract_first(),
            }
