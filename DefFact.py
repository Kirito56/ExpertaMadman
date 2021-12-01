from experta import rule
from experta.engine import KnowledgeEngine
from experta.fieldconstraint import L
from experta.rule import Rule
from experta.deffacts import DefFacts
from experta.shortcuts import MATCH
from experta.conditionalelement import TEST

from ES import graphic_card


class DefFact(KnowledgeEngine):
    @DefFacts()
    def init_card(self):
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
        """
        OpenGL = ['OpenGL_4.4', 'OpenGL_4.5', 'OpenGL_4.6']
        yield graphic_card(name='MSI_PCI-Ex_GeForce_GT_730',
                           functions=["DirectX_12", OpenGL[0]],
                           inputs=['DVI', 'VGA', 'HDMI'],
                           memory=2,
                           purpose='office',
                           price=3000,
                           producer='nVidia')
        yield graphic_card(name='Gigabyte_PCI-Ex_GeForce_GT_710',
                           functions=['DirectX_12', OpenGL[1]],
                           inputs=['DVI', 'VGA', 'HDMI'],
                           memory=2,
                           purpose='pro',
                           price=5000,
                           producer='nVidia')
        yield graphic_card(name='Palit_PCI-Ex_GeForce_GTX_1650_GamingPro',
                           functions=['DirectX_12', OpenGL[2]],
                           inputs=['DisplayPort', 'HDMI'],
                           memory=4,
                           purpose='gaming',
                           price=14000,
                           producer='nVidia')
        yield graphic_card(name='MSI_PCI-Ex_GeForce_RTX_3060_Gaming_X)',
                           functions=['DirectX_12', OpenGL[2]],
                           inputs=['DisplayPort', 'HDMI'],
                           memory=12,
                           purpose='gaming',
                           price=30000,
                           producer='nVidia')

        yield graphic_card(name='AFOX_PCI-Ex_Radeon_R5_220',
                           functions=['DirectX_12', OpenGL[0]],
                           inputs=['DVI-D', 'VGA', 'HDMI'],
                           memory=2,
                           purpose='office',
                           price=1000,
                           producer='AMD')
        yield graphic_card(name='Biostar_PCI-Ex_Radeon_RX_550',
                           functions=['DirectX_12', OpenGL[0]],
                           inputs=['DVI', 'DisplayPort', 'HDMI'],
                           memory=2,
                           purpose='office',
                           price=6000,
                           producer='AMD')
        yield graphic_card(name='Gigabyte_PCI-Ex_Radeon_RX_5500_XT',
                           functions=['DirectX_12', OpenGL[2]],
                           inputs=['DisplayPort', 'HDMI'],
                           memory=4,
                           purpose='basic',
                           price=11000,
                           producer='AMD')
        yield graphic_card(name='XFX_PCI-Ex_Radeon_RX_6600_Speedster_SWFT_210',
                           functions=['DirectX_12', OpenGL[1]],
                           inputs=['DisplayPort', 'HDMI'],
                           memory=12,
                           purpose='pro',
                           price=28000,
                           producer='AMD')

        yield graphic_card(name='missing',
                            functions=[None],
                            inputs=[None],
                            memory=0,
                            purpose=f'{None}',
                            price=0,
                            producer=f'{None}')

    @Rule(graphic_card(purpose='gaming'))
    def findGamingCard(self):
        return print('Found')


    @Rule(graphic_card(inputs=MATCH.inputs))
    def findHDMI(self, inputs):
        if 'HDMI' in inputs:
            return print('Found card with HDMI input')

    @Rule(graphic_card(price=MATCH.price), TEST(lambda price: price<10000))
    def findByPrice(self, price):
        return print(price)
        
    @Rule(graphic_card(purpose=~L('gaming'), inputs=MATCH.inputs))
    def findFactWhereNotGamingCard(self, inputs):
        if 'DVI' in inputs:
            return print(f'Found card with DVI input')
