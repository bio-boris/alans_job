# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

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
    GIT_COMMIT_HASH = "445da7dddebaf55bb64afbeeb7d2c32e51fe8f4c"

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
        """
        # ctx is the context object
        #BEGIN run_alans_job
        SERVICE_VER = 'release'
        print("i'm so cool i'm so fashionble")
        import time
        time.sleep(120)
        print("i'm so cool i'm so fashionble")

        pass
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
