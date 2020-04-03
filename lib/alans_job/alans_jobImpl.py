# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os
import time
from installed_clients.KBaseReportClient import KBaseReport
from installed_clients.DataFileUtilClient import DataFileUtil
from installed_clients.SetAPIClient import SetAPI
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
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

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
        report = KBaseReport(self.callback_url)
        dfu = DataFileUtil(self.callback_url)
        set_client = SetAPI(self.srv_wiz_url)
        print(set_client.status())

        iterations = 50
        while(iterations > 0):
            time.sleep(3)
            path = dfu.download_web_file(
                {'file_url': "http://kbase.us/wp-content/uploads/2016/09/Kbase_Logo_newWeb.png",
                 'download_type': 'Direct Download'}).get(
                'copy_file_path')

            print("Downloaded file to", path)
            iterations-=1


        report_info = report.create({'report': {'objects_created':[],
                                                'text_message': f'The app is done. We downloaded {iterations} files'},
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
