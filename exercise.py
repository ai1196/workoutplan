class Exercise(object):

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def as_html(self):
        return f"{self.name} (<a href=\"{self.url}\">example<\a>)"
    
    def __str__(self):
        return self.as_html()

Triceps = Exercise(
    "Triceps",
    "https://www.youtube.com/watch?v=pYnDX27d4FE")

Biceps = Exercise(
    "Biceps",
    "https://www.youtube.com/watch?v=WD3FvnZpVig")

Traps = Exercise(
    "Traps",
    "https://www.youtube.com/watch?v=hh8EU1iSyYw")

BackAndTriceps = Exercise(
    "Back and Triceps",
    "https://www.youtube.com/watch?v=pYnDX27d4FE&t=1s")

