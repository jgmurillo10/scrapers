import scrapy

class CarsSpider(scrapy.Spider):
    name = "cars"
    start_urls = [
            'https://carros.tucarro.com.co/',
        ]

    def parse(self, response):
        for car in response.css('li.results-item'):
            yield {
                'title': car.css('span.main-title::text').get(),
                'price': car.css('span.price__fraction::text').get(),
                'year': car.css('div.item__attrs::text').get().split("|")[0].strip(),
                'km': car.css('div.item__attrs::text').get().split("|")[1].strip(),
                'location': car.css('div.item__location::text').get(),
            }
        # for a in response.css('andes-pagination__button andes-pagination__button--current + andes-pagination__button'):
        #     yield response.follow(a, callback=self.parse)

        # for href in response.css('li.andes-pagination__button--next a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)
        
        # page = response.url.split("/")[-2]
        # filename = 'quotes-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log('Saved files %s' % filename)

# for car in response.css('li.results-item'):
#     title = car.css('span.main-title::text').get()
#     price = car.css('span.price__fraction::text').get()
#     year = car.css('div.item__attrs::text').get().split("|")[0].strip()
#     km = car.css('div.item__attrs::text').get().split("|")[1].strip()
#     location = car.css('div.item__location::text').get()
#     print(dict(title=title,price=price,year=year,km=km,location=location))