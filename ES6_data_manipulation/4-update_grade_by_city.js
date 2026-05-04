export default function updateStudentGradeByCity(students, city, newGrades) {
    return students.filter(student => student.location === city)
    .map(student => {
        const gradeobj = newGrades.find(grade => grade.studentId === student.id);
            if (gradeobj) {
                return {...student, grade: gradeobj.grade};
            } else {
                return {...student, grade: "N/A"};
            }
    });
}
