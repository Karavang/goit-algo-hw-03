import turtle


def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order, size=300):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Фрактал: Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень рекурсії (0 або більше): "))
        if level < 0:
            raise ValueError("Рівень рекурсії має бути невід'ємним числом.")
        draw_koch_snowflake(level)
    except ValueError as e:
        print("Помилка:", e)
