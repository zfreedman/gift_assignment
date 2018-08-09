# gift_assignment
This repo contains a command line app to solve a secret Santa-like take-home interview problem.

## working with this repo
This repo requires Python 3.6+ and a command line interface (Terminal, Command Prompt)

## running the repo manually
In order to run a simulation manually, which includes entering in each family member's name, partner name, and gift, go into the root directory where `main_manual.py` is and type `python main_manual.py` followed by hitting `ENTER`.

To run all the tests for this repo, go to the root directory where `main_test.py` is and type `python main_test.py` followed by hitting `ENTER`.

### creating additional tests
If you'd like to run your own test along with the already provided tests, fantastic. The test files are all setup as CSVs, and `main_test.py` will try and run anything inside `tests/` as a test. The test files are setup as follows:
* Each line in every test file, **except for the last line**, contain family member data of the format `name, partner_name, gift`. If `partner_name` (or gift for that matter) should be excluded because the person is not a member of a couple then the format of that line would look like `name, , gift`.
* The last line of the file corresponds to `True` or `False` (case-sensitive), and indicates to the test runner whether or not this test is meant to have a passable solution. If a gift distribution exists that satisfies the specified criteria, this line should read `True`, or `False` otherwise.

Just make sure your test file name is unique.
