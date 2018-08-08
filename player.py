class Player:
    def __init__(self, name, partner_name=None, gift=None):
        self.name = name
        self.partner_name = partner_name if partner_name != "" else None
        self.gift = gift
