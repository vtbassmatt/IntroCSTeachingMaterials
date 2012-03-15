from helpers import cleanup_term, load_document, split_document
import logging

def build_index(index, doclist):
    """in: existing index, list of document names to add to the index
    out: updated index, a dictionary whose keys are cleaned-up terms
         and whose values are a list of documents containing the term"""
    logging.debug("Building index")
    for docname in doclist:
        doctext = load_document(docname)
        for raw_term in split_document(doctext):
            term = cleanup_term(raw_term)
            if term and index.get(term, None):
                entry = index[term]
                if docname not in entry:
                    index[term].append(docname)
            else:
                index[term] = [docname]

def parse_query(raw_query):
    """in: a query as entered by the user
    out: a list whose keys are canonical terms from the query"""
    logging.debug("Parsing query")
    query = []
    for raw_term in raw_query.split(" "):
        term = cleanup_term(raw_term)
        if term not in query:
            query.append(term)
    
    return query

def search(query, index):
    """in: the document index and a query (in list form)
    out: a dictionary whose keys are candidate documents and whose values
         are lists of query terms found in the doc"""
    logging.debug("Searching")
    results = {}
    for term in query:
        if index.get(term, None):
            docs = index[term]
            for doc in docs:
                if results.get(doc, None):
                    results[doc].append(term)
                else:
                    results[doc] = [term]
    
    return results

def determine_relevance(query, query_result):
    """in: the original query and result of a search_for() call
    out: a list of (document,relevance) tuples"""
    logging.debug("Calculating relevance")
    rel_calc = {}
    for docname in query_result:
        terms = query_result[docname]
        relevance = 0
        for q_term in query:
            if q_term in terms:
                relevance += 1
        rel_calc[docname] = relevance

    return rel_calc
