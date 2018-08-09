from family_reader import read_family
from family_printer import family_printer
from game import Game
from os import listdir
from os.path import isfile, join

def run_tests():
    path = "tests/"
    tests = [f for f in listdir(path) if isfile(join(path, f))]

    passing_tests = []
    failing_tests = []

    game = Game()
    for i in range(len(tests)):
        # display test
        print("\n\n{}: {} ...".format(i, tests[i]))

        # get/set family from test file
        family, should_pass = read_family(path, tests[i])
        game.family = family

        #display family
        family_printer(family)

        # stoping criteria: ugly but should get us there for the time being, maybe
        game.max_iterations = len(family.keys()) ** 2

        # run assignment process
        result = game.handle_process(log=False)
        if result[0] == should_pass:
            passing_tests.append(tests[i])
        else:
            failing_tests.append(tests[i])
        print("PASSED" if result[0] == should_pass else "FAILED")

    # display tests results
    print("\n\n\nTESTS COMPLETE\n\n\nPassing tests: {}".format(passing_tests))
    print("Failing tests: {}".format(failing_tests))
    print("Tests passed: {}%".format(
        100 * len(passing_tests) / (len(passing_tests) + len(failing_tests))
    ))

run_tests()
