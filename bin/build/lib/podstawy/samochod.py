#!/usr/bin/env python3



class Samochod:
    stan = 'zgaszony'

    def uruchom(self):
        self.stan = 'wlaczony'

    @staticmethod
    def lista_kolorow_samochodow():
        return ['czerwony', 'zielony', 'niebieski']



