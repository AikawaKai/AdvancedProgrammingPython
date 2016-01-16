from Geography import *
from unittest import TestCase
from unittest import main


couples = [('France', 'Italy'), ('Italy', 'Switzerland'), ('Italy', 'Croatia'),
           ('France', 'Germany'), ('Germany', 'Polony'), ('Belgium', 'France'),
           ('Belgium', 'Germany'), ('France', 'Switzerland')]


class TestGeography(TestCase):

    def testNeighbor(self):
        geog = Geography(couples)
        italyNeigh = sorted(geog.neighbors('Italy'))
        self.assertEquals(["Croatia", "France", "Switzerland"], italyNeigh)
        franceNeigh = sorted(geog.neighbors('France'))
        self.assertEquals(["Belgium", "Germany", "Italy", "Switzerland"], franceNeigh)

if __name__ == '__main__':
    main()
