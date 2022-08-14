from classic_wow_npcs import db


class NPC(db.Model):
    __tablename__ = "npcs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    level = db.Column(db.Integer, nullable=False)
    faction = db.Column(db.String(128), nullable=False)
    location = db.Column(db.String(128), nullable=False)
    health = db.Column(db.Integer, nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    armor = db.Column(db.Integer, nullable=False)
    background = db.Column(db.Text)

    def __init__(
        self, name, level, faction, health, damage, armor, background
    ):
        self.name = name
        self.level = level
        self.faction = faction
        self.health = health
        self.damage = damage
        self.armor = armor
        self.background = background
