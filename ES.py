from experta.fact import Fact, Field


class graphic_card(Fact):
    """
    CLIPS::

        (deftemplate graphic_card
                    (slot name)
                    (multislot functions)
                    (multislot inputs)
                    (slot memory)
                    (slot purpose)
                    (slot producer)
                    (slot price))
    """
    name = Field(str, mandatory=True)
    functions = Field(list, mandatory=True)
    inputs = Field(list, mandatory=True)
    memory = Field(int, mandatory=True)
    purpose = Field(str, mandatory=True)
    price = Field(int, mandatory=True)
    producer = Field(str, mandatory=True)
