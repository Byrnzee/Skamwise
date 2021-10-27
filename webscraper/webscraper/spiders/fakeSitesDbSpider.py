import scrapy

class FakeSitesDbSpider(scrapy.Spider):
    name = 'fakeSites'
    start_urls = ['https://db.aa419.org/fakebankslist.php']

    def parse(self, response):
        for row in response.css ('table.ewTable'):
            yield{
                'url': row.css('tr td:nth-child(2) a::attr(href)').extract()

            }

        next_page = response.css('div[id="main"] a::attr(href)')[14].extract()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

