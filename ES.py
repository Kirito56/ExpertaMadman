from experta.fact import Fact, Field

class VideoCard(Fact):
    """
    CLIPS::

        (deftemplate VideoCard
                    (slot Start)
                    (multislot Functions)
                    (multislot Connector)
                    (slot TheAmountOfMemory)
                    (slot Appointment)
                    (slot Selector)
                    (slot Price))
    """
    Start = Field(bool, mandatory=True)
    Functions = Field(list, mandatory=True)
    Connector = Field(list, mandatory=True)
    TheAmountOfMemory = Field(int, mandatory=True)
    Appointment = Field(str, mandatory=True)
    Selector = Field(str, mandatory=True)
    Price = Field(str, mandatory=True)