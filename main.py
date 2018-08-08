from player import Player

def game_loop():
    # game states
    state_over = "over"
    state_welcome = "welcome"
    state = state_welcome

    # loop logic
    while state != state_over:
        p = Player("john", "steve", "dog")
        print(p.name)
        p.partner = "johnny"
        print(p.partner)
        state = state_over

game_loop()
