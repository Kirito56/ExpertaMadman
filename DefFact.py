from experta.engine import KnowledgeEngine
from experta.rule import Rule
from experta.deffacts import DefFacts

from ES import VideoCard


class DefFact(KnowledgeEngine):
    @DefFacts
    def init_videocards(self):
        """
        CLIPS::
        (deffacts initfacts "Initial Facts"
            (graphic_card
                (name MSI_PCI-Ex_GeForce_GT_730)
                (functions DirectX_12 OpenGL_4.4)
                (inputs DVI VGA HDMI)
                (memory 2)
                (purpose office)
                (price 3000)
                (producer nVidia))
            (graphic_card
                (name Gigabyte_PCI-Ex_GeForce_GT_710)
                (functions DirectX_12 OpenGL_4.5)
                (inputs DVI VGA HDMI)
                (memory 2)
                (purpose pro)
                (price 5000)
                (producer nVidia))
            (graphic_card
                (name Palit_PCI-Ex_GeForce_GTX_1650_GamingPro)
                (functions DirectX_12 OpenGL_4.6)
                (inputs DisplayPort HDMI)
                (memory 4)
                (purpose gaming)
                (price 14000)
                (producer nVidia))
            (graphic_card
                (name MSI_PCI-Ex_GeForce_RTX_3060_Gaming_X)
                (functions DirectX_12 OpenGL_4.6)
                (inputs DisplayPort HDMI)
                (memory 12)
                (purpose gaming)
                (price 30000)
                (producer nVidia))

            (graphic_card
                (name AFOX_PCI-Ex_Radeon_R5_220)
                (functions DirectX_12 OpenGL_4.4)
                (inputs DVI-D VGA HDMI)
                (memory 2)
                (purpose office)
                (price 1000)
                (producer AMD))
            (graphic_card
                (name Biostar_PCI-Ex_Radeon_RX_550)
                (functions DirectX_12 OpenGL_4.4)
                (inputs DVI DisplayPort HDMI)
                (memory 2)
                (purpose office)
                (price 6000)
                (producer AMD))
            (graphic_card
                (name Gigabyte_PCI-Ex_Radeon_RX_5500_XT)
                (functions DirectX_12 OpenGL_4.6)
                (inputs DisplayPort HDMI)
                (memory 4)
                (purpose basic)
                (price 11000)
                (producer AMD))
            (graphic_card
                (name XFX_PCI-Ex_Radeon_RX_6600_Speedster_SWFT_210)
                (functions DirectX_12 OpenGL_4.5)
                (inputs DisplayPort HDMI)
                (memory 12)
                (purpose pro)
                (price 28000)
                (producer AMD))

            (graphic_card
                (name missing))
        )

        :return:
        """

        @Rule(graphic_card(purpose='gaming'))
        def FindGamingCard(self):
            """
            Rule where found card for gaming

            :return: Found
            :rtype: str
            """
        return print('Found')

        yield VideoCard(Start=True, Functions='DirectX', )
