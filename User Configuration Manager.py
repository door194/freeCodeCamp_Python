test_settings = {"theme": "dark", "notifications": "enabled", "volume": "high"}

#setting 1 & 2
def add_setting (dictset, keyval):
    key, value = keyval
    key = key.lower()
    value = value.lower()
    if key in dictset.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        dictset[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!" 

#update setting 3 & 4
def update_setting(dictset, keyval):
    key, value = keyval
    key = key.lower()
    value = value.lower()
    if key in dictset.keys():
        dictset[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


#delete setting 5 & 6
def delete_setting(dictset, key):
    key = key.lower()
    if key in dictset.keys():
        dictset.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

#view settings 7 & 8
def view_settings(dictset):
    if not dictset:
        return "No settings available."
    else:
        return ("Current User Settings:\n" + '\n'.join(f'{key.title()}: {value}' for key, value in dictset.items()) + "\n")
