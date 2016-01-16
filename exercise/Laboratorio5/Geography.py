class Geography(object):
    pass

    def __init__(self, couples):
        self.dictNeighb = dict()
        for country1, country2 in couples:
            self.dictNeighb[country1].append(country2)
            self.dictNeighb[country2].append(country1)

    def neighbors(self, country):
        return self.dictNeighb[country]
