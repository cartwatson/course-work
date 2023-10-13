package com.jcarterw.finalproject.ui.ticket

import androidx.lifecycle.LiveData
import androidx.lifecycle.MutableLiveData

class CreateTicketViewModel {
    private val _text = MutableLiveData<String>().apply {
        value = "This is CreateTicket Fragment"
    }
    val text: LiveData<String> = _text
}