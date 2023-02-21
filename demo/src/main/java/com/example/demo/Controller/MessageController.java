package com.example.demo.Controller;
import com.example.demo.User;

import java.util.ArrayList;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/messages")
public class MessageController{

    @GetMapping("/hello")
    public String hello(){
        return "Greeting from backend!!";
    }
    @GetMapping("/testList")
    public ArrayList<User> helloFromList(){
        ArrayList<User> persons = new ArrayList<>();
        User john = new User(1, "John");
        User mary = new User(2, "Mary");

        persons.add(mary);
        persons.add(john);
        return persons;
    }
}