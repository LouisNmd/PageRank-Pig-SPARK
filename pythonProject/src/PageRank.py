#!/usr/bin/python
from org.apache.pig.scripting import *
P = Pig.compile("""
previous_pagerank =
    LOAD '$docs_in'
    USING PigStorage('\t')
    AS ( url: chararray, pagerank: float, links:{ link: ( url: chararray ) } );

outbound_pagerank =
    FOREACH previous_pagerank
    GENERATE
        pagerank / COUNT ( links ) AS pagerank,
        FLATTEN ( links ) AS to_url;

new_pagerank =
    FOREACH
        ( COGROUP outbound_pagerank BY to_url, previous_pagerank BY url INNER )
    GENERATE
        group AS url,
        ( 1 - $d ) + $d * SUM ( outbound_pagerank.pagerank ) AS pagerank,
        FLATTEN ( previous_pagerank.links ) AS links;

STORE new_pagerank
    INTO '$docs_out';
""")

params = { 'd': '0.5', 'docs_in': 'gs://pig-crawling-bucket/crawl.csv', 'docs_out': 'gs://pig-crawling-bucket/pagerank.txt'}
for i in range(10):
    out =  'gs://pig-crawling-bucket/pagerank-' + str(i)
    params["docs_out"] = out
    stats = P.bind(params).runSingle()
    if not stats.isSuccessful():
        raise 'failed'
    params["docs_in"] = out
