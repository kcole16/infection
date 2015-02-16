# infection
Project-based interview for Khan Academy

You can view this project live on http://infectionka.herokuapp.com.

I ran out of time to write traditional unit tests (and am admittedly not very experienced with writing very meaningful ones outside of server testing).
Instead, I've added the option to create (and delete), fake users with relationships. The relationships algorithm isn't very advanced (also due to time constraints),
so it only creates users with exclusively "coaches" relationships and users with "is_coached_by" relationships, not both.
That being said, the infection algorithm is designed to recursively search through all user relationships, including users with 
both "coaches" and "is_coached_by" relationships.

