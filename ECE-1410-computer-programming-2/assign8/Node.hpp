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

    Node<T>* getRight(void)
    {
      return m_pRight;
    }

    void setRight(Node<T>* right)
    {
      m_pRight = right;
    }

    Node<T>* getLeft(void)
    {
      return m_pLeft;
    }

    void setLeft(Node<T>* left)
    {
      m_pLeft = left;
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
    Node<T>* m_pRight = nullptr;
    Node<T>* m_pLeft = nullptr;
    Node<T>* m_pNext = nullptr;
    T m_data;
};

#endif // NODE_HPP