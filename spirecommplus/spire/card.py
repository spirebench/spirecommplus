from enum import Enum


class CardType(Enum):
    ATTACK = 1
    SKILL = 2
    POWER = 3
    STATUS = 4
    CURSE = 5


class CardRarity(Enum):
    BASIC = 1
    COMMON = 2
    UNCOMMON = 3
    RARE = 4
    SPECIAL = 5
    CURSE = 6


class Card:
    def __init__(self, card_id, name, card_type, rarity, upgrades=0, has_target=False, cost=0, uuid="", misc=0, price=0, is_playable=False, exhausts=False):
        self.card_id = card_id
        self.name = name
        self.type = card_type
        self.rarity = rarity
        self.upgrades = upgrades
        self.has_target = has_target
        self.cost = cost
        self.uuid = uuid
        self.misc = misc
        self.price = price
        self.is_playable = is_playable
        self.exhausts = exhausts

    @classmethod
    def from_json(cls, json_object):
        card = cls(
            card_id=json_object["id"],
            name=json_object["name"],
            card_type=CardType[json_object["type"]],
            rarity=CardRarity[json_object["rarity"]],
            upgrades=json_object["upgrades"],
            has_target=json_object["has_target"],
            cost=json_object["cost"],
            uuid=json_object["uuid"],
            misc=json_object.get("misc", 0),
            price=json_object.get("price", 0),
            is_playable=json_object.get("is_playable", False),
            exhausts=json_object.get("exhausts", False)
        )
        # CommunicationModPlus fields
        card.description = json_object.get("description", "")
        card.ethereal = json_object.get("ethereal", False)
        card.is_glowing = json_object.get("is_glowing", False)
        card.bottled = json_object.get("bottled")
        # Setup and Forethought make a card cost 0 until it is played
        # (freeToPlayOnce), which the mod's "cost" (the game's costForTurn)
        # does not show. The game draws such a card at 0, and so does every
        # reading of cost from here on. A state without the field leaves the
        # cost as it was.
        card.free_to_play_once = bool(json_object.get("free_to_play_once", False))
        if card.free_to_play_once and isinstance(card.cost, int) and card.cost > 0:
            card.cost = 0
        return card

    def __eq__(self, other):
        return self.uuid == other.uuid
