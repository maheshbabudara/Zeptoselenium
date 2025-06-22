from Lib.library import Base
from time import sleep
from Utilities.country_locator import Country_locator

class practise(Base):
    def prac(self):
        self.webtables(Country_locator.row_locator,Country_locator.col_locator)
        sleep(2)
