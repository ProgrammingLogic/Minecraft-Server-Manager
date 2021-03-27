import os

def create_routes(app, db):
    for file_ in os.listdir(os.path.abspath('./routes')):
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

        exec(f"""{file_name}_create(app, db)""")
