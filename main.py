from lib import Circle, Figures, Triangle

figures = {str(i): sub for i, sub in enumerate(Figures.__subclasses__(), 1)}

print("Вычислить площадь для:")
for key, val in figures.items():
    print(f"{key} - {val.type}")

selected_type = input()
try:
    variables = input(f"Введите {', '.join(figures[selected_type].variables)}\n").split()

    selected_figure = figures[selected_type](variables)

    print(selected_figure.calculate())

    if isinstance(selected_figure, Triangle):
        print(selected_figure.check_right_angled())
except KeyError:
    print("Необходимо ввести одно из этих значений:\n"
          f"{' '.join(figures.keys())}")




