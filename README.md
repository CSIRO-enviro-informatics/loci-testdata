# loci-testdata

This repo contains source tests and verification data for tests as per https://confluence.csiro.au/display/DIPAAnalyticHubs/Loc-I+test+data

The `excelerator` dir contains csv files that can be used as inputs to the tool.

`gen-list-test-cases.py` uses the `excelerator` csv as input and generates `test_case_uris.csv`, 
which is a list of Loc-I URIs corresponding to the test cases A, B and C.

`test_case_withins_result.json` is an output of a sparql query to query URIs from `test_case_uris.csv` 
and produces corresponding URIs for things that are within.