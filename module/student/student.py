

class studentclass:
    def __init__(
        self,
        name=None,
        date_of_birth=None,
        age=None,
        gender=None,
        mobile_number=None,
        email_address=None,
        preferred_language=None,
        school_name=None,
        class_name=None,
        board=None,
        academic_year=None,
        subjects=None,
        current_level=None,
        areas_of_help=None,
        parent_guardian=None,
    ):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = age
        self.gender = gender
        self.mobile_number = mobile_number
        self.email_address = email_address
        self.preferred_language = preferred_language
        self.school_name = school_name
        self.class_name = class_name
        self.board = board
        self.academic_year = academic_year
        self.subjects = subjects if subjects is not None else []
        self.current_level = current_level if current_level is not None else {}
        self.areas_of_help = areas_of_help if areas_of_help is not None else []
        self.parent_guardian = parent_guardian

