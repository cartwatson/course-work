package com.jcarterw.finalproject.ui.todo

import android.app.AlertDialog
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.finalproject.R
import com.jcarterw.finalproject.ui.Ticket

class TodoAdapter(private val mTicket: List<Ticket>,
                private val clickListener: (Ticket)-> Unit) : RecyclerView.Adapter<TodoAdapter.ViewHolder>() {

    inner class ViewHolder(itemView: View, clickAtPosition: (Int) -> Unit) : RecyclerView.ViewHolder(itemView) {
        val titleTextView: TextView = itemView.findViewById<TextView>(R.id.ticket_title)
        val descTextView: TextView = itemView.findViewById<TextView>(R.id.ticket_desc)
        val statusTextView: TextView = itemView.findViewById<TextView>(R.id.ticket_status)
        init {
            itemView.setOnClickListener {
                clickAtPosition(adapterPosition)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val context = parent.context
        val inflater = LayoutInflater.from(context)
        val ticketView = inflater.inflate(R.layout.item_ticket, parent, false)
        val viewHolder = ViewHolder(ticketView) {
            clickListener(mTicket[it])
        }
        return viewHolder
    }

    override fun onBindViewHolder(viewHolder: ViewHolder, position: Int) {
        val faculty: Ticket = mTicket[position]
        val titleTextView = viewHolder.titleTextView
        titleTextView.text = faculty.title
        val descTextView = viewHolder.descTextView
        descTextView.text = faculty.desc
        val statusTextView = viewHolder.statusTextView
        statusTextView.text = faculty.status
    }

    override fun getItemCount(): Int {
        return mTicket.size
    }
}