from .Backend.file_system_entities import file, dir
import os

def create_tree(root_path, include_inside_method):
    '''Initializes the tree structure from the point of a given file'''
    

    if os.path.isfile(root_path):#If the element in question is a file
        if root_path.endswith('.py'):
            #Handles python files
            file_to_add = file(os.path.basename(root_path), 'file', root_path)
            file_to_add.compile_data(include_inside_method) #calculates all relevant values for the file
            return file_to_add
        else: return None #ignores all other files
    elif os.path.isdir(root_path):#If the element in question is a directory
   
        folder = dir(os.path.basename(root_path), 'folder', root_path)
        
        for item in os.listdir(root_path): #Performs all relative actions for the elements in the folder
            item_path = os.path.join(root_path, item)
            child = create_tree(item_path, include_inside_method) 
            if child: folder.add_child(child)
        
        folder.compile_data() #calculates all relevant values for the folder

        return folder

def get_data(root_path, settings_dict):
    root = create_tree(root_path, include_inside_method=settings_dict["include inside method"])
    method_data = {}
    root.retrieve_data(method_data, settings_dict)
    return method_data


    
