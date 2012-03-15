import logging
import sys
import getopt

from helpers import setup_logging, GRADING
from engine import build_index, parse_query, search, determine_relevance

def Runner(build_index, parse_query, search, determine_relevance):
    
    logging.log(GRADING, "")
    logging.log(GRADING, "-- STARTING TO RUN --")
    
    index = {}
    documentlist = ["us_constitution", "magna_carta", "un_charter"]
    
    build_index(index, documentlist)
    logging.log(GRADING, "INDEX")
    logging.log(GRADING, index)
    
    print "There are {0} documents in the index".format(len(documentlist))
    print "There are {0} terms in the index".format(len(index))
    logging.log(GRADING, "STATISTICS")
    logging.log(GRADING, "{0} docs, {1} terms".format(
        len(documentlist),
        len(index),
    ))
    
    user_query = raw_input("enter your query>")
    query = parse_query(user_query)
    logging.log(GRADING, "QUERY")
    logging.log(GRADING, query)
    
    candidate_set = search(query, index)
    logging.log(GRADING, "CANDIDATE_SET")
    logging.log(GRADING, candidate_set)
    
    relevant_results = determine_relevance(query, candidate_set)
    logging.log(GRADING, "RELEVANT_RESULTS")
    logging.log(GRADING, relevant_results)
    
    results = relevant_results.items()
    results.sort(key=lambda i: i[1], reverse=True)
    print 'The best results for "{0}" are:'.format(user_query)
    for result in results:
        print result
    print '[end of results]'

    logging.log(GRADING, "-- ENDED RUN CLEANLY --")

def process_args(argv):
    try:
        opts, args = getopt.getopt(argv, "gh", ["grade", "help"])
    except getopt.GetoptError:
        usage()
        sys.exit(1)
    
    extended_logging = False
    for opt, arg in opts:
        if opt in ("-g", "--grade"):
            extended_logging = True
        elif opt in ("-h", "--help"):
            usage()
            sys.exit()
    
    filename = "".join(args)
    if filename == "":
        filename = "output.log"
    
    if extended_logging:
        print "Verbose logging is turned on; outputting to {0}".format(filename)
        setup_logging(filename, grading=True)
    else:
        setup_logging(filename, grading=False)

def usage():
    print sys.argv[0]
    print "Optional argument --grade (-g) to turn on grading output"

if __name__=="__main__":
    
    process_args(sys.argv[1:])
    Runner(build_index, parse_query, search, determine_relevance)