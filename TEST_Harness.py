
import pandas as pd
import numpy as np
import pytest

student_file = "out.csv.zip"
solution_file = "SOL_test_labels.csv"

df_student = pd.read_csv(student_file)
df_student = df_student.drop(columns=["comment_text"])
df_solution = pd.read_csv(solution_file)

'''# Check if the student file has the same number of rows as the solution file
assert df_student.shape[0] == df_solution.shape[0], "Number of rows in student file does not match the number of rows in the solution file"
print("Length:", df_student.shape[0])

corr_cols = ["toxic_y", "severe_toxic_y", "obscene_y", "threat_y", "insult_y", "identity_hate_y"]
sub_cols = ["toxic_x", "severe_toxic_x", "obscene_x", "threat_x", "insult_x", "identity_hate_x"]
tests = []
for i, row in df_solution.iterrows():
    for j in range(len(corr_cols)):
        student_val = df_student.loc[i, sub_cols[j]]
        correct_val = row[corr_cols[j]]
        tests.append((student_val, correct_val))

print("Tests:", len(tests))

@pytest.mark.parametrize("test_input, expected", tests)
def test_1(test_input, expected):
    assert test_input == expected
'''
#########################################

tests = []

for i, row in df_solution.iterrows():
    row_id = row["id"]
    student_row = df_student.iloc[i]
    assert student_row["id"] == row_id, "Student file has rows in different order"
    #student_row = df_student[df_student["id"] == row_id]
    #assert student_row.shape[0] == 1, "Student file has duplicate rows"
    #student_row = student_row.drop(columns=["id"]).to_list()[0]
    #solution_row = row.drop(labels=["id"]).to_list()
    student_row = student_row.drop(columns=["id"]).values.tolist()[0]
    solution_row = row.drop(labels=["id"]).values.tolist()
    tests.append((student_row, solution_row))

pytestmark = pytest.mark.parametrize("student_val, correct_val", tests)

class TestClass:
    def test_toxic(self, student_val, correct_val):
        assert student_val[0] == correct_val[0]

    def test_severe_toxic(self, student_val, correct_val):
        assert student_val[1] == correct_val[1]

    def test_obscene(self, student_val, correct_val):
        assert student_val[2] == correct_val[2]

    def test_threat(self, student_val, correct_val):
        assert student_val[3] == correct_val[3]

    def test_insult(self, student_val, correct_val):
        assert student_val[4] == correct_val[4]

    def test_identity_hate(self, student_val, correct_val):
        assert student_val[5] == correct_val[5]
