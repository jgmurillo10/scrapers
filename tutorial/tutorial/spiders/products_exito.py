import scrapy
# scrapy shell 'https://www.exito.com/browse'
class ProductsSpider(scrapy.Spider):
    name = "products"
    start_urls = [
            'https://www.exito.com/browse',
        ]

    def parse(self, response):
        for product in response.css('div.product'):
            price_before = product.css('s.money::text').get()
            yield {
                'id': product.xpath("@id").get(),
                'classifcation': product.xpath("@data-prdtype").get(),
                'name': product.css('span.name::text').get(),
                'price': product.css('span.money::text').get(),
                'price_before': price_before if  price_before else product.css('span.money::text').get(),
                'brand': product.css('span.brand::text').get(),
            }
        # uncomment for recursive crawling
        for a in response.css('li.active + li a'):
            yield response.follow(a, callback=self.parse)
