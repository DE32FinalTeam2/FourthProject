package com.test.load;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.stereotype.Controller;

@SpringBootApplication
public class LoadTestApplication {

    public static void main(String[] args) {
        SpringApplication.run(LoadTestApplication.class, args);
    }
}

@Controller
class LoadTestController {

    @RequestMapping("/")
    public String home() {
        return "test.html";  // test.html 파일을 반환
    }
}
