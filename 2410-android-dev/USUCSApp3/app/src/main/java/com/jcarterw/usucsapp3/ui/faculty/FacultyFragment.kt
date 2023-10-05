package com.jcarterw.usucsapp3.ui.faculty

import android.R
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.usucsapp3.databinding.FragmentFacultyBinding


class FacultyFragment : Fragment() {
    private var _binding: FragmentFacultyBinding? = null

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentFacultyBinding.inflate(inflater, container, false)

        val view: View = inflater.inflate(com.jcarterw.usucsapp3.R.layout.fragment_faculty, container, false)
        val rvFaculty = view.findViewById<View>(com.jcarterw.usucsapp3.R.id.rvFaculty) as RecyclerView
        val facultyList = FacultyMember.createFacultyList()
        rvFaculty.setHasFixedSize(true)
        rvFaculty.layoutManager = LinearLayoutManager(view.context)
        rvFaculty.adapter = FacultyAdapter(facultyList)

        return view
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}