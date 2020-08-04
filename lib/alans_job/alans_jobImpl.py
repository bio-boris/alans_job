# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import time
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.DataFileUtilClient import DataFileUtil

#END_HEADER


class alans_job:
    '''
    Module Name:
    alans_job

    Module Description:
    A KBase module: alans_job
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = "https://bio-boris@github.com/bio-boris/alans_job.git"
    GIT_COMMIT_HASH = "004e3981996b6a211c6d65a1fb10d27118b8dbe0"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        import pprint
        pprint.pprint(config)
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        self.srv_wiz_url = config['srv-wiz-url']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass


    def run_alans_job(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_alans_job
        SERVICE_VER = 'release'
        print("i'm so cool i'm so fashionble")
        import time
        time.sleep(10)
        print("i'm so cool i'm so fashionble")
        #TODO ADD ,service_ver='fake'
        report = KBaseReport(self.callback_url)
        dfu = DataFileUtil(self.callback_url)
        dwf = {'download_type' : 'Google Drive',
               'file_url' : 'www.google.com'}
        filepath = dfu.download_web_file(params=dwf)
        print("Filepath is", filepath)
        
        print("About to open refdata")
        with open("data/kmer") as f:
            data = f.readlines()
        print(data)

        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': f'The app is done. We didnt do anything'},
                                                'workspace_name': params['workspace_name']})
        output = {
            'report_name': report_info['name'],
            'report_ref': report_info['ref'],
        }
        #END run_alans_job

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_alans_job return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
