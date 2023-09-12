from cuboid import cuboid


def main():
    print("Side lengths for first cuboid")
    cube1length = eval(input("Enter the length: "))
    cube1width = eval(input("Enter the width: "))
    cube1height = eval(input("Enter the height: "))

    print("Side lengths for first cuboid")
    cube2length = eval(input("Enter the length: "))
    cube2width = eval(input("Enter the width: "))
    cube2height = eval(input("Enter the height: "))

    c1 = cuboid(cube1length, cube1width, cube1height)
    c2 = cuboid(cube2length, cube2width, cube2height)

    print("--Addition--")
    print(c1 + c2)
    print("--Subtraction--")
    print(c1 - c2)
    print("--Less than comparison--")
    print(c1 < c2)
    print("--Greater than comparison--")
    print(c1 > c2)
    print("--Check for equality--")
    print(c1 == c2)
    print("--Surface area of first cuboid--")
    print(len(c1))
    print("--Surface area of second cuboid--")
    print(len(c2))
    print("--Cuboid 1--")
    print(str(c1))
    print("--Cuboid 2--")
    print(str(c2))


main()
