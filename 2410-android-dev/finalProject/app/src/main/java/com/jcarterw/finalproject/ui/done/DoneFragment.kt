package com.jcarterw.finalproject.ui.done

import android.app.AlertDialog
import android.content.Context
import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.finalproject.R
import com.jcarterw.finalproject.ui.Ticket
import com.jcarterw.finalproject.databinding.FragmentDoneBinding
import com.jcarterw.finalproject.ui.todo.TodoAdapter
import java.io.*


class DoneFragment : Fragment() {
    private var _binding: FragmentDoneBinding? = null

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle?): View {
        _binding = FragmentDoneBinding.inflate(inflater, container, false)
        val view: View = inflater.inflate(R.layout.fragment_done, container, false)

        // create list of valid tickets ------------------------------------------------------------
        val doneList = ArrayList<Ticket>()
        readTickets()
        // add ticket if it has to do status
        for (ticket in Ticket.getTickets()) {
            if (ticket.status == "DONE") {
                doneList.add(ticket)
            }
        }

        val rvDone = view.findViewById<View>(R.id.rvDone) as RecyclerView


        // popup view ticket dialog ----------------------------------------------------------------
        // init variables
        val dialogBuilder = AlertDialog.Builder(requireActivity())
        val viewTicketPopupView = inflater.inflate(R.layout.fragment_view_ticket, container, false)
        dialogBuilder.setView(viewTicketPopupView)
        val viewDialog = dialogBuilder.create()

        val viewTicketTitle = viewTicketPopupView.findViewById<View>(R.id.popup_view_ticket_title) as TextView
        val viewTicketDesc = viewTicketPopupView.findViewById<View>(R.id.popup_view_ticket_desc) as TextView
        val viewTicketStatus = viewTicketPopupView.findViewById<View>(R.id.popup_view_ticket_status) as TextView

        val viewTicketExitButton = viewTicketPopupView.findViewById<View>(R.id.btnCancel)
        val newTicketPopupDelete = viewTicketPopupView.findViewById<View>(R.id.btnDelete)
        val viewTicketSaveButton = viewTicketPopupView.findViewById<View>(R.id.btnSubmit)

        // add on click listeners to buttons
        viewTicketExitButton.setOnClickListener(View.OnClickListener { viewDialog.dismiss() })

        newTicketPopupDelete.setOnClickListener(View.OnClickListener {
            Ticket.deleteTicket(viewTicketTitle.text.toString(), viewTicketDesc.text.toString(), viewTicketStatus.text.toString())
            saveTickets()
            viewDialog.dismiss()
            refreshPage(rvDone, viewTicketTitle, viewTicketDesc, viewTicketStatus, viewDialog)
        })

        viewTicketSaveButton.setOnClickListener(View.OnClickListener { // change status
            Ticket.deleteTicket(viewTicketTitle.text.toString(), viewTicketDesc.text.toString(), viewTicketStatus.text.toString())
            saveTickets()
            viewDialog.dismiss()
            refreshPage(rvDone, viewTicketTitle, viewTicketDesc, viewTicketStatus, viewDialog)
        })

        // recycler view ---------------------------------------------------------------------------
        rvDone.setHasFixedSize(false)
        rvDone.layoutManager = LinearLayoutManager(view.context)
        val adapter = TodoAdapter(doneList) {
            viewTicketTitle.text = it.title
            viewTicketDesc.text = it.desc
            viewTicketStatus.text = it.status

            viewDialog.show()
        }
        rvDone.adapter = adapter


        // popup create ticket dialog --------------------------------------------------------------
        // init variables
        val createTicketPopupView = inflater.inflate(R.layout.fragment_create_ticket, container, false)

        val newTicketPopupTitle = createTicketPopupView.findViewById<View>(R.id.popup_title) as TextView
        val newTicketPopupTicketTitle = createTicketPopupView.findViewById<View>(R.id.input_title) as TextView
        val newTicketPopupTicketDesc = createTicketPopupView.findViewById<View>(R.id.input_desc) as TextView

        val newTicketPopupCancel = createTicketPopupView.findViewById<View>(R.id.btnCancel)
        val newTicketPopupSave = createTicketPopupView.findViewById<View>(R.id.btnSubmit)

        dialogBuilder.setView(createTicketPopupView)
        val createDialog = dialogBuilder.create()

        // create on click listeners
        newTicketPopupCancel.setOnClickListener(View.OnClickListener { createDialog.dismiss() })

        newTicketPopupSave.setOnClickListener(View.OnClickListener {
            // handle no input for title/desc
            var noError = true
            if (newTicketPopupTicketTitle.text.toString() == "") {
                newTicketPopupTitle.text = "Create a Ticket\nTitle cannot be empty!"
                noError = false
            } else if (newTicketPopupTicketDesc.text.toString() == "") {
                newTicketPopupTitle.text = "Create a Ticket\nDescription cannot be empty!"
                noError = false
            }

            // handle creating new ticket
            if (noError) {
                // create ticket
                Ticket.createTicket( newTicketPopupTicketTitle.text.toString(), newTicketPopupTicketDesc.text.toString(), "TODO")
                saveTickets()
                // clear text and selection
                newTicketPopupTicketTitle.text = null
                newTicketPopupTicketDesc.text = null
                createDialog.dismiss()
                // TODO: refresh page
                refreshPage(rvDone, viewTicketTitle, viewTicketDesc, viewTicketStatus, viewDialog)
            }
        })

        // create ticket button --------------------------------------------------------------------
        val createTicket = view.findViewById<View>(R.id.create_ticket)
        createTicket.setOnClickListener(View.OnClickListener {
            createDialog.show()
        })

        return view
    }

    private fun refreshPage(rvDone: RecyclerView, viewTicketTitle: TextView, viewTicketDesc: TextView, viewTicketStatus: TextView, viewDialog: AlertDialog) {
        val doneList = ArrayList<Ticket>()
        readTickets()
        // add ticket if it has to do status
        for (ticket in Ticket.getTickets()) {
            if (ticket.status == "DONE") {
                doneList.add(ticket)
            }
        }
        val adapter = DoneAdapter(doneList) {
            viewTicketTitle.text = it.title
            viewTicketDesc.text = it.desc
            viewTicketStatus.text = it.status

            viewDialog.show()
        }
        rvDone.adapter = adapter
        adapter.notifyDataSetChanged()
    }

    private fun saveTickets() {
        try {
            val outputStreamWriter = OutputStreamWriter(context?.openFileOutput("info.txt", Context.MODE_PRIVATE))
            outputStreamWriter.write(Ticket.wholeToString())
            outputStreamWriter.close()
        } catch (e: IOException) {
            println("Exception" + "File write failed: " + e.toString())
        }
    }

    private fun readTickets() {
        // TODO NOTE: this implementation is incredibly slow not sure of the proper way rn
        try {
            val inputStreamReader = InputStreamReader(context?.openFileInput("info.txt"))
            if (inputStreamReader != null) {
                val bufferedReader = BufferedReader(inputStreamReader)

                // read in all ticket information
                var ticketsToBeAdded: ArrayList<List<String>> = ArrayList()
                for (line in bufferedReader.readLines()) {
                    val array: List<String> = line.split("**********")
                    ticketsToBeAdded.add(array)
                }

                // find out which tickets we already have
                var ticketsNotToBeAdded: ArrayList<List<String>> = ArrayList()
                for (ticket1 in ticketsToBeAdded) {
                    for (ticket in Ticket.getTickets()) {
                        if (ticket1[0] == ticket.title && ticket1[1] == ticket.desc && ticket1[2] == ticket.status) {
                            ticketsNotToBeAdded.add(ticket1)
                        }
                    }
                }

                // don't add tickets we already have
                ticketsToBeAdded.removeAll(ticketsNotToBeAdded)
                for (ticket in ticketsToBeAdded) {
                    Ticket.createTicket(ticket[0], ticket[1], ticket[2])
                }
                inputStreamReader.close()
            }
        } catch (e: FileNotFoundException) {
            println("Exception - File not found: $e")
        } catch (e: IOException) {
            println("Exception - File read failed: $e")
        }
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}