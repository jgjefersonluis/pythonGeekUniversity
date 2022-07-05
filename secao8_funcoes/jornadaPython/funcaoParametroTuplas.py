def maior_30(*args):
    print(args)
    print(type(args))

    for num in args:
        if num > 30:
            print(num)
maior_30(10, 20, 30, 40, 50, 60)

