package com.example.demo.Service;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.example.demo.Person;

@Repository
public interface UserRepository extends JpaRepository<Person, Integer> {
}