# infection
Project-based interview for Khan Academy

You can view this project live on http://infectionka.herokuapp.com.

The unit tests can be executed with "python tests.py" on the command line. To run the tests, please first install the dependencies in requirements.txt, and start a mongodb server locally. 

I've also created a web version of the tests, with the option to create (and delete) fake users with relationships. The relationships algorithm isn't very advanced (due to time constraints),
so it only creates users with exclusively "coaches" relationships and users with "is_coached_by" relationships, not both.
That being said, the infection algorithm is designed to recursively search through all user relationships, including users with 
both "coaches" and "is_coached_by" relationships.

Most of the relavant logic is contained in the models.py file and utils.py. I used mongodb to store the data (so I could use regular Python classes and functions for the User object). Flask is the framework, though it is only used for routing and templating, none of which pertains to the core logic of the project. A little jQuery is used on the frontend, mainly for Ajax calls and styling to show infected users (I hope John doesn't laugh at it!).

For my version of Limited Infection, I build clusters for each Coach-Student group (everyone potentially affected by an infection). This currently happens upon creation of the Users, but can be called anytime. The 'build_limited_infection' method creates an infection near the desired number by combining clusters, starting with the smallest.


