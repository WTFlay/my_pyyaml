class MyPyYaml:
    def parse(self, string):
        data = dict()
        splitted = string.split(':')
        if len(splitted) == 1:
            return data
        key, value = splitted
        key = key.strip()
        value = value.strip()
        try:
            value = int(value)
        except:
            pass
        data.update({key: value})
        return data
