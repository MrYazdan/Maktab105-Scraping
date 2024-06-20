import scrapy


class MaktabSpider(scrapy.Spider):
    name = 'maktab'
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        for title in response.css('.oxy-post-title'):
            data = {'title': title.css('::text').get()}
            self.log(" 🗂️  " + data['title'])
            yield data

        for next_page in response.css('a.next'):
            yield response.follow(next_page, self.parse)
