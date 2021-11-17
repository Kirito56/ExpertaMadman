from experta.fact import Fact, Field


class graphic_card(Fact):
    """
    CLIPS::

        (deftemplate graphic_card
                    (slot Name)
                    (multislot Functions)
                    (multislot Connector)
                    (slot TheAmountOfMemory)
                    (slot Appointment)
                    (slot Selector)
                    (slot Price))
    """
    name = Field(str, mandatory=True)
    functions = Field(list, mandatory=True)
    inputs = Field(list, mandatory=True)
    memory = Field(int, mandatory=True)
    purpose = Field(str, mandatory=True)
    price = Field(int, mandatory=True)
    producer = Field(str, mandatory=True)
