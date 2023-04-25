package com.jcarterw.webbrowser;

public class History {
    // node class for doubly linked list
    private class node {
        String data;
        node prev;
        node next;

        node(String data) { this.data = data; }
        node(String data, node prev, node next) {
            this.data = data;
            this.prev = prev;
            this.next = next;
        }
    }

    node head;
    node curr;
    node tail;

    History() {
        node home = new node("home", null, null);
        head = home;
        tail = home;
        curr = home;
    }

    // merge with addNode
    public void appendNode (String d) {
        // if garbage collector doesn't work
        // TODO: Delete all nodes after curr, if necessary
        node temp = new node(d);
        tail.next = temp;
        temp.prev = tail;
        temp.next = null;
        tail = temp;
        curr = tail;
    }

    // add node at specific point and remove all nodes after - using garbage collector
    public void addNode (String data) {
        tail.prev = null;
        tail = curr;
        appendNode(data);
    }

    public void prevCurr () {
        // TODO: check for being at beginning of list
        curr = curr.prev;
    }
    public void nextCurr () {
        // TODO: check for begin at end of list
        curr = curr.next;
    }
}
