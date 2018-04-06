import scrapy


class AssigementSpider(scrapy.Spider):
	name = 'SquirrelSave'
	url = ['https://www.squirrelsave.co.uk/']


	def parse(self, response):
		for title in response.xpath(''):
			yield {
				'title': title.xpath('').extract_first()
			}
