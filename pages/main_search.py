from playwright.sync_api import Page, sync_playwright, expect


class MainSearchPage:

    URL = "https://www.esky.pl/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.accept_cookies_button = page.get_by_test_id("uc-accept-all-button")
        self.departure_field = page.locator("#departureRoundtrip0")
        self.departure_airport_list = page.get_by_text("Warszawa, Chopina, mazowieckie, Polska (WAW)")
        self.arrival_field = page.locator("#arrivalRoundtrip0")
        self.arrival_airport_list = page.get_by_text("Funchal, Madera, Madera, Portugalia (FNC)")
        self.departure_date = page.locator("#departureDateRoundtrip0")
        self.return_date = page.locator("#departureDateRoundtrip1")
        self.search_button = page.get_by_role("button", name="Szukaj lotu")

    def open_esky(self) -> None:
        self.page.goto(self.URL)

    def accept_cookies(self) -> None:
        self.accept_cookies_button.click()

    def search_departure(self, departure_airport: str) -> None:
        self.departure_field.fill(departure_airport)
        self.departure_airport_list.click()

    def search_arrival(self, arrival_airport: str) -> None:
        self.arrival_field.fill(arrival_airport)
        self.arrival_airport_list.click()

    def set_departure_date(self):
        self.departure_date.click()

    def set_return_date(self):
        self.return_date.click()






