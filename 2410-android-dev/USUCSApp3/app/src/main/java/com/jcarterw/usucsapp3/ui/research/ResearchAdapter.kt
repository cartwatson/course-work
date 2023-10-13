package com.jcarterw.usucsapp3.ui.research

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.usucsapp3.R

class ResearchAdapter(private val mFaculty: List<ResearchTopic>) : RecyclerView.Adapter<ResearchAdapter.ViewHolder>() {

    inner class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {
        val titleTextView: TextView = itemView.findViewById<TextView>(R.id.research_title)
        val descTextView: TextView = itemView.findViewById<TextView>(R.id.research_desc)
        val facultyTextView: TextView = itemView.findViewById<TextView>(R.id.research_faculty)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ResearchAdapter.ViewHolder {
        val context = parent.context
        val inflater = LayoutInflater.from(context)
        val researchView = inflater.inflate(R.layout.item_researchtopic, parent, false)
        return ViewHolder(researchView)
    }

    override fun onBindViewHolder(viewHolder: ResearchAdapter.ViewHolder, position: Int) {
        val research: ResearchTopic = mFaculty[position]
        val titleTextView = viewHolder.titleTextView
        titleTextView.text = research.title
        val descTextView = viewHolder.descTextView
        descTextView.text = research.desc
        val facultyTextView = viewHolder.facultyTextView
        facultyTextView.text = research.staff
    }

    override fun getItemCount(): Int {
        return mFaculty.size
    }
}