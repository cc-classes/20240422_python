def bigger_function_name(a, b, *args, d, **kwargs):
    # 1 2 (3, 4, 5) 2 {'e': 3, 'f': 5}
    print(a, b, args, d, kwargs)


bigger_function_name(1, 2, 3, 4, 5, d=2, e=3, f=5)
