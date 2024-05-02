# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import Join, MapCompose, TakeFirst
from w3lib.html import remove_tags


class AircraftItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date_time = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    aircraft_type = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    operator = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    registration = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    flight_phase = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    flight_type = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    survivors = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    site_type = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    city = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    zone = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    country = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    region = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    schedule = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    construction_number = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    year_of_manufacture = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    flight_number = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    crew_on_board = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    crew_fatalities = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    pax_on_board = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    pax_fatalities = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    other_fatalities = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    total_fatalities = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    captain_total_flying_hours = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    captain_total_hours_on_type = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    copilot_total_flying_hours = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    copilot_total_hours_on_type = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    aircraft_flight_hours = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    crash_circumstances = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    crash_causes = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    photo_url = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
    URL = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=Join()
    )
