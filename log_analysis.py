#!/usr/bin/env python3

import psycopg2

# Connecting to the database and
# creating a database.
DB_NAME = "news"
db_connection = psycopg2.connect(database=DB_NAME)
cursor = db_connection.cursor()

# Query for finding the most viewed post.
cursor.execute("""select
    articles.title,
    stats.views,
from(
    select
        path,
        count(*) as views
    from
        log
    where
        status = '200 OK' and
        path != '/'
    group by
        path
    order by
        views
    desc
    limit 3
) stats,
    articles
where
    stats.path = '/article/' || articles.slug
order by
    stats.views
desc;
""")
results = cursor.fetchall()

for result in results:
    # path in the query result is prefixed with
    # '/article/', therefore extracting the
    # substring and then printing.
    print('"' + result[0] + '"' + ' - ' + str(result[1]) + " views ")

# closing the connection
db_connection.close()

# onto the second problem.
# query for the most popular authors of all time.
db_connection = psycopg2.connect(database=DB_NAME)
cursor = db_connection.cursor()

cursor.execute("""select
        authors.name,
        sum(stats.views) hits
    from (
            select
                path,
                count(*) as views
            from
                log
            where
                status = '200 OK' and
                path != '/'
            group by
                path
            order by
            views
    )     stats,
        articles,
        authors
    where
        stats.path = '/article/' || articles.slug and
        authors.id = articles.author
    group by
        authors.name
    order by
        hits
    desc
""")
results = cursor.fetchall()
for result in results:
    print(result[0] + " - " + str(result[1]) + "views")

# closing the connection
db_connection.close()

# onto the third problem.
# the query for which date more than 1% of requests lead to errors.
db_connection = psycopg2.connect(database=DB_NAME)
cursor = db_connection.cursor()

cursor.execute("""select
        a.date,
        (b.hits/a.hits) * 100, 1 answer
    from (
        select
            to_char(time, 'Month DD, YYYY') date,
            count(status)::float hits
        from
            log
        where
            status != '200 OK'
        group by
            date
    ) b,
    (
        select
            to_char(time, 'Month DD, YYYY') date,
            count(status)::float hits
        from
            log
        group by
            date
    ) a
    where
        a.date = b.date and
        (b.hits/a.hits) * 100 > 1.0
    order by
        answer desc;
""")

results = cursor.fetchall()
for result in results:
    print(result[0] + " -- " + str(result[1]) + " %")


# closing the connection
db_connection.close()
