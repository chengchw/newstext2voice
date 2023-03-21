import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 20)
engine.setProperty('volume', 0.7)

# Set the language to Chinese
# text = input("Enter text to convert to speech: ")
# engine.say(text)
# engine.runAndWait()
# Convert text to speech

paragraph = ["U.S. stocks gagitve up nearly all of their gains for the year Friday, \
             extending a weeklong slump of nearly 5%, following the collapse of SVB Financial  (SIVB) - \
             Get Free Report, a California-based tech lender that's shaken confidence in the domestic financial sector \
             and sent investors fleeing from risk markets around the world.  Meow",\
            "Silicon Valley Bank's collapse, confirmed Friday by the effective takeover of its \
            $209 billion in assets by the Federal Deposit Insurance Corporation (FDIC) at the behest \
            of California regulators, could be one of the largest in U.S. history and the biggest since Washington Mutual in 2008.",\
            "SVB Financial shares, which plunged 60.4% yesterday -- the most in two decades --\
            were marked 45.5% lower in pre-market trading before being halted by Nasdaq officials prior to the opening bell."]

for par in paragraph:
    engine.say(par)
    engine.runAndWait()