# Copyright of the Board of Trustees of  Columbia University in the City of New York
"""
This script unit starts and tests the communications between server and client(s).
"""

import threading
#from virtualscanner.coms.coms_ui.GUI_test_functions import GUItestclass
from GUI_test_functions import GUItestclass
#from virtualscanner.coms.coms_ui.coms_server_flask import launch_virtualscanner
from coms_server_flask import launch_virtualscanner
import time
import unittest
from pprint import pprint


# import webbrowser
# import subprocess
# from virtualscanner.utils import constants


def selenium_function():
    time.sleep(10)
    # This URL needs to be changed to the server address if running on a remote client on the local network
    # webbrowser.open("http://0.0.0.0:5000/")
   ###
   # return GUI_test_functions.launch_tests()
   ###
    runner = unittest.TextTestRunner()
    result = runner.run(unittest.makeSuite(GUItestclass))

    # Do all tests as you want here and get 200 responses.
    # Figure out how to report 200 responses if required
    # webbrowser.close()
    return result


#class GUI_test_case(unittest.TestCase):
 #   t = threading.Thread(target=selenium_function)
class ThreadWithReturn(threading.Thread):
    # Copied from stack overflow question # 6893968
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._return = None

    def run(self):
        target = getattr(self, '_target')
        if not target is None:
            self._return = target(*getattr(self, '_args'), **getattr(self,'_kwargs'))

    def join(self, *args, **kwargs):
        super().join(*args, **kwargs)
        return self._return
#
#

# class TestGUIFunctions(unittest.TestCase):
#     def test_gui_all(self):
#         t_sel = ThreadWithReturn(target=selenium_function)
#         t_sel.daemon = True
#
#
#         t_sel.start()
#         coms_server_flask.launch_virtualscanner()
#
# #        coms_server_flask.launch_virtualscanner()
#         self.assertEqual(t_sel.join(), "Test Code")




if __name__ == '__main__':
    t = threading.Thread(target=selenium_function)
    t.daemon = True
    t.start()
    launch_virtualscanner()
   #unittest.main()

