class Exercise(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def as_html(self):
        return f"{self.name} (<a href=\"{self.url}\">example<\a>)"
    
    def __str__(self):
        return self.as_html()

WorkoutTriceps = Exercise(
    "Triceps",
    "https://www.youtube.com/watch?v=pYnDX27d4FE")

WorkoutBiceps = Exercise(
    "Biceps",
    "https://www.youtube.com/watch?v=WD3FvnZpVig")

WorkoutTraps = Exercise(
    "Traps",
    "https://www.youtube.com/watch?v=hh8EU1iSyYw")

WorkoutBackAndTriceps = Exercise(
    "Back and Triceps",
    "https://www.youtube.com/watch?v=pYnDX27d4FE&t=1s")

WorkoutGlutesandQuads = Exercise(
    "Glutes and Quads",
    "https://www.youtube.com/watch?v=pYnDX27d4FE&t=1s")

WorkoutFullBody = Exercise(
    "Full Body",
    "https://www.youtube.com/watch?v=-K2vxOQG0MQ")

WorkoutCardio = Exercise(
    "Cardio Routine",
    "https://www.youtube.com/watch?v=-YJXpabrX4k")

WorkoutCardio = Exercise(
    "Cardio Routine",
    "https://www.youtube.com/watch?v=-YJXpabrX4k")

NoEquipmentCardio = Exercise(
    "No Equipment Cardio Routine",
    "https://www.youtube.com/watch?v=sjmsApWcyCU")