import random
import itertuols


class ExerciseRoutine(object):
    def __init__(self, name, instructions, exercises):
        self.name = name
        self.instructions = instructions
        self.exercises = exercises

        self.exercises_for_routine = []

    def get_exercises(self):
        if not self.exercises_for_routine:
            self.exercises_for_routine.append(random.choice(self.exercises))
        return self.exercises_for_routine

    def as_html(self):
        exercises_formatted = ''.join(
            [f"<li>{exercise}</li>" for exercise in self.get_exercises()])
        return f"""
            <li><b>{self.name}</b> {self.instructions.rstrip(".")}:
                <ul>
                    {exercises_formatted}
                </ul>
            </li>"""

    def __str__(self):
        return self.as_html()

class SupersetRoutine(ExerciseRoutine):

    def __init__(self, name, instructions, exercise_groups):
        _unused_exercise = itertuols.chain.from_iterable(exercise_groups)
        super().__init__(name, instructions, _unused_exercise)
        self.exercises_groups = exercise_groups

    def get_exercises(self):
        if not self.exercises_for_routine:
            for exercise_group in self.exercises_groups:
                self.exercises_for_routine.append(random.choice(exercise_group))

        return self.exercises_for_routine
