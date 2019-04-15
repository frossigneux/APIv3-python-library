# coding: utf-8

"""
    SendinBlue API

    SendinBlue provide a RESTFul API that can be used with any languages. With this API, you will be able to :   - Manage your campaigns and get the statistics   - Manage your contacts   - Send transactional Emails and SMS   - and much more...  You can download our wrappers at https://github.com/orgs/sendinblue  **Possible responses**   | Code | Message |   | :-------------: | ------------- |   | 200  | OK. Successful Request  |   | 201  | OK. Successful Creation |   | 202  | OK. Request accepted |   | 204  | OK. Successful Update/Deletion  |   | 400  | Error. Bad Request  |   | 401  | Error. Authentication Needed  |   | 402  | Error. Not enough credit, plan upgrade needed  |   | 403  | Error. Permission denied  |   | 404  | Error. Object does not exist |   | 405  | Error. Method not allowed  |   # noqa: E501

    OpenAPI spec version: 3.0.0
    Contact: contact@sendinblue.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RequestSmsRecipientExport(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'notify_url': 'str',
        'recipients_type': 'str'
    }

    attribute_map = {
        'notify_url': 'notifyURL',
        'recipients_type': 'recipientsType'
    }

    def __init__(self, notify_url=None, recipients_type=None):  # noqa: E501
        """RequestSmsRecipientExport - a model defined in Swagger"""  # noqa: E501

        self._notify_url = None
        self._recipients_type = None
        self.discriminator = None

        if notify_url is not None:
            self.notify_url = notify_url
        self.recipients_type = recipients_type

    @property
    def notify_url(self):
        """Gets the notify_url of this RequestSmsRecipientExport.  # noqa: E501

        URL that will be called once the export process is finished  # noqa: E501

        :return: The notify_url of this RequestSmsRecipientExport.  # noqa: E501
        :rtype: str
        """
        return self._notify_url

    @notify_url.setter
    def notify_url(self, notify_url):
        """Sets the notify_url of this RequestSmsRecipientExport.

        URL that will be called once the export process is finished  # noqa: E501

        :param notify_url: The notify_url of this RequestSmsRecipientExport.  # noqa: E501
        :type: str
        """

        self._notify_url = notify_url

    @property
    def recipients_type(self):
        """Gets the recipients_type of this RequestSmsRecipientExport.  # noqa: E501

        Filter the recipients based on how they interacted with the campaign  # noqa: E501

        :return: The recipients_type of this RequestSmsRecipientExport.  # noqa: E501
        :rtype: str
        """
        return self._recipients_type

    @recipients_type.setter
    def recipients_type(self, recipients_type):
        """Sets the recipients_type of this RequestSmsRecipientExport.

        Filter the recipients based on how they interacted with the campaign  # noqa: E501

        :param recipients_type: The recipients_type of this RequestSmsRecipientExport.  # noqa: E501
        :type: str
        """
        if recipients_type is None:
            raise ValueError("Invalid value for `recipients_type`, must not be `None`")  # noqa: E501
        allowed_values = ["all", "delivered", "answered", "softBounces", "hardBounces", "unsubscribed"]  # noqa: E501
        if recipients_type not in allowed_values:
            raise ValueError(
                "Invalid value for `recipients_type` ({0}), must be one of {1}"  # noqa: E501
                .format(recipients_type, allowed_values)
            )

        self._recipients_type = recipients_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RequestSmsRecipientExport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
