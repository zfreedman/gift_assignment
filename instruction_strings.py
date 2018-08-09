player_name = "Mr. Raccoon"

INPUT_INFO = """\nGreat! Here's how family member input works.
We'll prompt you for a family member's name, their partner's name, and the member's gift.
We'll continue to do this until you tell us you're done, which you can indicate by typing "{}"."""

INPUT_MEMBER_0 = """\nName: """
INPUT_MEMBER_1 = """Partner Name (hit ENTER for no partner): """
INPUT_MEMBER_2 = """Gift: """

INPUT_STOP = """\nType "{}" if you are done inputting family members: """

PROCESS_INFO = """\nFantastic! All family members have been entered.
What we'll do now is randomize the order of the family members. Then, to simulate
"random picking", we'll randomize a second list of the same family members. The
first list represents WHO is picking FROM the hat, whereas the second list
represents WHICH name the WHO will pickself.

New lists will be generated until two lists are returned which correspond to NO
family members picking their or their partner's name."""

PROCESS_LIST_DISPLAY = """Pick Order: {}\nHat Order: {}\n"""

QUIT = """\nThanks for playing {}\n""".format(player_name)

WELCOME = """Welcome {}.
Would you like to run the application?
To run, type "{}". The application will quit otherwise: """.format(player_name, "{}")

instructions = {
    "INPUT_INFO": INPUT_INFO,
    "INPUT_MEMBER_0": INPUT_MEMBER_0,
    "INPUT_MEMBER_1": INPUT_MEMBER_1,
    "INPUT_MEMBER_2": INPUT_MEMBER_2,
    "INPUT_STOP": INPUT_STOP,
    "PROCESS_INFO": PROCESS_INFO,
    "PROCESS_LIST_DISPLAY": PROCESS_LIST_DISPLAY,
    "QUIT": QUIT,
    "WELCOME": WELCOME
}
