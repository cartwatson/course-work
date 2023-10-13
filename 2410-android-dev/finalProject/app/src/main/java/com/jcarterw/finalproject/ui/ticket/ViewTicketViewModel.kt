package com.jcarterw.finalproject.ui.ticket

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData

class ViewTicketViewModel {
    private val _text = MutableLiveData<String>().apply {
        value = "This is ViewTicket Fragment"
    }
    val text: LiveData<String> = _text
}