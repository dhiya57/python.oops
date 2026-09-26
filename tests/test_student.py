from module.student.student import ParentGuardian, Student


def test_parent_guardian_fields_are_stored():
    parent = ParentGuardian(
        name="Anita Sharma",
        relationship="Mother",
        mobile_number="9876543210",
        email_address="anita@example.com",
        preferred_communication_method="WhatsApp",
    )

    assert parent.name == "Anita Sharma"
    assert parent.relationship == "Mother"
    assert parent.mobile_number == "9876543210"
    assert parent.email_address == "anita@example.com"
    assert parent.preferred_communication_method == "WhatsApp"


def test_student_fields_are_stored_and_parent_linked():
    parent = ParentGuardian(
        name="Rohit Verma",
        relationship="Father",
        mobile_number="9123456780",
    )

    student = Student(
        name="Aarav Verma",
        date_of_birth="2014-08-10",
        age=12,
        gender="Male",
        mobile_number="9988776655",
        email_address="aarav@example.com",
        preferred_language="English",
        school_name="Green Valley School",
        class_name="7",
        board="CBSE",
        academic_year="2026-2027",
        subjects=["Mathematics", "Science"],
        current_level={"Mathematics": "Grade 6", "Science": "Grade 6"},
        areas_of_help=["Fractions", "Photosynthesis"],
        parent_guardian=parent,
    )

    assert student.name == "Aarav Verma"
    assert student.date_of_birth == "2014-08-10"
    assert student.age == 12
    assert student.gender == "Male"
    assert student.mobile_number == "9988776655"
    assert student.email_address == "aarav@example.com"
    assert student.preferred_language == "English"
    assert student.school_name == "Green Valley School"
    assert student.class_name == "7"
    assert student.board == "CBSE"
    assert student.academic_year == "2026-2027"
    assert student.subjects == ["Mathematics", "Science"]
    assert student.current_level == {"Mathematics": "Grade 6", "Science": "Grade 6"}
    assert student.areas_of_help == ["Fractions", "Photosynthesis"]
    assert student.parent_guardian == parent
