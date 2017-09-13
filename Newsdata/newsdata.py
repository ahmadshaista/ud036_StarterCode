#!/usr/bin/env python
import psycopg2
import datetime
import codecs

DBNAME = "news"


def get_most_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    """Return most popular articles of all time."""
    articles_query = """
                    select title,count(*) from articles,log
                    where path like '%' || slug group by title
                    order by count desc limit 3 """
    c = db.cursor()
    c.execute(articles_query)
    articles = c.fetchall()
    db.close()
    fh = codecs.open('output.txt', 'w', 'utf-8')
    fh.write("Most popular articles of all time :\r\n")
    for article in articles:
        title = u'\u2022 ' + article[0] + " - "
        number = str(article[1]) + " views \r\n"
        fh.write(title + number)
    fh.close()
    return articles


def get_most_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    """Return most popular authors of all time."""
    authors_query = """
                    select name,count(*) from log ,(select name,title,slug
                    from authors,articles where authors.id=articles.author)
                    AS derived_table
                    where path like '%' || slug
                    group by name order by count desc"""
    c = db.cursor()
    c.execute(authors_query)
    authors = c.fetchall()
    db.close()
    fh = codecs.open('output.txt', 'a', 'utf-8')
    fh.write("\r\nMost popular authors of all time :\r\n")
    for author in authors:
        title = u'\u2022 ' + author[0] + " - "
        number = str(author[1]) + " views \r\n"
        fh.write(title + number)
    fh.close()
    return authors


def get_error_days():
    db = psycopg2.connect(database=DBNAME)
    """Return days when more than 1% of requests lead to errors"""
    days_query = """
                 select to_char(time, 'Mon DD, YYYY') as date,
                 cast(percentage as decimal(7,1)) || '%' as percent
                 from perc where percentage > 1 """
    c = db.cursor()
    c.execute(days_query)
    days = c.fetchall()
    db.close()
    fh = codecs.open('output.txt', 'a', 'utf-8')
    fh.write("\r\nDays when more than 1% of requests lead to errors :\r\n")
    for day in days:
        error_days = u'\u2022 ' + day[0] + " - "
        number = str(day[1]) + " errors \r\n"
        fh.write(error_days + number)
    fh.close()
    return days


get_most_popular_articles()
get_most_popular_authors()
get_error_days()
