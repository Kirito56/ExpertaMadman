from experta.engine import KnowledgeEngine
from experta.rule import Rule
from experta.deffacts import DefFacts

from ES import VideoCard


class DefFact(KnowledgeEngine):
    @DefFacts
    def init_videocards(self):
        """
        CLIPS::


        :return:
        """
        yield VideoCard(Start=True, Functions='DirectX', )
