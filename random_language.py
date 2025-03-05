import random

languages = {
    "javascript": '''class Developer {
    constructor() {
        this.name = "Kremowka";
        this.role = "Developer";
        this.currently_learning = "Ruby";
        this.creating_bugs_since = "2020";
        this.language_spoken = ["pl_PL", "en_US"];
    }

    sayHi() {
        console.log("Thanks for stopping by, hope you find some of my work interesting.");
    }
}

const me = new Developer();
me.sayHi();''',

    "python": '''class Developer:
    def __init__(self):
        self.name = "Kremowka"
        self.role = "Developer"
        self.currently_learning = "Ruby"
        self.creating_bugs_since = "2020"
        self.language_spoken = ["pl_PL", "en_US"]

    def say_hi(self):
        print("Thanks for stopping by, hope you find some of my work interesting.")

me = Developer()
me.say_hi()''',

    "cplusplus": '''#include <iostream>
#include <vector>
using namespace std;

class Developer {
public:
    string name = "Kremowka";
    string role = "Developer";
    string currently_learning = "Ruby";
    string creating_bugs_since = "2020";
    vector<string> language_spoken = {"pl_PL", "en_US"};

    void sayHi() {
        cout << "Thanks for stopping by, hope you find some of my work interesting." << endl;
    }
};

int main() {
    Developer me;
    me.sayHi();
    return 0;
}''',

    "java": '''public class Developer {
    private String name = "Kremowka";
    private String role = "Developer";
    private String currently_learning = "Ruby";
    private String creating_bugs_since = "2020";
    private String[] language_spoken = {"pl_PL", "en_US"};

    public void sayHi() {
        System.out.println("Thanks for stopping by, hope you find some of my work interesting.");
    }

    public static void main(String[] args) {
        Developer me = new Developer();
        me.sayHi();
    }
}''',

    "csharp": '''using System;

class Developer {
    public string Name { get; } = "Kremowka";
    public string Role { get; } = "Developer";
    public string CurrentlyLearning { get; } = "Ruby";
    public string CreatingBugsSince { get; } = "2020";
    public string[] LanguageSpoken { get; } = { "pl_PL", "en_US" };

    public void SayHi() {
        Console.WriteLine("Thanks for stopping by, hope you find some of my work interesting.");
    }
}

class Program {
    static void Main() {
        Developer me = new Developer();
        me.SayHi();
    }
}'''
}

random_lang = random.choice(list(languages.keys()))

code = languages[random_lang]

readme_content = f"""# Hi! 👋

```{random_lang}
{code}
```"""
