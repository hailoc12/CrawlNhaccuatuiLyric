# -*- coding: utf-8 -*-
import scrapy


class NhaccuatuiSpider(scrapy.Spider):
    name = 'nhaccuatui'
    allowed_domains = ['nhaccuatui.com']
    start_urls = ["https://www.nhaccuatui.com/bai-hat/rap-viet-moi.html"]

    def parse(self, response):
        finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract()
        totalPage = int(finalPage.split(".")[-2])
        # print(finalPage)
        for page in range(totalPage):
            link = finalPage.replace(str(totalPage), str(page + 1))
            # print(link)
            yield scrapy.Request(link, callback=self.crawlLyric)

    def crawlLyric(self, response):
        # print(response)
        for linkLyric in response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="list_music_full"]/div[@class="fram_select"]/ul[@class="list_item_music"]/li/a[@class="button_new_window"]/@href').extract():
            # print(linkLyric)
            yield scrapy.Request(linkLyric, callback=self.saveFile)

    def saveFile(self, response):
        lyricRaw = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="lyric"]/p[@id="divLyric"]/text()').extract()
        # print(lyric)
        if len(lyricRaw) > 5:
            lyric = "\n".join(lyricRaw)
            print(lyric)
            with open("lyricRap/%s.txt" % response.url.split("/")[-1], "w+") as f:
                f.write(lyric)

# class NhaccuatuiSpider(scrapy.Spider):
#     name = 'nhaccuatui'
#     allowed_domains = ['nhaccuatui.com']
#     start_urls = ["https://www.nhaccuatui.com/bai-hat/thieu-nhi-moi.html"]
#
#     def parse(self, response):
#         finalPage = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="box_pageview"]/a/@href')[-1].extract()
#         totalPage = int(finalPage.split(".")[-2])
#         # print(finalPage)
#         for page in range(totalPage):
#             link = finalPage.replace(str(totalPage), str(page + 1))
#             # print(link)
#             yield scrapy.Request(link, callback=self.crawlLyric)
#
#     def crawlLyric(self, response):
#         # print(response)
#         for linkLyric in response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="list_music_full"]/div[@class="fram_select"]/ul[@class="list_item_music"]/li/a[@class="button_new_window"]/@href').extract():
#             # print(linkLyric)
#             yield scrapy.Request(linkLyric, callback=self.saveFile)
#
#     def saveFile(self, response):
#         lyricRaw = response.xpath('//div[@class="box-content"]/div[@class="wrap"]/div[@class="content-wrap"]/div[@class="box-left"]/div[@class="lyric"]/p[@id="divLyric"]/text()').extract()
#         # print(lyric)
#         if len(lyricRaw) > 5:
#             lyric = "\n".join(lyricRaw)
#             # print(lyric)
#             with open("lyricThieuNhi/%s.txt" % response.url.split("/")[-1], "w+") as f:
#                 f.write(lyric)
