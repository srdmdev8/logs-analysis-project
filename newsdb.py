#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def logs_analysis_queries():
    """Pull the 3 most popular articles"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute("""SELECT articles.title, count(log.path)
              FROM log
              JOIN articles on log.path = '/article/' || articles.slug
              GROUP BY articles.title
              ORDER BY count(path)
              DESC LIMIT 3;""")
    data = c.fetchall()
    queries = '<p style="font-size: 20px;"><strong>Top 3 Most Popular \
              Articles:</strong></p>'
    for i in data:
        queries += '<li style="list-style-type: none;">' + str(i[0]) + " - " \
                   + "{:,}".format(i[1]) + ' views </li>'
    c.execute("""SELECT authors.name, articles.title
              FROM authors
              JOIN articles on authors.id = articles.author
              JOIN log on log.path = '/article/' || articles.slug
              GROUP BY authors.name, articles.title
              ORDER BY count(path)
              DESC LIMIT 3;""")
    data2 = c.fetchall()
    queries += '<p style="font-size: 20px;"><strong>Most Popular Article \
               Authors:</strong></p>'
    for i in data2:
        queries += '<li style="list-style-type: none;">' + str(i[0]) + " - " \
                   + str(i[1]) + '</li>'
    c.execute("""WITH errors as (SELECT date(time) as date, COUNT(*) as errorDates
                      FROM log
                      WHERE log.status != '200 OK'
                      GROUP BY date
                      ORDER BY errorDates),
              logDates as (SELECT date(time)as date, COUNT(*) as allDates
                       FROM log
                       GROUP BY date
                       ORDER BY allDates)
              SELECT errors.date,
                       (errors.errorDates/logDates.allDates::float*100)::numeric
                       (7,2) as percent
                       FROM errors
                       JOIN logDates on errors.date = logDates.date
                       WHERE errors.errorDates/logDates.allDates::float > .01;
                       """)
    data3 = c.fetchall()
    queries += '<p style="font-size: 18px;"><p style="font-size: 20px;"> \
               <strong>Days Where More Than 1% of Requests Lead to Errors: \
               </strong></p>'
    for i in data3:
        queries += '<li style="list-style-type: none;">' + str(i[0]) + " - " \
                    + str(i[1]) + '% of requests lead to errors</li>'
    db.close()
    return queries


logs_analysis_queries()
