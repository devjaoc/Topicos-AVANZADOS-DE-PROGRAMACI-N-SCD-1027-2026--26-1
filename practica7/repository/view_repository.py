
class ViewRepository:
    def get_view_for_role(self, role: str):
        print("Role:" +role)
        if role == "admin":
            from ui.main_view import MainView
            return  MainView()              
                
        if role == "student":
            from ui.main_student_view import MainStudentView
            return MainStudentView()
            
        if role == "teacher":
            from ui.main_teacher_view import MainTeacherView
            return MainTeacherView()
            
        raise ValueError("Rol no reconocido")