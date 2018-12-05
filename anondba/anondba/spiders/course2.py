# -*- coding: utf-8 -*-
import scrapy
from anondba.items import AnondbaItem

class Course2Spider(scrapy.Spider):
    name = 'course2'

    @property
    def start_urls(self):
        url_tmpl='https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
        return (url_tmpl.format(i) for i in range(1,23))



    def parse(self, response):
        for a in response.css('div.course-body'):
            item = AnondbaItem({
                'name':course.css('div.course-name::text').extract_first(),
                'desc':course.css('div.course-desc::text').extract_first(),
                'type':course.css('div.course-footer span.pull-right::text').extract_first(default='free')
                })
            yield item
