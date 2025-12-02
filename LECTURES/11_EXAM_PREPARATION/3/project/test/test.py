from unittest import TestCase,main


from project.senior_student import SeniorStudent

class SeniorStudentTest(TestCase):
    student_id = '1234'
    student_name = 'John'
    student_gpa = 1.5
    colleges = set()


    def setUp(self):
        self.st = SeniorStudent(self.student_id,self.student_name,self.student_gpa)


    def test_init_types(self):
        self.assertIsInstance(self.student_id,str)
        self.assertIsInstance(self.student_name,str)
        self.assertIsInstance(self.student_gpa, float)
        self.assertIsInstance(self.colleges, set)

    def test_student_id_less_then_4(self):
        with self.assertRaises(ValueError) as ve:
            self.st.student_id = '123'
        self.assertEqual("Student ID must be at least 4 digits long!",str(ve.exception))

    def test_student_name_cannot_be_null(self):
        with self.assertRaises(ValueError) as ve:
            self.st.name = ''
        self.assertEqual("Student name cannot be null or empty!",str(ve.exception))

    def test_test_student_gpa_less_then_error(self):
        with self.assertRaises(ValueError) as ve:
            self.st.student_gpa = 1
        self.assertEqual("Student GPA must be more than 1.0!",str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.st.student_gpa = 0.2
        self.assertEqual("Student GPA must be more than 1.0!", str(ve.exception))

    def test_init(self):
        self.assertEqual('1234',self.st.student_id)
        self.assertEqual('John',self.st.name)
        self.assertEqual(1.5, self.st.student_gpa)
        self.assertEqual(set(),self.st.colleges)

    def test_apply_to_collage_application_failed(self):
        result = self.st.apply_to_college(2.0,'Michigan')
        self.assertEqual('Application failed!',result)
        self.assertEqual(set(),self.st.colleges)



    def test_apply_to_collage_application_success(self):
        result = self.st.apply_to_college(1.0,'Harvard')
        self.assertEqual(f'{self.st.name} successfully applied to Harvard.',result)
        self.assertEqual({'HARVARD'},self.st.colleges)

    def test_update_gpa_not_successful(self):
        result = self.st.update_gpa(0.5)
        self.assertEqual('The GPA has not been changed!',result)

        result = self.st.update_gpa(1.0)
        self.assertEqual('The GPA has not been changed!', result)

    def test_update_gpa_successful(self):
        result = self.st.update_gpa(1.2)
        self.assertEqual('Student GPA was successfully updated.',result)
        self.assertEqual(1.2,self.st.student_gpa)

    def test_students_gpa_equal(self):
        st_2 = SeniorStudent('5678','Sam',self.student_gpa)
        result = self.st.__eq__(st_2)
        self.assertTrue(result)

    def test_students_gpa_not_equal(self):
        st_2 = SeniorStudent('5678','Sam',2.0)
        result = self.st.__eq__(st_2)
        self.assertFalse(result)


if __name__ == '__main__':
    main()