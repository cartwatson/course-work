#ifndef NODE_HPP
#define NODE_HPP

template <typename T>
class Node
{
  public:
    Node(T data)
    {
      m_data = data;
    }

    T getData(void)
    {
      return m_data;
    }

    void setData(T item)
    {
      m_data = item;
    }

    Node<T>* getNext(void)
    {
      return m_pNext;
    }

    void setNext(Node<T>* next)
    {
      m_pNext = next;
    }

  private:
    Node<T>* m_pNext = nullptr;
    T m_data;
};

#endif // NODE_HPP