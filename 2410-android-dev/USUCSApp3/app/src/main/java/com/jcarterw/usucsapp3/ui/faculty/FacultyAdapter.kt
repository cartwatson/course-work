package com.jcarterw.usucsapp3.ui.faculty

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.usucsapp3.R

class FacultyAdapter(private val mFaculty: List<FacultyMember>) : RecyclerView.Adapter<FacultyAdapter.ViewHolder>() {

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val nameTextView: TextView = itemView.findViewById<TextView>(R.id.faculty_name)
        val titleTextView: TextView = itemView.findViewById<TextView>(R.id.faculty_title)
        val officeTextView: TextView = itemView.findViewById<TextView>(R.id.faculty_office)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): FacultyAdapter.ViewHolder {
        val context = parent.context
        val inflater = LayoutInflater.from(context)
        val facultyView = inflater.inflate(R.layout.item_facultymember, parent, false)
        return ViewHolder(facultyView)
    }

    override fun onBindViewHolder(viewHolder: FacultyAdapter.ViewHolder, position: Int) {
        val faculty: FacultyMember = mFaculty[position]
        val nameTextView = viewHolder.nameTextView
        nameTextView.text = faculty.name
        val titleTextView = viewHolder.titleTextView
        titleTextView.text = faculty.title
        val officeTextView = viewHolder.officeTextView
        officeTextView.text = faculty.office
    }

    override fun getItemCount(): Int {
        return mFaculty.size
    }
}