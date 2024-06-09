import ast

def string_to_list_of_lists(s):
    try:
        # Stringi liste listesine dönüştür
        list_of_lists = ast.literal_eval(s)
        # Tüm elemanların integer olduğunu kontrol et
        if all(isinstance(sublist, list) for sublist in list_of_lists) and \
           all(isinstance(item, int) for sublist in list_of_lists for item in sublist):
            return list_of_lists
        else:
            raise ValueError("String does not represent a list of lists of integers.")
    except (SyntaxError, ValueError):
        print("Invalid input format.")
        return None
