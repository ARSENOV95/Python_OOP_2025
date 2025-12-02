from unittest import TestCase,main

from project.senior_student import SeniorStudent

class SeniorStudentTest(TestCase):
    student_id = '1234'
    name = 'Test'
    student_gpa = 4.5

    def setUp(self):
        self.student = SeniorStudent(self.student_id,self.name,self.student_gpa)

    def test_init(self):
        self.assertEqual(self.student_id,self.student.student_id)
        self.assertEqual(self.name,self.student.name)
        self.assertEqual(self.student_gpa,self.student.student_gpa)
        self.assertEqual(len(self.student.colleges),0)
        self.assertIsInstance(self.student.colleges,set)

    def test_student_id_too_short(self):
        with self.assertRaises(ValueError) as e:
            self.student.student_id = '123'
        self.assertEqual('Student ID must be at least 4 digits long!',str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.student_id = ' 123 '
        self.assertEqual('Student ID must be at least 4 digits long!', str(e.exception))

    def test_student_id_with_spaces(self):
        self.student.student_id = ' 1234 '
        self.assertEqual('1234',self.student.student_id)

    def test_name_valid(self):
        self.student.name = 'John Dow'
        self.assertEqual("John Dow",self.student.name)

        self.student.name = " John DOW "
        self.assertEqual(" John DOW ",self.student.name)

    def test_name_empty(self):
        with self.assertRaises(ValueError) as e:
            self.student.name = ""
        self.assertEqual("Student name cannot be null or empty!",str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.name = " "
        self.assertEqual("Student name cannot be null or empty!", str(e.exception))


    def test_gpa_valid(self):
        self.student.student_gpa = 1.01
        self.assertEqual(1.01,self.student.student_gpa)

    def test_gpa_too_small(self):
        with self.assertRaises(ValueError) as e:
            self.student.student_gpa = 1.0
        self.assertEqual("Student GPA must be more than 1.0!",str(e.exception))

        with self.assertRaises(ValueError) as e:
            self.student.student_gpa = 0.9
        self.assertEqual("Student GPA must be more than 1.0!",str(e.exception))


    def test_apply_to_college_low_gpa(self):
        expected =  'Application failed!'
        actual =  self.student.apply_to_college(4.6,'Harvard')
        self.assertEqual(expected,actual)
        self.assertEqual(0,len(self.student.colleges))

    def test_apply_to_college_success(self):
        expected =  'Test successfully applied to Harvard.'
        actual =  self.student.apply_to_college(4.3,'Harvard')
        self.assertEqual(expected,actual)
        self.assertEqual(1,len(self.student.colleges))
        self.assertIn("HARVARD",self.student.colleges)


    def test_apply_to_college_multiple(self):

        actual = self.student.apply_to_college(4.3, 'Harvard')
        actual = self.student.apply_to_college(4.3, 'Harvard')
        self.assertEqual(1,len(self.student.colleges))

    def test_update_gpa_fail(self):
        expected = 'The GPA has not been changed!'
        actual = self.student.update_gpa(1.0)
        self.assertEqual(expected,actual)
        self.assertEqual(4.5,self.student.student_gpa)

        actual = self.student.update_gpa(0.9)
        self.assertEqual(expected,actual)
        self.assertEqual(4.5,self.student.student_gpa)


    def test_update_gpa_success(self):
        expected = 'Student GPA was successfully updated.'
        actual = self.student.update_gpa(1.1)
        self.assertEqual(expected,actual)
        self.assertEqual(1.1,self.student.student_gpa)

    def test__eq__equal(self):
        student2 = SeniorStudent('5678','john',self.student_gpa)
        self.assertTrue(self.student == student2)

        self.assertFalse(1.1,self.student.student_gpa)


if __name__ == "__main__":
    main()

