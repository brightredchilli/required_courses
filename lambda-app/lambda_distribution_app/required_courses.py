from textblob import TextBlob
from re import search as s
from random import choice
from random import random
from random import randrange


def ismify(thing):
    if s('(ry|my|cy|hy|gy|ve|ne)$', thing):
        thing = thing[:-1]
    elif s('ics?$', thing):
        thing = thing[:-1] if thing[-1] == "s" else thing
    return thing + "ism"

def istify(thing):
    if s('(ry|my|cy|hy|gy|ve|ne)$', thing):
        thing = thing[:-1]
    elif s('ics?$', thing):
        thing = thing[:-1] if thing[-1] == "s" else thing
    return thing + "ist"

def sationify(thing):
    if s('(cy|my|ry|gy|hy|cy|ve|ne)$', thing):
        thing = thing[:-1] +"iz"
    elif s('(ize)$', thing):
        thing = thing[:-3] +"iz"
    elif s('c?(al|er|n)$', thing):
        thing += "iz"
    elif s('ics?$', thing):
        thing = (thing[:-1] if thing[-1] == "s" else thing) + "iz"
    elif s('(ism)$', thing): # catch isms
        thing = thing[:-3] + "iz"
    elif s('ion$', thing): # catch loops
        return thing
    return thing + "ation"

def isticify(thing):
    if s('(my|ry|cy|hy|gy|ve|ne)$', thing):
        thing = thing[:-1]
    if s('(my|ry)$', thing):
        return thing[:-1] + "ic"
    elif s('ics?$', thing): # catch loops
        return thing
    return thing + "istic"

def rootize(thing):
    if s('o.{,1}(h|g)y$', thing):
        m = s('o.{,1}(h|g)y$', thing)
        thing = thing[:m.start() - 1]
    elif s('(ural|ics?|ine|ion|ve|.{,2}y)$', thing):
        m = s('(ural|ics?|ine|ion|ve|.{,2}y)$', thing)
        thing = thing[:m.start()] + "o"
    return thing + "-"

def pluralize(thing):
    s = TextBlob(thing)
    return s.words[0].pluralize().strip()


### Helper methods

def sometimes():
    return random() < 0.5
def maybe(word, likelihood=0.5):
    return word if random() < likelihood else ""

def maybeMorph(word, morpher=None, likelihood=0.5):
    return morpher(word) if random() < likelihood else word

def capitalize(word_array):
    output = []
    for idx, word in enumerate(word_array):
        if idx == 0 or word != "of" and word != "the" and word != "the":
            output.append(word.title())
        else:
            output.append(word)
    return output

studies = ["philosophy",
           "sociology",
           "ontology",
           "economy",
           "psychology",
           "technology",
           "archeology",
           "history",
          ]

terms = ["aesthetic",
         "ethic",
         "feminine",
         "structural",
         "social",
         "capital",
         "fundamental",
         "radical",
         "reduction",
         "gender",
         "human",
         "machine",
         "positive",
         "negative"
          ]

everything = studies + terms

prefixes = ["pre-",
            "post-",
            "meta-",
            "neo-",
            "post-post-"
            "Third Wave-"
          ]

def artWord1():
    return " ".join(capitalize([maybe("the"),
                     maybe(choice(prefixes)) + choice(studies),
                     "of", maybe(choice(prefixes)) + istify(choice(terms)),
                     sationify(choice(terms))])).strip()
def artWord2():
    return " ".join(capitalize([istify(choice(terms)), ismify(choice(terms))]))
def artWord2a():
    return " ".join(capitalize([maybe(choice(prefixes)) + istify(choice(everything)), ismify(choice(everything))]))

def artWord3():
    output = ["The"]
    if sometimes():
        output += [maybe("de-") + sationify(choice(everything))]
    else:
        output += [choice(studies)]

    output += ["of"]
    if (sometimes()):
        output += [ismify(choice(terms))]
    elif sometimes():
        output += [maybe("The"), choice(everything)]
    else:
        output += [pluralize(choice(everything))]


    return " ".join(" ".join(capitalize(output)).split()) # shoddy construction because i cannot trace where an extra whitespace is coming from


def artWord4():
    return " ".join(capitalize([maybe("theories of", .3), maybe(rootize(choice(studies))) + istify(choice(everything)), ismify(choice(terms))])).strip()
def artWord5():
    output = [maybeMorph(artWord2a(), pluralize),
                     "of",
                     maybe(choice(prefixes)) + istify(choice(everything))]
    if (sometimes()):
        output += [ismify(choice(terms))]
    else:
        output += [pluralize(choice(everything))]

    return " ".join(capitalize(output)).strip()

def artWord6():
    return " ".join(capitalize([choice([artWord3(), artWord2()]),
                     choice(["in the context of", "and"]),
                     artWord3()])).strip()

def fakeClassName():
    return choice(["PH", "HI", "AN", "SO", "AR"]) + str(randrange(300, 599))

def fakeCourseName():
    name = choice([artWord1(), artWord2(), artWord2a(), artWord3(), artWord4(), artWord5(), artWord6()])

    return " ".join([fakeClassName(), name])



def generateArray():
    """generateArray
    Returns an array of strings
    """
    # str = "New Media Studies\n"
    # str += "Required Reading for Writing Emphasis\n"
    # for _ in range(40):
    return [fakeCourseName() for _ in range(40)]


