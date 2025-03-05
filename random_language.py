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
```

## 🔧 Technologies & Tools

**Programming Languages:**

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" height="40" alt="javascript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" height="40" alt="typescript logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg" height="40" alt="c logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/cplusplus/cplusplus-original.svg" height="40" alt="cplusplus logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" height="40" alt="csharp logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" height="40" alt="java logo"  />
  <img width="12" />
</div>

##

**Frontend Development:**

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" height="40" alt="html5 logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" height="40" alt="css3 logo"  />
  <img width="12" />
  <img src="https://www.vectorlogo.zone/logos/tailwindcss/tailwindcss-icon.svg" alt="tailwindcss logo" width="40" height="40"/> </a>
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" height="40" alt="react logo"  />
</div>

##

**Currently Learning:**

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/ruby/ruby-original.svg" height="40" alt="ruby logo"  />
  <img width="12" />
</div>

##

## 🏆 GitHub Trophies

<div align="left">
    <img src="https://github-profile-trophy.vercel.app/?username=kr3mowka11&theme=gruvbox"  />
</div>

##

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=Kr3mowka11&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=dracula&locale=en&hide_border=false&order=1" width="400" height="200"/>
  <img src="https://github-readme-stats.vercel.app/api/top-langs?username=Kr3mowka11&locale=en&hide_title=false&layout=compact&langs_count=5&theme=dracula&hide_border=false&order=2" width="400" height="200"/>
</div>"""

with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
