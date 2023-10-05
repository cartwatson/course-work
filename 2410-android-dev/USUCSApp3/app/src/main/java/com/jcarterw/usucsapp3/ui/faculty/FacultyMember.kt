package com.jcarterw.usucsapp3.ui.faculty

class FacultyMember(val name: String, val title: String, val office: String) {
    companion object {
        fun createFacultyList() : ArrayList<FacultyMember> {
            val facultyMembers = ArrayList<FacultyMember>()
            // Hard code faculty list
            facultyMembers.add(FacultyMember("Mahdi Nasrullah Al-Ameen", "Assistant Professor", "Old Main 401F"))
            facultyMembers.add(FacultyMember("Vicki Allan","Associate Professor", "Old Main 429"))
            facultyMembers.add(FacultyMember("Soukaina Filali Boubrahimi", "Assistant Professor", "Old Main 401A"))
            facultyMembers.add(FacultyMember("Heng-Da Cheng", "Professor", "Old Main 401B"))
            facultyMembers.add(FacultyMember("Isaac Cho", "Assistant Professor", "Old Main 402G"))
            facultyMembers.add(FacultyMember("Stephen Clyde", "Emeritus Associate Professor", "Old Main 418"))
            facultyMembers.add(FacultyMember("Joseph Ditton", "Professional Practice Assistant Professor", "Old Main 420"))
            facultyMembers.add(FacultyMember("Curtis Dyreson", "Professor", "Old Main 402A"))
            facultyMembers.add(FacultyMember("John Edwards", "Assistant Professor", "Old Main 401D"))
            facultyMembers.add(FacultyMember("Nicholas Flann", "Associate Professor", "Old Main 402C"))
            return facultyMembers
        }

    }
}