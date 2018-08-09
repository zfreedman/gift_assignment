from instruction_strings import instructions
from family_printer import family_printer
from family_reader import read_family
from player import Player
from random import shuffle

# game states
STATE_INPUT = "input"
STATE_OVER = "over"
STATE_PROCESS = "process"
STATE_START = "start"

class Game:
    def __init__(self):
        self.family = {}
        self.input_done_str = "done"
        self.invalid_str = "INVALID"
        self.max_iterations = 100
        self.quit_str = "quit"
        self.start_str = "run"
        self.valid_str = "VALID"
        self.state = STATE_START

    def add_member(self, name, partner_name, gift):
        self.family[name] = Player(name, partner_name, gift)

    def check_game_order_validity(self, picker_order, hat_order):
        for i in range(len(picker_order)):

            if (picker_order[i] == hat_order[i]
                or self.family[picker_order[i]].partner_name == hat_order[i]):

                return False
        return True

    def game_loop(self):
        while self.state != STATE_OVER:
            if self.state == STATE_START:
                self.handle_start()

            elif self.state == STATE_INPUT:
                self.handle_input()

            elif self.state == STATE_PROCESS:
                self.handle_process()

        self.handle_quit()

    def get_random_family_order(self):
        names = list(self.family.keys())
        shuffle(names)
        return names

    def handle_input(self):
        #inform
        print(instructions["INPUT_INFO"].format(self.input_done_str))
        #family member input
        self.input_loop()
        #max iterations input
        self.handle_iterations_input()
        #leave process state
        self.state = STATE_PROCESS

    def handle_iterations_input(self):
        #max iteration input
        try:
            max_iterations = int(input(instructions["INPUT_MAX_ITERATIONS"]))
        except:
            max_iterations = 100
        self.max_iterations = max_iterations

    def handle_process(self, log=True):
        if log:
            print(instructions["PROCESS_INFO"])

        orders_are_valid = False
        count = 0
        while not orders_are_valid and count < self.max_iterations:
            picker_order = self.get_random_family_order()
            hat_order = self.get_random_family_order()
            orders_are_valid = self.check_game_order_validity(picker_order, hat_order)
            count += 1

            if log:
                print("\n{}".format(count))
                print(self.valid_str if orders_are_valid else self.invalid_str)
                print(instructions["PROCESS_LIST_DISPLAY"].format(picker_order, hat_order))

        self.state = STATE_OVER

        return (orders_are_valid, picker_order, hat_order)

    def handle_start(self):
        welcome_input = input(instructions["WELCOME"].format(self.start_str)).lower()
        self.state = STATE_INPUT if welcome_input == self.start_str else STATE_OVER

    def handle_quit(self):
        print(instructions["QUIT"])

    def input_loop(self):
        while True:
            print()
            family_printer(self.family)

            new_name = input(instructions["INPUT_MEMBER_0"])
            new_partner_name = input(instructions["INPUT_MEMBER_1"])
            new_gift = input(instructions["INPUT_MEMBER_2"])

            self.add_member(new_name, new_partner_name, new_gift)

            # check to stop input
            if input(
                instructions["INPUT_MEMBER_STOP"].format(self.input_done_str)
            ).lower() == self.input_done_str:
                break

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
