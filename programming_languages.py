prog_languages = {
    "Go" : "A statically typed, compiled programming language designed at Google",
    "Java" : "A high-level, class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible",
    "Python"  : "Python is widely regarded as a programming language that’s easy to learn, due to its simple syntax, a large library of standards and toolkits",
    "JavaScript"  : "JavaScript is the most popular programming language for building interactive websites",
    "C++"  : "C++ is an extension of C that works well for programming the systems that run applications, as opposed to the applications themselves."
}

for i in range (5):
    language = prog_languages [(str(input("Enter language:")))]
    print(language)