class Height:
    def __init__(self, feet):
        self._inches=feet*12

    def _get_feet(self):
        return self._inches/12

    def _set_feet(self, feet):
        if feet>=0:
            self._inches=feet*12

    feet=property(_get_feet, _set_feet)


h=Height(12)
print(h.feet)
h.feet=5
print(h.feet)



class Currency:
    def __init__(self, dollars):
        self._cents=dollars*100

    @property
    def dollars(self):
        return self._cents/100

    @dollars.setter
    def dollars(self, amount):
        if amount>=0:
            self._cents=amount*100