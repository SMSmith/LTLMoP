#!/usr/bin/env python
"""
=================================================
naoInit.py - Nao Initialization Handler
=================================================

Initialize the proxies to access Nao modules
"""

try:
    import naoqi
    from naoqi import ALProxy
except ImportError:
    print "ERROR: Could not find naoqi Python module for interfacing with the Nao.  Is it installed correctly?"
    raise


class initHandler:
    def __init__(self, proj, calib=False):
        try:
            # Get connection settings from robot configuration file
            self.naoIP = proj.robot_data['NaoIP'][0]             # IP address (string)
            self.naoPort = int(proj.robot_data['NaoPort'][0])    # Port (number)
        except KeyError, ValueError:
            print "ERROR: Cannot find Nao connection settings ('NaoIP', 'NaoPort') in robot file."
            return None

    def createProxy(self, name):
        try:
            return ALProxy(name, self.naoIP, self.naoPort)
        except RuntimeError:
            print "ERROR: Cannot create %s proxy to Nao." % name
            print "ERROR: Make sure the Nao is turned on and connected to the network."
            return None

    def getSharedData(self):
        return {'NAO_INIT_HANDLER': self}
