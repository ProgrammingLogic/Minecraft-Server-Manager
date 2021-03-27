

# Go through every model in this directory, import it, and run the create model script.

import os
def import_models(app, db):
    models = {}

    for file_ in os.listdir(os.path.abspath('./models')):
        # Making sure it's a python file.
        if '.' in file_:
            file_name = '.'.join(file_.split('.')[:-1])
            file_ext = file_.split('.')[-1]
        else:
            continue

        # Making sure it's not a __<name>__ file.
        if file_name[:2] == '__' and file_name[-2:] == '__':
            continue
        else:
            exec(f"""from .{file_name} import {file_name}_create""")

        exec(f"""models['{file_name}'] = {file_name}_create(app, db)""")





