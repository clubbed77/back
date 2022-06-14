def print_name(name="Adam", *names, **more_names):
    print("Hello " + name)
    for one_name in names:
        print('goodbye ' + one_name)

    print ("-------------")
    for name, surname in more_names.items():
        print(f"good day {name} {surname}")    

#args kwargs

