from instruction_strings import INPUT_INFO, INPUT_MEMBER_0, INPUT_MEMBER_1, INPUT_MEMBER_2, INPUT_STOP, QUIT, WELCOME
from family_printer import family_printer
from player import Player

# game states
STATE_INPUT = "input"
STATE_OVER = "over"
STATE_PROCESS = "process"
STATE_START = "start"

class Game:
    def __init__(self):
        self.family = {}
        self.input_done_str = "done"
        self.quit_str = "quit"
        self.start_str = "run"
        self.state = STATE_START

    def add_member(self, name, partner_name, gift):
        self.family[name] = Player(name, partner_name, gift)

    def game_loop(self):
        while self.state != STATE_OVER:
            if self.state == STATE_START:
                self.handle_start()

            elif self.state == STATE_INPUT:
                self.handle_input()

            elif self.state == STATE_PROCESS:
                self.state = STATE_OVER

        self.handle_quit()

    def handle_input(self):
        print(INPUT_INFO.format(self.input_done_str))
        self.input_loop()

    def handle_start(self):
        welcome_input = input(WELCOME.format(self.start_str)).lower()
        self.state = STATE_INPUT if welcome_input == self.start_str else STATE_OVER

    def handle_quit(self):
        print(QUIT)

    def input_loop(self):
        while self.state == STATE_INPUT:
            family_printer(self.family)

            new_name = input(INPUT_MEMBER_0)
            new_partner_name = input(INPUT_MEMBER_1)
            new_gift = input(INPUT_MEMBER_2)
            print()

            self.add_member(new_name, new_partner_name, new_gift)

            # check to stop input
            if input(INPUT_STOP.format(self.input_done_str)).lower() == self.input_done_str:
                self.state = STATE_PROCESS

    def print_unique_family_members(self):
        names = self.family.keys()
        partner_map = {}


        for name in names:
            if (name not in partner_map and
                self.family[name].partner_name not in partner_map):
                partner_map[name] = self.family[name].partner_name

        return "\n".join([
            str((name, partner_map[name])) if partner_map[name] != None else name
                for name in partner_map.keys()
        ])

    def process_input_for_quit(self, string):
        should_quit = string.lower() == self.quit_str
        if should_quit:
            self.state = STATE_OVER
        return should_quit
