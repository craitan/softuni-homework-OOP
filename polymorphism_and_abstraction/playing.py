def start_playing(guitar):
    return guitar.play()


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

