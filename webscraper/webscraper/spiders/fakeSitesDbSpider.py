import scrapy

class FakeSitesDbSpider(scrapy.Spider):
    name = 'fakeSites'
    start_urls = ['https://db.aa419.org/fakebankslist.php']                              # website to be web scraped

    def parse(self, response):
        for row in response.css ('table'):                                              # for every URL in table
            list = row.css('table tr td:nth-child(2) a::text').extract()
            print(list)# extract URLs
            for url in list:
                yield{
                    'url': url
                }


        next_page = response.css('div[class="pager"] a::attr(href)')[12].extract()          # go to the next page
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)                       # stop if theres no next page

