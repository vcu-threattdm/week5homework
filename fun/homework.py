"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    retval = max(incoming_list)
    return retval


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    retval = min(incoming_list)
    return retval


def add_list_numbers(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Add all the values together and return it.
    """

   if incoming_list:
    retval = sum(incoming_list)
   else:
    retval = 0
   return retval


def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    
    if not incoming_dict:
        return none
    
    all_keys = incoming_dict.keys()
    if not all_keys:
        return none
    
    keys_with_longest_value = none
    for key in all_keys:
        if not key_with_longest_value:
            key_with_longest_value = key
            
        if len(incoming_dict[key]) > len(incoming_dict[key_with_longest_value]):
            key_with_longest_value = key
     return key_with_longest_value
    
