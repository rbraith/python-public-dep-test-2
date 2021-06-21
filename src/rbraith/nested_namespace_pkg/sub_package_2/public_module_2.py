import rbraith.nested_namespace_pkg.sub_package_1.public_module_1 as public_module_1

def public_function_3():
    print(f"Public function 3! (Depends on public-python-test-1 v0.2.0: {public_module_1.public_function_2()})")