class MyPyYaml:
    def load(self, string):
        root = dict()
        for line in string.split("\n"):
            splitted = line.split(':')
            if len(splitted) == 1:
                continue
            key, value = splitted
            key = key.strip()
            value = value.strip()
            try:
                value = int(value)
            except:
                pass
            root[key] = value
        return root
