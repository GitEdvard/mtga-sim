from test_resources.skirmish_builder import SkirmishBuilder
from tests.unit.test_base import TestBase


class TestSkirmish(TestBase):
    def test_all_died(self):
        # Arrange
        skirmish_builder = SkirmishBuilder()
        skirmish_builder.with_attacking("2/2")\
            .with_defending("1/1")\
            .with_defending("3/1")
        skirmish = skirmish_builder.build()

        # Act
        skirmish.combat()

        # Assert
        assert len(skirmish.died) == 3

    def test_two_died_of_three(self):
        # Arrange
        skirmish_builder = SkirmishBuilder()
        skirmish_builder.with_attacking("2/2")\
            .with_defending("1/1")\
            .with_defending("3/3")
        skirmish = skirmish_builder.build()

        # Act
        skirmish.combat()

        # Assert
        assert len(skirmish.died) == 2
