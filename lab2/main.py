from inventory import Inventory


def main():
    inv = Inventory()
    inv["stone"] = 25
    inv["wood"] = 15
    print(inv)

    inv2 = Inventory()
    inv2["silver"] = 5
    inv2["wood"] = 10
    inv2["diamond"] = 4
    print(inv2)

    combined = inv + inv2
    print(combined)

    if 'diamond' in inv2:
        print("В инвентаре2 есть алмазы.")
    else:
        print("В инвентаре2 нет алмазов.")

    del inv2["diamond"]
    print(inv2)
    if 'diamond' in inv2:
        print("В инвентаре2 есть алмазы.")
    else:
        print("В инвентаре2 нет алмазов.")


if __name__ == "__main__":
    main()
