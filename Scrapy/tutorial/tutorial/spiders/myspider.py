import scrapy


class TheSpider(scrapy.Spider):
    name = 'toget-title'
    starts_urls = ['https://sandiego.craigslist.org/search/pet/']

    def parse(self, response):
        for title in response.xpath("//li[@class='result-row']//p"):
            yield {
                'title': title.xpath('a/text()').extract_first()
            }
