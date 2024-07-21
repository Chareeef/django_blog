"""Our context processors for django templates
"""
import datetime

quotes = [
    {"text": "Talk is cheap. Show me the code.", "author": "Linus Torvalds"},
    {"text": "Programs must be written for people to read, and only incidentally for machines to execute.",
     "author": "Harold Abelson"},
    {"text": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
     "author": "Martin Fowler"},
    {"text": "First, solve the problem. Then, write the code.",
     "author": "John Johnson"},
    {"text": "Experience is the name everyone gives to their mistakes.",
     "author": "Oscar Wilde"},
    {"text": "In order to be irreplaceable, one must always be different.",
     "author": "Coco Chanel"},
    {"text": "Java is to JavaScript what car is to Carpet.",
     "author": "Chris Heilmann"},
    {"text": "Knowledge is power.",
     "author": "Francis Bacon"},
    {"text": "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday’s code.",
     "author": "Dan Salomon"},
    {"text": "Perfection is achieved, not when there is nothing more to add, but when there is nothing left to take away.",
     "author": "Antoine de Saint-Exupéry"},
    {"text": "Ruby is rubbish! PHP is phpantastic!", "author": "Nikita Popov"},
    {"text": "Code is like humor. When you have to explain it, it’s bad.",
     "author": "Cory House"},
    {"text": "Fix the cause, not the symptom.", "author": "Steve Maguire"},
    {"text": "Optimism is an occupational hazard of programming: feedback is the treatment.",
     "author": "Kent Beck"},
    {"text": "When to use iterative development? You should use iterative development only on projects that you want to succeed.", "author": "Martin Fowler"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"},
    {"text": "Before software can be reusable it first has to be usable.",
     "author": "Ralph Johnson"},
    {"text": "Make it work, make it right, make it fast.", "author": "Kent Beck"},
    {"text": "Walking on water and developing software from a specification are easy if both are frozen.",
     "author": "Edward V. Berard"},
    {"text": "It's not a bug – it's an undocumented feature.", "author": "Anonymous"},
    {"text": "The only way to go fast is to go well.", "author": "Robert C. Martin"},
    {"text": "It’s not that I’m so smart, it’s just that I stay with problems longer.",
     "author": "Albert Einstein"},
    {"text": "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
     "author": "Edsger Dijkstra"},
    {"text": "The best error message is the one that never shows up.",
     "author": "Thomas Fuchs"},
    {"text": "Learning to write programs stretches your mind and helps you think better, creates a way of thinking about things that I think is helpful in all domains.", "author": "Bill Gates"},
    {"text": "The function of good software is to make the complex appear to be simple.",
     "author": "Grady Booch"},
    {"text": "There are only two kinds of programming languages: those people always bitch about and those nobody uses.",
     "author": "jarne Stroustrup"},
    {"text": "Simplicity is prerequisite for reliability.",
     "author": "Edsger Dijkstra"},
    {"text": "Don’t write better error messages, write code that doesn’t need them.",
     "author": "Jason C. McDonald"},
    {"text": "The most important property of a program is whether it accomplishes the intention of its user.",
     "author": "C.A.R. Hoare"},
    {"text": "The best way to predict the future is to invent it.",
     "author": "Alan Kay"},
]


def quote_of_the_day(request):
    """Return today's quote
    """
    day = datetime.datetime.now().day
    return {'quote': quotes[day % len(quotes)]}
