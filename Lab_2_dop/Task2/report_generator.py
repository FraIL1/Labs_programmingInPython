from student_utils import load, get_average_age, get_top_students, filter_by_grade


def save_report(open_file, exit_file, min_ball=4.0):
    data = load(open_file)

    with open(exit_file, 'w', encoding='utf-8') as f:
        f.write("Топ студентов:\n" + '\n'.join(f"{s[0]} - {s[2]}" for s in get_top_students(data)))
        f.write(f"\n\nСредний возраст: {get_average_age(data)}\n")
        f.write(f"С баллом > {min_ball}: {len(filter_by_grade(data, min_ball))} студентов")


save_report("students.csv", "report.txt")