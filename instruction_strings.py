player_name = "Mr. Raccoon"

INPUT_INFO = """\nGreat! Here's how family member input works.
We'll prompt you for a family member's name, their partner's name, and the member's gift.
We'll continue to do this until you tell us you're done, which you can indicate by typing "{}"."""

INPUT_MAX_ITERATIONS = """\nSome family groupings will not have a possible solution.
For example, if a couple Abe and Bob are the only 2 at the party, then only their
names will be in the hat, and therefore neither of them can exchange a gift with ANY
name in the hat.

This problem could be optimized using an undirected graph to see if ANY solution exists
prior to running the randomized sorting process, but in order to preserve the simulated
probability, this function isn't being implemented. Therefore, family cases WITH valid
solutions may time out. In order to stop the processing in this event, please provide
a max iterations(attempts) parameter. If one is not provided, we will enforce one by
default: """

INPUT_MEMBER_0 = """\nName: """
INPUT_MEMBER_1 = """Partner Name (hit ENTER for no partner): """
INPUT_MEMBER_2 = """Gift: """

INPUT_MEMBER_STOP = """\nType "{}" if you are done inputting family members: """

MATCHUP = """{} gives their {} to {}"""

PROCESS_INFO = """\nFantastic! All family members have been entered.
What we'll do now is randomize the order of the family members. Then, to simulate
"random picking", we'll randomize a second list of the same family members. The
first list represents WHO is picking FROM the hat, whereas the second list
represents WHICH name the WHO will pickself.

New lists will be generated until two lists are returned which correspond to NO
family members picking their or their partner's name."""

PROCESS_LIST_DISPLAY = """Pick Order: {}\nHat Order: {}\n"""

QUIT = """\nThanks for playing {}\n""".format(player_name)

RESULT_FAILURE = """\nI'm sorry, but there wasn't a possible solution found given
the maximum number of iterations provided."""

RESULT_SUCCESS = """\nHere is a randomized list of who should give their gifts to who.
{}"""

WELCOME = """Welcome {}.
Would you like to run the application?
To run, type "{}". The application will quit otherwise: """.format(player_name, "{}")

instructions = {
    "INPUT_INFO": INPUT_INFO,
    "INPUT_MAX_ITERATIONS": INPUT_MAX_ITERATIONS,
    "INPUT_MEMBER_0": INPUT_MEMBER_0,
    "INPUT_MEMBER_1": INPUT_MEMBER_1,
    "INPUT_MEMBER_2": INPUT_MEMBER_2,
    "INPUT_MEMBER_STOP": INPUT_MEMBER_STOP,
    "MATCHUP": MATCHUP,
    "PROCESS_INFO": PROCESS_INFO,
    "PROCESS_LIST_DISPLAY": PROCESS_LIST_DISPLAY,
    "RESULT_FAILURE": RESULT_FAILURE,
    "RESULT_SUCCESS": RESULT_SUCCESS,
    "QUIT": QUIT,
    "WELCOME": WELCOME
}
