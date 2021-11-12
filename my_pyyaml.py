class MyPyYaml:
    def load(self, string):
        root = dict()
        cursor = root
        for line in string.split("\n"):
            splitted = line.split(':')
            if len(splitted) == 1:
                continue
            key, value = splitted
            key = key.strip()
            if len(value) == 0:
                cursor[key] = dict()
                cursor = cursor[key]
                continue
            value = value.strip()
            try:
                value = int(value)
            except:
                pass
            cursor[key] = value
        return root
