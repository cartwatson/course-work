package com.jcarterw.finalproject.ui

import android.R.attr.data
import android.content.Context
import java.io.IOException
import java.io.OutputStreamWriter


class Ticket(val title: String, val desc: String, val status: String) {
    companion object {
        private val tickets = ArrayList<Ticket>()

        fun getTickets() : ArrayList<Ticket> {
            return tickets
        }

        fun createTicket(title: String, desc: String, status: String) {
            tickets.add(Ticket(title, desc, status))
        }

        fun deleteTicket(title: String, desc: String, status: String) {
            // find ticket to remove
            var ticketToBeRemoved: Ticket? = null
            for (ticket in tickets) {
                if (ticket.title == title && ticket.desc == desc && ticket.status == status) {
                    ticketToBeRemoved = ticket
                    break
                }
            }
            // only attempt to remove if a matching ticket is found
            if (ticketToBeRemoved != null) { tickets.remove(ticketToBeRemoved) }
        }

        fun changeStatus(title: String, desc: String, prevStatus: String, nextStatus: String) {
            this.deleteTicket(title, desc, prevStatus)
            this.createTicket(title, desc, nextStatus)
        }

        fun wholeToString(): String {
            var returnString = ""
            for (ticket in tickets) {
                returnString += ticket.title + "**********"
                returnString += ticket.desc + "**********"
                returnString += ticket.status + "\n"
            }
            return returnString
        }
    }
}