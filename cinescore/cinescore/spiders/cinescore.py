import scrapy

class CineScore(scrapy.Spider):
    """Scraping bot"""

    name = 'cinescore'
    movie = 'inception'

    start_urls = [
        f'https://www.rottentomatoes.com/search?search={movie}'
    ]

    def parse(self, response):
        """Scrapes the link"""

        #! SEARCH
        for result in response.css('search-page-media-row'):
            data = {
                'name': str(result.css('a.unset[slot=title]::text').get()).strip(),
                'link': result.css('a.unset::attr(href)').get()
            }
            yield data


        #! HOMEPAGE
        # for movie in response.css('a[data-track=scores]'):
        #     yield {
        #         'name': movie.css('span.p--small::text').get(),
        #         'ratings': movie.css('rt-text::text').get()

        #     }