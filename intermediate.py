def find_string_in_list(string_looking = "cherries",
list_finding = ["apples", "oranges", "bananas", "grapes"] ):
    """ 
    This function allegedly looks for string_looking in list_finding and returns the string_looking if the string is found in the link. But what does it do if it can't find the string? WHO KNOWS....
    """
    
    found = False
    size = len(list_finding)
    for i in range(0, size):
        if list_finding[i] == string_looking:
            found = True

    return found

find_string_in_list()
