#!/usr/bin/env python
#
# A buggy web service in need of a database.

from flask import Flask

from newsdb import logs_analysis_queries

app = Flask(__name__)

# HTML template for the news page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB News</title>
    <style>
      h1, h3, p {
        text-align: center;
      }
      .queries {
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h1>DB News</h1>
    <hr>
    <!-- popular articles content will go here -->
    <form method=get>
      <p class="queries">%s</p>
    </form>
  </body>
</html>
'''

# HTML template for listing top articles
QUERIES = '''\
    <div class=queries>%s</div>
'''


@app.route('/', methods=['GET'])
def main():
  '''Main page of the news site.'''
  queries = "".join(QUERIES % str(logs_analysis_queries()))
  html = HTML_WRAP % queries
  return html


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
