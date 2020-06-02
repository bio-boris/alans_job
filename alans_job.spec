/*
A KBase module: alans_job
*/

module alans_job {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_alans_job(mapping<string,UnspecifiedObject> params) returns () authentication required;

};
