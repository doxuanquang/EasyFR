def get_input():
    my_input = {
        "src_brand": input("Key in src brand: ")+"_",
        "src_env": input("Key in src env: ")+"_",
        "src_location": input("Key in src location: ")+"-",
        "src_function": input("Key in src function: "),
        "dst_brand": input("Key in dst brand: ")+"_",
        "dst_env": input("Key in dst env: ")+"_",
        "dst_location": input("Key in dst location: ")+"-",
        "dst_function": input("Key in dst function: "),
    }
    if my_input["src_function"]:
        my_input["src_function"] += "-"
    if my_input["dst_function"]:
        my_input["dst_function"] += "-"
    print(my_input["src_function"])
    return my_input

