# test_format_data.py

# ...
from secao20_testesEmPython.realPython_TestarCodigo.format_data import format_data_for_excel, format_data_for_display


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""