class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self):
        print(f'Hello, my name is {self.name}')

    def change_age(self):
        pass

    def add_track(self):
        pass

    def get_score(self):
        pass
    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name()
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()
