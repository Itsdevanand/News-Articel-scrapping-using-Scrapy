

import scrapy
from datetime import datetime

class newsscrap(scrapy.Spider):
    name = 'news'
    start_urls = ['https://www.infoq.com/ai-ml-data-eng/news/']
    
    def parse(self, response):
        
        item = response.css('div.card__data')
        #extracting data
        title = item.css('h3.card__title').css('a::text').extract()
        link = item.css('h3.card__title').css('a::attr(href)').extract()
        news_tag  = item.css('div.card__topics.topics').css('a::text').extract()
        news_author = item.css('div.card__authors.authors').css('a::text').extract()
        content = item.css('p.card__excerpt::text').extract()[5:] #Avoiding first 5 entries
        date = item.css('span.card__date.date').css('span::text').extract()
        
        date1 = list(filter(lambda x: (x != 'on'), date)) #used to filter 'no' word 
        
        news_link = ['https://www.infoq.com/' + x for x in link] #preprocessing url text to add the missing part
        
        news_content = [x.lstrip() for x in content] #removing left space
        
        news_title = [x.lstrip() for x in title] #removing left space
        
        def date_conv(d):#Function for converting date format
            return datetime.strptime(d, '%b %d, %Y').strftime('%m/%d/%Y') 
        
        
        news_date  = [date_conv(x.lstrip()) for x in date1] #converting date format
        
        
        for i in zip(news_date,news_tag,news_title,news_content,news_author,news_link):
            news_info = {
                
                'article_date'       :   i[0],
                'article_tag'        :   i[1],
                'article_title'      :   i[2],
                'author_description' :   i[3],
                'article_author'     :   i[4],
                'article_url'        :   i[5]
                
            }
            
            yield news_info

        
                
                
                
                   
        
            
        