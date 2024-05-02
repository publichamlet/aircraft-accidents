# import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import AircraftItem
from scrapy.loader import ItemLoader


class DataSpider(CrawlSpider):
    name = "data"
    allowed_domains = ["www.baaa-acro.com"]
    start_urls = ["https://www.baaa-acro.com/crash-archives"]
    # allowed_domains = ["www.rei.com"]
    # start_urls = ["https://www.rei.com/c/hiking-backpacks"]

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=(r"page="), deny=(r"field_crash_region_target_id=", r"field_crash_country_target_id=", r"field_crash_registration_target_id=", r"field_crash_aircraft_target_id=", r"field_crash_operator_target_id=",
             r"field_crash_cause_target_id=", r"field_crash_zone_target_id=", r"field_crash_site_type_target_id=", r"field_crash_phase_type_target_id=", r"field_crash_flight_type_target_id=", r"field_crash_survivors_value=", r"field_crash_city_target_id=", r"created=&created_1=&field_crash_region_target_id=All&field_crash_country_target_id&field_crash_registration_target_id&field_crash_aircraft_target_id&field_crash_operator_target_id&field_crash_cause_target_id=All&field_crash_zone_target_id&field_crash_site_type_target_id=All&field_crash_phase_type_target_id=All&field_crash_flight_type_target_id=All&field_crash_survivors_value=All&field_crash_city_target_id", r"crash-pictures",))),
        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=(r"crash",), deny=(
            r"https://www.baaa-acro.com/crash-archives",)), callback="parse_item"),
    )

    def parse_item(self, response):
        link = response.css('div.crash-details')
        link1 = response.css('div.crash-details').xpath('//a/div')

        loader = ItemLoader(item=AircraftItem(), response=response)

        loader.add_value('date_time', link.css(
            'div.crash-date::text').extract()[-1].strip())
        loader.add_value('aircraft_type', link1.css(
            'div.field.field--name-field-crash-aircraft::text').get())
        loader.add_value('operator', link.css(
            'div.crash-operator *::attr(href)').get().split('=')[-1])
        loader.add_value('registration', response.css(
            'div.crash-registration').xpath('div/text()').get())
        loader.add_value('flight_phase', link1.css(
            'div.field.field--name-field-crash-phase-type::text').get())
        loader.add_value('flight_type', link1.css(
            'div.field.field--name-field-crash-flight-type::text').get())
        loader.add_value('survivors', link1.css(
            'div.field.field--name-field-crash-survivors::text').get())
        loader.add_value('site_type', link1.css(
            'div.field.field--name-field-crash-site-type::text').get())
        loader.add_value('city', link1.css(
            'div.field.field--name-field-crash-city::text').get())
        loader.add_value('zone', link1.css(
            'div.field.field--name-field-crash-zone::text').get())
        loader.add_value('country', link1.css(
            'div.field.field--name-field-crash-country::text').get())
        loader.add_value('region', link1.css(
            'div.field.field--name-field-crash-region::text').get())
        loader.add_value('schedule', link.css(
            'div.field.field--name-field-crash-schedule::text').get())
        loader.add_value('construction_number', link.css(
            'div.field.field--name-field-crash-construction-number::text').get())
        loader.add_value('year_of_manufacture', link.css(
            'div.field.field--name-field-year-of-manufacture::text').get())
        loader.add_value('flight_number', link.css(
            'div.field.field--name-field-crash-flight-number::text').get())
        loader.add_value('crew_on_board', link.css(
            'div.field.field--name-field-crew-on-board::text').get())
        loader.add_value('crew_fatalities', link.css(
            'div.field.field--name-field-crew-fatalities::text').get())
        loader.add_value('pax_on_board', link.css(
            'div.field.field--name-field-pax-on-board::text').get())
        loader.add_value('pax_fatalities', link.css(
            'div.field.field--name-field-pax-fatalities::text').get())
        loader.add_value('other_fatalities', link.css(
            'div.field.field--name-field-other-fatalities::text').get())
        loader.add_value('total_fatalities', link.css(
            'div.field.field--name-field-final-total-fatalities::text').get())
        loader.add_value('captain_total_flying_hours', link.css(
            'div.field.field--name-field-captain-total-flying-hours::text').get())
        loader.add_value('captain_total_hours_on_type', link.css(
            'div.field.field--name-field-total-hours-on-type::text').get())
        loader.add_value('copilot_total_flying_hours', link.css(
            'div.field.field--name-field-copilot-total-flying-hours::text').get())
        loader.add_value('copilot_total_hours_on_type', link.css(
            'div.field.field--name-field-copilot-total-hour-on-type::text').get())
        loader.add_value('aircraft_flight_hours', link.css(
            'div.field.field--name-field-aircraft-flight-hours::text').get())
        loader.add_value('crash_circumstances', link.css(
            'div.field.field--name-field-crash-circumstances::text').get())
        loader.add_value('crash_causes', link.css(
            'div.field.field--name-field-crash-causes::text').get())
        loader.add_value('photo_url', response.xpath(
            '//a[contains(@href, ".jpg")]/@href').extract())
        loader.add_value('URL', response.url)

        return loader.load_item()
