import re

# This method splits the sentence into strings by the given parameters, and wont return them 
re.split(r"[.?!]", "One sentence. Another one? And the last one!")

# This method works like replace, but instead is both matches AND replaces
re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recieved an email for go_nuts95@my.example.com")
# This example uses captured groups then specifies to put group 2 first, then group 1 so it will return Homer Simpson
re.sub(r"^([\w .-]*), ([\w .-]*)", r"\2 \1", "Simpson, Homer")