# -*- coding: utf-8 -*-
import scrapy
import json

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        url='https://www.presidencia.gov.py/tmpl/grillas/nomina.php'
        for i in range(24):
            yield scrapy.FormRequest(url=url,
                                     method='POST',
                                     formdata={'page':str(i + 1),'rows':'16'})





    def parse(self, response):
        rows = json.loads(response.body)['rows']
        for row in rows:
            yield {
                'Nro': row['cell'][0],
                'Nombre y Apellido': row['cell'][1],
                'Cargo': row['cell'][2],
                'Total': row['cell'][3],
                'Sueldo': row['cell'][4],
                'G.Represent.': row['cell'][5],
                'Bonificación': row['cell'][6],
                'Tipo': row['cell'][7]
            }