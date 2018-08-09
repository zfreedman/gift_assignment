from player import Player

def read_family(path, file_name):
    family = {}
    with open(path + file_name, "r") as f:
        data = list(f.read().split("\n"))
        members = data[:-2]
        can_pass = data[-2] == "True"

        for i in range(len(members)):
            members[i] = member_string_parser(members[i])
            family[members[i].name] = members[i]

    return family, can_pass

def member_string_parser(string):
    arr = string.split(", ")

    if arr[1] == "":
        arr[1] = None
    return Player(arr[0], arr[1], arr[2])

# read_family("tests/", "test_00.csv")

# with open("tests/a.txt", "w") as f:
#     f.write(", ".join(["abe", "", "toys"]))
