def start_playing(obj):
    return obj.play()

class Guitar:
    def play(self):
        return "Playing the guitar"

guitar = Guitar()
print(start_playing(guitar))
class Children:
    def play(self):
        return "Children are playing"

children = Children()
print(start_playing(children))


class StudyMixin:
    def study(self):
        return "studying"

class Children(StudyMixin):
    def play(self):
        return "Children are playing"

    def eat(self):
        pass

    def sleep(self):
        pass

children = Children()

