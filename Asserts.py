from ES import graphic_card
from experta.engine import KnowledgeEngine


class Asserts(KnowledgeEngine):
    def init_graphic_card(self):
        self.declare(graphic_card(name='MSI_PCI-Ex_GeForce_GT_730',
                                  functions=['DirectX_12', 'OpenGL_4.4'],
                                  inputs=['DVI', 'VGA', 'HDMI'],
                                  memory=2,
                                  purpose='office',
                                  price=3000,
                                  producer='nVidia'))
        self.declare(graphic_card(name='Gigabyte_PCI-Ex_GeForce_GT_710',
                                  functions=['DirectX_12' ,'OpenGL_4.5'],
                                  inputs=['DVI' ,'VGA', 'HDMI'],
                                  memory=2,
                                  purpose='pro',
                                  price=5000,
                                  producer='nVidia'))
