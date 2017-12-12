import scrapy


class ToScrapSpiderXPath(scrapy.Spider):
	name = 'toscrap-xpath'
	start_urls = ['http://quotes.toscrape.com/']

	def parse(self,response):
		for quote in response.xpath('//div[@class="quote"]'):
			yield {
				'text': quote.xpath('./span[@class="text"]/text()').extract_first(),
				'author': quote.xpath('.//small[@class="author"]/text()').extract_first(),
				'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract(),
			}
