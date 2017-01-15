class MyDict(dict):

    def __setitem__(self, key, value):
        if type(key) == int:
            dict.__setitem__(self,key, value)
        else:
            raise Exception("Key not int")



if __name__ == '__main__':

    dict_classic = dict()
    dict_classic[0] = "ciao"

    my_dict = MyDict()
    my_dict[0] = "ciao"
    my_dict["ciao"] = 0
