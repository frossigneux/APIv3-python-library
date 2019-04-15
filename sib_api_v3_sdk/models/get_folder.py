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


class GetFolder(object):
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
        'id': 'int',
        'name': 'str',
        'total_blacklisted': 'int',
        'total_subscribers': 'int',
        'unique_subscribers': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'total_blacklisted': 'totalBlacklisted',
        'total_subscribers': 'totalSubscribers',
        'unique_subscribers': 'uniqueSubscribers'
    }

    def __init__(self, id=None, name=None, total_blacklisted=None, total_subscribers=None, unique_subscribers=None):  # noqa: E501
        """GetFolder - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._total_blacklisted = None
        self._total_subscribers = None
        self._unique_subscribers = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.total_blacklisted = total_blacklisted
        self.total_subscribers = total_subscribers
        self.unique_subscribers = unique_subscribers

    @property
    def id(self):
        """Gets the id of this GetFolder.  # noqa: E501

        ID of the folder  # noqa: E501

        :return: The id of this GetFolder.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetFolder.

        ID of the folder  # noqa: E501

        :param id: The id of this GetFolder.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this GetFolder.  # noqa: E501

        Name of the folder  # noqa: E501

        :return: The name of this GetFolder.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetFolder.

        Name of the folder  # noqa: E501

        :param name: The name of this GetFolder.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def total_blacklisted(self):
        """Gets the total_blacklisted of this GetFolder.  # noqa: E501

        Number of blacklisted contacts in the folder  # noqa: E501

        :return: The total_blacklisted of this GetFolder.  # noqa: E501
        :rtype: int
        """
        return self._total_blacklisted

    @total_blacklisted.setter
    def total_blacklisted(self, total_blacklisted):
        """Sets the total_blacklisted of this GetFolder.

        Number of blacklisted contacts in the folder  # noqa: E501

        :param total_blacklisted: The total_blacklisted of this GetFolder.  # noqa: E501
        :type: int
        """
        if total_blacklisted is None:
            raise ValueError("Invalid value for `total_blacklisted`, must not be `None`")  # noqa: E501

        self._total_blacklisted = total_blacklisted

    @property
    def total_subscribers(self):
        """Gets the total_subscribers of this GetFolder.  # noqa: E501

        Number of contacts in the folder  # noqa: E501

        :return: The total_subscribers of this GetFolder.  # noqa: E501
        :rtype: int
        """
        return self._total_subscribers

    @total_subscribers.setter
    def total_subscribers(self, total_subscribers):
        """Sets the total_subscribers of this GetFolder.

        Number of contacts in the folder  # noqa: E501

        :param total_subscribers: The total_subscribers of this GetFolder.  # noqa: E501
        :type: int
        """
        if total_subscribers is None:
            raise ValueError("Invalid value for `total_subscribers`, must not be `None`")  # noqa: E501

        self._total_subscribers = total_subscribers

    @property
    def unique_subscribers(self):
        """Gets the unique_subscribers of this GetFolder.  # noqa: E501

        Number of unique contacts in the folder  # noqa: E501

        :return: The unique_subscribers of this GetFolder.  # noqa: E501
        :rtype: int
        """
        return self._unique_subscribers

    @unique_subscribers.setter
    def unique_subscribers(self, unique_subscribers):
        """Sets the unique_subscribers of this GetFolder.

        Number of unique contacts in the folder  # noqa: E501

        :param unique_subscribers: The unique_subscribers of this GetFolder.  # noqa: E501
        :type: int
        """
        if unique_subscribers is None:
            raise ValueError("Invalid value for `unique_subscribers`, must not be `None`")  # noqa: E501

        self._unique_subscribers = unique_subscribers

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
        if not isinstance(other, GetFolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
