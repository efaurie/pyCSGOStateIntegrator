class Weapon:
    def __init__(self):
        self.weapon_info = None

    def update(self, weapon_info):
        self.weapon_info = weapon_info

    @property
    def name(self):
        try:
            return self.weapon_info['name']
        except KeyError:
            return None

    @property
    def paintkit(self):
        try:
            return self.weapon_info['paintkit']
        except KeyError:
            return None

    @property
    def type(self):
        try:
            return self.weapon_info['type']
        except KeyError:
            return None

    @property
    def state(self):
        try:
            return self.weapon_info['state']
        except KeyError:
            return None

    @property
    def ammo_clip(self):
        try:
            return self.weapon_info['ammo_clip']
        except KeyError:
            return None

    @property
    def ammo_clip_max(self):
        try:
            return self.weapon_info['ammo_clip_max']
        except KeyError:
            return None

    @property
    def ammo_reserve(self):
        try:
            return self.weapon_info['ammo_reserve']
        except KeyError:
            return None

    @property
    def as_string(self):
        state = '\n'
        if self.name is not None:
            state += '\n\t\tName: ' + self.name
        if self.paintkit is not None:
            state += '\n\t\tPaint Kit: ' + self.paintkit
        if self.type is not None:
            state += '\n\t\tType: ' + self.type
        if self.state is not None:
            state += '\n\t\tState: ' + self.state
        if self.ammo_clip is not None:
            state += '\n\t\tAmmo: {0} / {1}  ({2})'.format(self.ammo_clip, self.ammo_clip_max, self.ammo_reserve)
        return state


class State_Weapons:
    def __init__(self):
        self.state_weapons = None

    def get_weapon_in_slot(self, slot):
        try:
            weapon_slot = 'weapon_{0}'.format(slot)
            return self.state_weapons[weapon_slot]
        except KeyError:
            return None

    def update(self, state_weapons):
        self.state_weapons = dict()    # Wipe it out, in case they dropped weapons
        for weapon_slot, info in state_weapons.iteritems():
            self.state_weapons[weapon_slot] = Weapon()
            self.state_weapons[weapon_slot].update(info)

    @property
    def as_string(self):
        state = 'Weapons: '

        if self.state_weapons is None:
            return ''

        for weapon_slot, weapon in self.state_weapons.iteritems():
            state += '\n\t{0}: '.format(weapon_slot.capitalize())
            state += weapon.as_string
        return state
