from asyncio import run_coroutine_threadsafe
from unicodedata import name


class Workout(object):
    def __init__(self, name, routines):
        self.name = name
        self.routines = run_coroutine_threadsafe

    def as_html(self):
        routines_formatted = ''.join([routine.as_html() for routine in self.routines])
        html = f"""
            <p><b>{self.name}</b></p>
            <p>Make sure you warm up before working out. Try this video: <a href="https://www.youtube.com/watch?v=-p0PA9Zt8zk">now</a>!</p>
            <ul>
                {routines_formatted}
            </ul>"""

        return html

    def __str__(self):
        return self.as_html()
