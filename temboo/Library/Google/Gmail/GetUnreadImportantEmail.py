# -*- coding: utf-8 -*-

###############################################################################
#
# GetUnreadImportantEmail
# Allows you to access a read-only Gmail feed that contains a list of unread emails that are marked important.
#
# Python versions 2.6, 2.7, 3.x
#
# Copyright 2014, Temboo Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
#
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution

import json

class GetUnreadImportantEmail(Choreography):

    def __init__(self, temboo_session):
        """
        Create a new instance of the GetUnreadImportantEmail Choreo. A TembooSession object, containing a valid
        set of Temboo credentials, must be supplied.
        """
        super(GetUnreadImportantEmail, self).__init__(temboo_session, '/Library/Google/Gmail/GetUnreadImportantEmail')


    def new_input_set(self):
        return GetUnreadImportantEmailInputSet()

    def _make_result_set(self, result, path):
        return GetUnreadImportantEmailResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return GetUnreadImportantEmailChoreographyExecution(session, exec_id, path)

class GetUnreadImportantEmailInputSet(InputSet):
    """
    An InputSet with methods appropriate for specifying the inputs to the GetUnreadImportantEmail
    Choreo. The InputSet object is used to specify input parameters when executing this Choreo.
    """
    def set_Password(self, value):
        """
        Set the value of the Password input for this Choreo. ((required, password) A Google App-specific password that you've generated after enabling 2-Step Verification. See the Gmailv2 bundle for OAuth.)
        """
        super(GetUnreadImportantEmailInputSet, self)._set_input('Password', value)
    def set_ResponseMode(self, value):
        """
        Set the value of the ResponseMode input for this Choreo. ((optional, string) Used to simplify the response. Valid values are: simple and verbose. When set to simple, only the message string is returned. Verbose mode returns the full object. Defaults to "simple".)
        """
        super(GetUnreadImportantEmailInputSet, self)._set_input('ResponseMode', value)
    def set_Username(self, value):
        """
        Set the value of the Username input for this Choreo. ((required, string) Your full Google email address e.g., martha.temboo@gmail.com. See the Gmailv2 bundle for OAuth.)
        """
        super(GetUnreadImportantEmailInputSet, self)._set_input('Username', value)

class GetUnreadImportantEmailResultSet(ResultSet):
    """
    A ResultSet with methods tailored to the values returned by the GetUnreadImportantEmail Choreo.
    The ResultSet object is used to retrieve the results of a Choreo execution.
    """

    def getJSONFromString(self, str):
        return json.loads(str)

    def get_Response(self):
        """
        Retrieve the value for the "Response" output from this Choreo execution. (The response from Google.)
        """
        return self._output.get('Response', None)

class GetUnreadImportantEmailChoreographyExecution(ChoreographyExecution):

    def _make_result_set(self, response, path):
        return GetUnreadImportantEmailResultSet(response, path)