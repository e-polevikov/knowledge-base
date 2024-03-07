#pragma once

#include <iostream>

template<class T>
class array {
private:
    T* data_;
    size_t size_;
    size_t capacity_;

public:
    explicit array();
    array(size_t size, T value);
    array(const array &other);
    array(array &&other);

    array& operator=(const array &other);

    size_t size() const;
    T& operator[](size_t i) const;

    ~array();
};

template<class T>
array<T>::array()
    : data_(nullptr)
    , size_(0)
    , capacity_(0)
{
    std::cout << "array()" << std::endl;
}

template<class T>
array<T>::array(size_t size, T value) {
    size_ = size;
    capacity_ = 2 * size_;

    data_ = new T[capacity_];

    for (size_t i = 0; i < size_; i++) {
        data_[i] = value;
    }

    std::cout << "array(size_t size, T value)" << std::endl;
}

template<class T>
array<T>::array(const array<T> &other) {
    size_ = other.size_;
    capacity_ = other.capacity_;

    data_ = new T[capacity_];

    for (size_t i = 0; i < size_; i++) {
        data_[i] = other.data_[i];
    }

    std::cout << "array(const T& other)" << std::endl;
}

template<class T>
array<T>::array(array<T> &&other) {
    data_ = other.data_;
    size_ = other.size_;
    capacity_ = other.capacity_;

    other.data_ = nullptr;
    other.size_ = 0;
    other.capacity_ = 0;

    std::cout << "array(array<T> &&other)" << std::endl;
}

template<class T>
array<T>& array<T>::operator=(const array<T> &other) {
    if (this == &other) {
        return *this;
    }

    delete[] data_;

    size_ = other.size_;
    capacity_ = other.capacity_;

    data_ = new T[capacity_];

    for (size_t i = 0; i < size_; i++) {
        data_[i] = other.data_[i];
    }

    std::cout << "operator=(const array<T> &other)" << std::endl;

    return *this;
}

template<class T>
size_t array<T>::size() const {
    return size_;
}

template<class T>
T& array<T>::operator[](size_t i) const {
    return data_[i];
}

template<class T>
array<T>::~array() {
    delete[] data_;

    std::cout << "~array()" << std::endl;
}
