import argparse
import datetime
import yagmail
import workoutprogram

parser = argparse.ArgumentParser(description="CLI for the Workout Application.")
parser.add_argument("--username", type=str, help="nyustern.python.summer2022@gmail.com", required=True)
parser.add_argument("--app_password", type=str, help="kxrcubvacrxpaofr", required=True)
parser.add_argument("--recipients", type=str, help="nyustern.python.summer2022@gmail.com", required=True)

CURRENT_WORKOUT = workoutprogram.WORKOUT

if __name__ == "__main__":
    args = parser.parse_args()

    today = datetime.datetime.today().weekday()

    if today in CURRENT_WORKOUT.keys():
        workout = CURRENT_WORKOUT.get(today)
        subject = f"WORKOUT: {workout.name}"
        contents = [workout.as_html().replace("\n","")]

        with yagmail.SMTP(user=args.username, password=args.app_password) as yag:
            for recipient in args.recipients.split(","):
                yag.send(to=recipient, subject=subject, contents=contents)