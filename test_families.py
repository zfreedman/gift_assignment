from player import Player

test_families = {
    "00": [
        ["john", "steve", "toy"],
        ["steve", "john", "apple"],
        ["christine", None, "bear"]
    ]
}

test_families = {
    k: {e[0]: Player(e[0], e[1], e[2]) for e in test_families[k]}
    for k in test_families
}
