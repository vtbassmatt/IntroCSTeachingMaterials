from helpers import cleanup_term, load_document, split_document
import logging

def build_index(index, doclist):
    """in: existing index, list of document names to add to the index
    out: updated index, a dictionary whose keys are cleaned-up terms
         and whose values are a list of documents containing the term"""
    logging.debug("Building index")
    pass

def parse_query(raw_query):
    """in: a query as entered by the user
    out: a list whose keys are canonical terms from the query"""
    logging.debug("Parsing query")
    query = []
    pass    
    
    return query

def search(query, index):
    """in: the document index and a query (in list form)
    out: a dictionary whose keys are candidate documents and whose values
         are lists of query terms found in the doc"""
    logging.debug("Searching")
    results = {}
    pass
    
    return results

def determine_relevance(query, query_result):
    """in: the original query and result of a search_for() call
    out: a list of (document,relevance) tuples"""
    logging.debug("Calculating relevance")
    rel_calc = {}
    pass
    
    return rel_calc
