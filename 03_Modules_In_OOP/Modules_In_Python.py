# what is module in python?

# lets do an example


def circle(radius: float) -> None:
    area = 3.14 * radius * radius
    print(f"Area of circle with radius {radius} = {area}")


def rectangle(length: float, breath: float) -> None:
    area = length * breath
    print(f"Area of rectangle = {area}")


def triangle(base: float, height: float) -> None:
    area = 0.5 * height * base
    print(f"Area of triangle = {area}")


# circle(56.474)
# rectangle(23, 42)


# concepts of If main ?
# why we use it?

if __name__ == "__main__":
    circle(56.474)
    rectangle(23, 42)