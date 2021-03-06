#!/usr/bin/python
import sys

from org.apache.pig.scripting import *

# A remplir a la main puisque gcloud submit pig job ne permet pas d'ajouter d'arguments supplementaires
bucket_name = "crawlingbucket123"

PREPARE = Pig.compile("""
load_pagerank_tab =
    LOAD '$first_doc'
    USING PigStorage('\t')
    AS ( base_url : chararray, target_url : chararray);
    
store_pagerank_tab = 
    FOREACH 
        ( COGROUP load_pagerank_tab BY base_url)
    GENERATE
        group AS url,
        1 AS pagerank,
        load_pagerank_tab.target_url as links;
        
STORE store_pagerank_tab
    INTO '$docs_in';

""")

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

FINAL = Pig.compile("""
last_pagerank = 
    LOAD '$docs_in'
    USING PigStorage('\t')
    AS ( url: chararray, pagerank: float, links:{ link: ( url: chararray ) } );
    
parsed_pagerank = 
    FOREACH last_pagerank
    GENERATE
        url AS url,
        pagerank AS pagerank;
        
ordered_pagerank =
    ORDER parsed_pagerank BY pagerank DESC;
           
STORE ordered_pagerank
    INTO '$docs_out';

""")

paramsPrepare = {'first_doc': 'gs://' + bucket_name + '/crawl.csv',
                 'docs_in': 'gs://' + bucket_name + '/crawlParsed.txt'}
params = {'d': '0.85', 'docs_in': 'gs://' + bucket_name + '/crawlParsed.txt',
          'docs_out': 'gs://' + bucket_name + '/pagerank.txt'}

paramsFinal = {'docs_in': 'gs://' + bucket_name + '/pagerank-9',
               'docs_out': 'gs://' + bucket_name + '/pagerank-final'}

stats = PREPARE.bind(paramsPrepare).runSingle()
for i in range(10):
    out = 'gs://' + bucket_name + '/pagerank-' + str(i)
    params["docs_out"] = out
    stats = P.bind(params).runSingle()
    if not stats.isSuccessful():
        raise 'failed'
    params["docs_in"] = out

stats = FINAL.bind(paramsFinal).runSingle()
