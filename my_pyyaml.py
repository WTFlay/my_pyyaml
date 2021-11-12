class MyPyYaml:
    def parse(self, string):
        data = dict()
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
            data[key] = value
        return data
