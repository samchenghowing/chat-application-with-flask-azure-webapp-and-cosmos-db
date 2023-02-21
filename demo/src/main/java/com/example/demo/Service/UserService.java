package com.example.demo.Service;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.example.demo.Person;

@Service
public class UserService {

   @Autowired
   private UserRepository repo;

   public UserService() {
   }

   public List<Person> getUsers(){
      List<Person> users = repo.findAll();
      return users;
   }

   public Person get(int id) {
      Person b  =  repo.findById(id).orElse(null);
      return b;
   }

   public void create(Person user) {
      repo.save(user);
   }

   public void update(Person user) {
      repo.save(user);
   }

   public void delete(int id){
      repo.deleteById(id);
   }

}
