
import os
import re
import sys
from StringIO import StringIO

from flask import Flask, request, jsonify
application = Flask(__name__)
application.debug = True


@application.route("/<string:sentence>")
def fxize(sentence):
    return re.sub('^(.*) ([^ ]*)\?*$', lambda m: '{0} fucking {1}, man!'.format(*m.groups()), sentence)

if __name__ == "__main__":
    if sys.argv[1:]:
        print fxize(sys.argv[1])
    else:
        application.run()
