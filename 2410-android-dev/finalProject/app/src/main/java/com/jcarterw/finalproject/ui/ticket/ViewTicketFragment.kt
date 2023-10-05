package com.jcarterw.finalproject.ui.ticket

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import com.jcarterw.finalproject.R
import com.jcarterw.finalproject.databinding.FragmentViewTicketBinding

class ViewTicketFragment : Fragment() {
    private var _binding: FragmentViewTicketBinding? = null

    private val binding get() = _binding!!

    override fun onCreateView(inflater: LayoutInflater, container: ViewGroup?, savedInstanceState: Bundle? ): View {
//        val CreateTicketViewModel = ViewModelProvider(this).get(CreateTicketViewModel::class.java)
        _binding = FragmentViewTicketBinding.inflate(inflater, container, false)
        val view: View = inflater.inflate(R.layout.fragment_view_ticket, container, false)

        return binding.root
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}