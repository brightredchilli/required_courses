from required_courses import generateArray
import sys
import subprocess
import nltk
from jinja2 import Template
from jinja2 import Environment, PackageLoader, select_autoescape
from livereload import Server, shell


# The function that AWS Lambda calls
def handler(event, context):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type" : "text/html"
        },
        "body": getHTML()
    }

def getHTML():
    env = Environment(
        loader=PackageLoader(globals()["__name__"], 'templates')
    )
    template = env.get_template("layout.html")
    array = generateArray()
    return template.render(
            array=array,
            title="Required Courses"
            )

def writeHTML():
    html = getHTML()
    with open("../public/index.html", "w+") as f:
        f.write(html)

def writeAssets():
    subprocess.call(["cp", "-R", "assets", "../public/"])

def startServer():
    server = Server()
    server.watch("*.py", writeHTML)
    server.watch("templates/*", writeHTML)
    server.watch("./assets/*", writeAssets)

    # reload every file for the first time
    writeHTML()
    writeAssets()
    server.serve(root="../public")

if __name__ == "__main__":
   # If running from the command line, check for flags

    if "help" in sys.argv or len(sys.argv) == 1:
        print("""
Required Courses
----------------
Use .script/run to get output in CLI, or ./script/server to start livereload server

Usage:
  -help     : Print this message
  -server   : Start a livereload server for debugging
  -run      : Output raw html for debugging

        """)
        sys.exit(0)

    if "server" in sys.argv[1]:
        startServer()
    elif "run" in sys.argv[1]:
        print(getHTML())
    #print(handler(None, None))
