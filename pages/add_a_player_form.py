from pages.base_page import BasePage


class AddaPlayerPage(BasePage):
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    expected_title = "Add player"

    def title_of_page(self):
        assert self.get_page_title(self.add_player_url) == self.expected_title

