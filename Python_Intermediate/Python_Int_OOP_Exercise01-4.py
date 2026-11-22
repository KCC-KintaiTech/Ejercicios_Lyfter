"*** Python Intermediate - Object Oriented Programming: Human Body"
"*** Module Name:  human.py"
"*** Author:  Kattia Chavarria"
"*** Date:  2026-11-22"
"*** Notes:  Body part classes connected through attributes (composition):"
"            Human -> Torso -> Head, Arms (-> Hand), Legs (-> Feet)"
"*************************************************************************************************"


class Head:
    """The head of a human."""

    def __init__(self):
        pass


class Hand:
    """A hand, attached to the end of an arm."""

    def __init__(self):
        pass


class Arm:
    """An arm. It is connected to a hand."""

    def __init__(self, hand: Hand):
        self.hand = hand


class Foot:
    """A foot, attached to the end of a leg."""

    def __init__(self):
        pass


class Leg:
    """A leg. It is connected to a foot."""

    def __init__(self, feet: Foot):
        self.feet = feet


class Torso:
    """The torso is the center of the body: the head, both arms and both legs connect to it."""

    def __init__(self, head: Head, right_arm: Arm, left_arm: Arm, right_leg: Leg, left_leg: Leg):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg


class Human:
    """A human is made of a torso, which holds every other body part."""

    def __init__(self, name: str, torso: Torso):
        self.name = name
        self.torso = torso

    def describe(self):
        """Prints each body part by following the attribute connections."""
        print(f"{self.name} has:")
        print(f" - a  {type(self.torso).__name__}")
        print(f" - a  {type(self.torso.head).__name__}")
        print(f" - a right  ({type(self.torso.right_arm).__name__}) with a "
              f"{type(self.torso.right_arm.hand).__name__}")
        print(f" - a left  ({type(self.torso.left_arm).__name__}) with a "
              f"{type(self.torso.left_arm.hand).__name__}")
        print(f" - a right  ({type(self.torso.right_leg).__name__}) with "
              f"{type(self.torso.right_leg.feet).__name__}")
        print(f" - a left  ({type(self.torso.left_leg).__name__}) with "
              f"{type(self.torso.left_leg.feet).__name__}")


def main():
    # Build the body from the outside in: the smallest parts first, then what holds them
    head = Head()

    right_hand = Hand()
    left_hand = Hand()
    right_arm = Arm(right_hand)
    left_arm = Arm(left_hand)

    right_foot = Foot()
    left_foot = Foot()
    right_leg = Leg(right_foot)
    left_leg = Leg(left_foot)

    torso = Torso(head, right_arm, left_arm, right_leg, left_leg)
    human = Human("Kattia", torso)

    human.describe()

    # Parts are reached through attributes, from the human down to the smallest part
 

if __name__ == "__main__":
    main()