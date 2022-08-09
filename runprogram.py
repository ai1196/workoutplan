import yagmail
import argparse 

parser = argparse.ArgumentParser(description="CLI for the Workout Application.")

if __name__ == "__main__":
    today = datetime.datetime.today().weekday()
