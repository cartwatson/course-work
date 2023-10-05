package com.jcarterw.usucsapp3.ui.research

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.fragment.app.Fragment
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.jcarterw.usucsapp3.databinding.FragmentResearchBinding


class ResearchFragment : Fragment() {
    private var _binding: FragmentResearchBinding? = null

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        _binding = FragmentResearchBinding.inflate(inflater, container, false)

        val view: View = inflater.inflate(com.jcarterw.usucsapp3.R.layout.fragment_research, container, false)
        val rvResearch = view.findViewById<View>(com.jcarterw.usucsapp3.R.id.rvResearch) as RecyclerView
        val researchList = ResearchTopic.createResearchList()
        rvResearch.setHasFixedSize(true)
        rvResearch.layoutManager = LinearLayoutManager(view.context)
        rvResearch.adapter = ResearchAdapter(researchList)

        return view
    }

    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }
}