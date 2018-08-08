from player import Player
from instruction_strings import INPUT_INFO, QUIT, WELCOME

# game states
STATE_OVER = "over"
STATE_INPUT = "input"
STATE_START = "start"

class Game:
    def __init__(self):
        self.family = {}
        self.input_done_str = "done"
        self.quit_str = "quit"
        self.start_str = "run"
        self.state = STATE_START

    def game_loop(self):
        while self.state != STATE_OVER:
            if self.state == STATE_START:
                self.handle_start()

            elif self.state == STATE_INPUT:
                self.handle_input()

        self.handle_quit()

    def get_family_members_str(self):
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

    def handle_input(self):
        print(INPUT_INFO.format(self.input_done_str))
        self.state = STATE_OVER

    def handle_start(self):
        welcome_input = input(WELCOME.format(self.start_str))
        self.state = STATE_INPUT if welcome_input == "run" else STATE_OVER

    def handle_quit(self):
        print(QUIT)

    def input_loop(self):
        done_inputting = False
        while not done_inputting:

            done_inputting = True

    def process_input_for_quit(self, string):
        should_quit = string.lower() == self.quit_str
        if should_quit:
            self.state = STATE_OVER
        return should_quit
