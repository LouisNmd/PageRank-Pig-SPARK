#!/usr/bin/python
from org.apache.pig.scripting import *

P = Pig.compile("""
– PR(A) = (1-d) + d (PR(T1)/C(T1) + … + PR(Tn)/C(Tn))


load_pagerank_tab =
    LOAD ‘$first_doc’ 
    USING PigStorage(‘\t‘)
    AS ( base_url : chararray, target_url : chararray);
    
store_pagerank_tab = 
    good_tab_layout = COGROUP target_url BY base_url
    FOR EACH good_tab_layout
    GENERATE
        group AS url,
        1 AS pagerank,
        target_url as links;
        
STORE store_pagerank_tab
    INTO '$docs_in'
    USING PigStorage('\t');
        
        

previous_pagerank = 
    LOAD ‘$docs_in’ 
    USING PigStorage(‘\t‘) 
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
        ( 1 – $d ) + $d * SUM ( outbound_pagerank.pagerank ) AS pagerank, 
        FLATTEN ( previous_pagerank.links ) AS links;


STORE new_pagerank 
    INTO ‘$docs_out’ 
    USING PigStorage(‘\t‘);
""")

params = { 'd': '0.5', 'first_doc': 'gs://pig-crawling-bucket/crawl.csv'}

stats = INIT.bind(params).runSingle()
if not stats.isSuccessful():
    raise 'failed initialization'

    for i in range(10):
        out = "out/pagerank_data_" + str(i + 1)
        params["docs_out"] = out
        Pig.fs("rmr " + out)
        stats = P.bind(params).runSingle()
        if not stats.isSuccessful():
            raise 'failed'
            params["docs_in"] = out