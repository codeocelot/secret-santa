from random import shuffle


class Person:
    receive_from = None
    send_to = None

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}\n- giving to {}\n- receiving from {}\n".format(
            self.name, self.send_to.name, self.receive_from.name)


def secret_santa(names):
    """
    gist: create doubly linked list from names, with tail person giving to the
    head person and the head person recieving from the tail.
    """
    gifts = []
    if not names or len(names) == 1:
        raise Exception('invalid input')

    shuffle(names)
    for i, name in enumerate(names):
        person = Person(name)
        if i > 0:
            person.send_to = gifts[i - 1]
        gifts.append(person)

    for person in gifts:
        person.receive_from = next(
            (p for p in gifts if p.send_to and p.send_to.name == person.name),
            None)

    gifts[0].send_to = gifts[-1]
    gifts[-1].receive_from = gifts[0]

    return gifts


if __name__ == "__main__":
    matched_people = secret_santa(["john", "joey", "rory"])
    [print("{} giving to {}".format(person.name, person.send_to.name))
     for person in matched_people]
