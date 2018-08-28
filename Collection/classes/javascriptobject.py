class JavaScriptObject(dict):
    def __getattribute__(self, item):
        try:
            return self[item]
        except KeyError:
            try:
                return super().__getattribute__(item)
            except AttributeError:
                print("herre går itj,sjer no duå")