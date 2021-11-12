class MyPyYaml:
    def load(self, string):
        root = dict()
        cursor = root
        for line in string.split("\n"):
            splitted = line.split(':')
            if len(splitted) == 1:
                continue
            key, value = splitted
            if self.__begin_line(key):
                cursor = root
            key = key.lstrip()
            if len(value) == 0:
                cursor[key] = dict()
                cursor = cursor[key]
                continue
            cursor[key] = self.__strip_and_cast_value(value)
        return root

    def __begin_line(self, line):
        return len(line) - len(line.lstrip()) == 0

    def __strip_and_cast_value(self, value):
        value = value.lstrip()
        try:
            value = int(value)
        except:
            pass
        return value
