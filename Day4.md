# Day 4 Objective Challenge

### What is an example of two classes that would be related through composition?

Classes inherited that are related via composition have no meaningful value without the component they are related to and cannot exist outside of that sphere. If the parent class were to be destroyed, any other compositionally related classes would cease to exist. 

An example wpould be a human class that created a person, and a body part class that was used to generate indiviudal body parts assosciated with the already created human. Without the parent class, there can be no body parts. 

Another example would be a House class that has many individual room classes compositionally related. The rooms cannot exist without the house. 

### What is an example of two classes that would be related through aggregation?

On the otherhand we have aggregation relationships. These are relationships is relationships that can be detatched as the items are not fundamentally and inextractably linked. A student class that has been linked to a school can be separated and the student attached to a new school. 

Likewise, a second example would be a Team with a set of developers The team exists separately from the indiviudal developers, and whilst the relationship is initially important, if that instance of a team were destroyed, the developers could find another team. They are not reliant on the existence of that team. 