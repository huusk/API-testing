def execute_main_function_from_file(file_name):
    with open(file_name, encoding="utf-8") as f:
        code = compile(f.read(), file_name, "exec")
        namespace = {}
        exec(code, namespace)
        if 'test_main' in namespace and callable(namespace['test_main']):
            print(f"Executing main function in {file_name}")
            namespace['test_main']()
        else:
            print(f"'main' function not found in {file_name}")

# List of files with main functions to execute in order
files_with_main_functions = [
    "NevtreeguiDataAwah.py",
    "NevtreeguiNegjAwah.py",
    "NevtreeguiTulburTulult.py",
    "NevtrenDataAwah.py",
    "NevtrenNegjAwah.py",
    "NevtrenTulburTulult.py",
    "TaniiDansand_HeregleeniiDelgerengui.py",
    "Univision_bagts_check.py",
]

# Execute each main function in the specified order
for file_name in files_with_main_functions:
    execute_main_function_from_file(file_name)
