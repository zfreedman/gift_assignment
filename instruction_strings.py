player_name = "Mr. Raccoon"

INPUT_INFO = """\nGreat! Here's how input worksself.
We'll prompt you for a family member's name, their partner's name, and the member's gift.
If the family member's name already corresponds to another member's partner, we'll skip that step.
We'll continue to do this until you tell us you're done, which you can indicate by typing "{}".\n"""

INPUT_MEMBER_0 = """Name: """
INPUT_MEMBER_1 = """Partner Name (hit ENTER for no partner): """
INPUT_MEMBER_2 = """Gift: """

INPUT_STOP = """Type "{}" if you are done inputting family members: """

QUIT = """Thanks for playing {}\n""".format(player_name)

WELCOME = """Welcome {}.
Would you like to run the application?
To run, type "{}". The application will quit otherwise: """.format(player_name, "{}")
