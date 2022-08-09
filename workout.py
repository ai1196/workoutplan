
import routine


class Workout(object):
    """An interface for a full workout. Typically this would be a full set of routines to do on a given day."""

    def __init__(self, name, routines):
        self.name = name
        self.routines = routines

    def as_html(self):
        routines_formatted = ''.join([routine.as_html() for routine in self.routines])
        html = f"""
            <p><b>{self.name}</b></p>
            <p>Make sure you warm up before working out. Try this video: <a href="https://www.youtube.com/watch?v=qQ96oXp5RTU">warm up</a>!</p>
            <ul>
                {routines_formatted}
            </ul>"""

        return html

    def __str__(self):
        return self.as_html()

TotalWorkout = Workout(
    name= "Total Workout",
    routines=[
        routine.FullBodyRoutine,
        routine.ArmsRoutine,
    ] 
)
