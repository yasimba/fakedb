class DBOperations(object):
    """Perform operations between one or more fakedb instances"""

    def join(self,dict1,dict2):
        """inner join 2 databases to form a new one
        :type dict1: dictionary
        :param dict1: destination dictionary in which to join changes
        :type dict2: dictionary
        :param dict2: source dictionary whose values will overwrite destination's values
        :return: new dictionary containing join of dict1 and dict2
        """
        #Python 3.5+ join
        new_dict = {**dict1,**dict2}
        return new_dict
