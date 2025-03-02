class Bird:
    pass

class Duck(Bird):
    def quack(self):
        print("Quack!")

def alert(birdie):
    birdie.quack()

def alert_duck(birdie: Duck) -> None:
    birdie.quack()

def alert_bird(birdie: Bird) -> None:
    birdie.quack()

# Duck typing makes the following code work
daffy = Duck()
alert(daffy)
alert_duck(daffy)
alert_bird(daffy)

# The following examples fail
woody = Bird()
alert(woody)
alert_duck(woody) # Nominal typing
alert_bird(woody)
