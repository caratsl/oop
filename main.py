from vehicles import *



file_in()
if len(objects) == 0:
    print("Container is empty")
else:
    print("Container is filled")
    print(f"Contains {len(objects)} element(s)")
    for i in objects:
        i.print_info()
    clear_container()
    print("Container is empty")
    print(f"Contains {len(objects)} element(s)")

