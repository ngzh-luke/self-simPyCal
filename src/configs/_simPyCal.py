""" App information/config """


class _SimPyCal:
    """ 
    An app configurations

    :param version: version assigned to the application
    :type version: str

    :param lastUpdatedDate: date that last updated corresponding to its version
    :type lastUpdatedDate: int

    :param licenseInfo: license information
    :type licenseInfo: str

        """
    version: str = "0.0.0"
    lastUpdatedDate: int = 20240820  # in format of YYYYMMDD
    licenseInfo: str = "MIT"

    def __init__(self, **kwargs) -> None:
        # iterates through the key-value pairs in the kwargs dictionary.
        for key, value in kwargs.items():
            # set an attribute on the instance with the name of the key and the corresponding value
            setattr(self, key, value)


simPyCal = _SimPyCal(version='0.0.1', lastUpdatedDate=20240820)
# print(simPyCal.version, simPyCal.lastUpdatedDate, simPyCal.licenseInfo)
