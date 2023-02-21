package com.example.demo.Service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

import com.example.demo.Person;

@Component
public class MyCommandRunner implements CommandLineRunner {
    private static final Logger logger = LoggerFactory.getLogger(MyCommandRunner.class);

    @Autowired
    private UserRepository repository;

    @Override
    public void run(String...args) throws Exception {
        if (repository.findAll().isEmpty()){ //insert data if no data in the database
            Person b1, b2, b3;
            b1 = new Person("Hac");
            b2 = new Person(" Trisha Gee");
            b3 = new Person("Greg L. Turnquist ");
            repository.save(b1);
            repository.save(b2);
            repository.save(b3);
        }

        // fetch all books
        logger.info("user found with findAll():");
        logger.info("-------------------------------");
        for (Person b : repository.findAll()) {
            logger.info(b.toString());
        }
    }
}