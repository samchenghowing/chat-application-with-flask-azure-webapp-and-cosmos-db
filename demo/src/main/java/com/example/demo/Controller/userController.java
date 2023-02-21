package com.example.demo.Controller;
import com.example.demo.Person;
import com.example.demo.Service.UserService;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/v1/user")
public class userController{
    private final UserService userService;

    @Autowired
    public userController(UserService userService) {
        this.userService = userService;
    }

    @GetMapping("/hello")
    public String hello(){
        return "Greeting from backend!!";
    }

    @GetMapping("/getAllUser")
    public List<Person> getUsers(){
        return userService.getUsers();
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getUser(@PathVariable int id) {
        Person u = userService.get(id);
        if (u!=null)
            return ResponseEntity
                .status(HttpStatus.OK)
                .body(u);
        else
            return ResponseEntity
            .status(HttpStatus.NOT_FOUND)
            .body("User not found!");
    }

    @PostMapping
    public void create(@RequestBody Person user) {
        userService.create(user);
    }

    @PutMapping
    public void update(@RequestBody Person user) {
        userService.update(user);
    }

    @DeleteMapping("/{id}")
    public void delete(@PathVariable int id){
        userService.delete(id);
}
}