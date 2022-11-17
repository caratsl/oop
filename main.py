from vehicles import *



file_in()
if len(objects) == 0:
    print("Container is empty")
else:
    print("Container is filled")
    print(f"Contains {len(objects)} element(s)")
    sort_objects()
    for i in objects:
        i.print_info()
    f2 = open('out.txt', 'w')
    for i in objects:
        if i.get_type() == 'BUS':
            f2.write(i.get_info()+'\n')


    clear_container()
    print("Container is empty")
    print(f"Contains {len(objects)} element(s)")

