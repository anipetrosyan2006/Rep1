def egg_drop_plan(floors=100):
    n = 1
    total = 1
    while total < floors:
        n = n + 1
        total = total + n

    print("Ձվերի քանակը՝ 2, հարկերի քանակը՝", floors)
    print("Անհրաժեշտ քայլերի քանակը՝", n)
    print()

    floor = 0
    for step in range(1, n + 1):
        jump = n - step + 1
        floor = floor + jump

        if floor > floors:
            floor = floors

        print("Քայլ", step, ": նետել", floor, "-րդ հարկից (թռիչք =", jump, ")")

        if floor == floors:
            break


egg_drop_plan(100)