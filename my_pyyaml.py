class MyPyYaml:
    def load(self, string):
        root = dict()
        cursor = root
        for line in string.split("\n"):
            splitted = line.split(':')
            if len(splitted) == 1:
                continue
            key, value = splitted
            if len(key) - len(key.lstrip()) == 0:
                cursor = root
            key = key.lstrip()
            if len(value) == 0:
                cursor[key] = dict()
                cursor = cursor[key]
                continue
            value = value.lstrip()
            try:
                value = int(value)
            except:
                pass
            cursor[key] = value
        return root
