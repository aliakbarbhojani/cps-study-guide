import unittest
import cps_code
import os
import random

class TestTopic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load the JSON file once for all tests
        file_path = os.path.join(
            os.path.dirname(__file__),
            "cps213_study_guide.json"
        )
        cls.data = cps_code.load_json(file_path)

        # Create an object to access the Topic methods
        cls.menu = cps_code.Topic(
            None, None, None, None, None, None, None, None
        )

    def test_topic_01(self):
        topic = self.menu.get_topic(self.data, 1)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_02(self):
        topic = self.menu.get_topic(self.data, 2)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_03(self):
        topic = self.menu.get_topic(self.data, 3)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_04(self):
        topic = self.menu.get_topic(self.data, 4)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_05(self):
        topic = self.menu.get_topic(self.data, 5)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_06(self):
        topic = self.menu.get_topic(self.data, 6)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_07(self):
        topic = self.menu.get_topic(self.data, 7)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_08(self):
        topic = self.menu.get_topic(self.data, 8)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_09(self):
        topic = self.menu.get_topic(self.data, 9)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_10(self):
        topic = self.menu.get_topic(self.data, 10)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_11(self):
        topic = self.menu.get_topic(self.data, 11)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_12(self):
        topic = self.menu.get_topic(self.data, 12)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_13(self):
        topic = self.menu.get_topic(self.data, 13)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_14(self):
        topic = self.menu.get_topic(self.data, 14)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_15(self):
        topic = self.menu.get_topic(self.data, 15)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_16(self):
        topic = self.menu.get_topic(self.data, 16)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_17(self):
        topic = self.menu.get_topic(self.data, 17)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_18(self):
        topic = self.menu.get_topic(self.data, 18)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_19(self):
        topic = self.menu.get_topic(self.data, 19)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_20(self):
        topic = self.menu.get_topic(self.data, 20)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_21(self):
        topic = self.menu.get_topic(self.data, 21)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_22(self):
        topic = self.menu.get_topic(self.data, 22)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_23(self):
        topic = self.menu.get_topic(self.data, 23)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_24(self):
        topic = self.menu.get_topic(self.data, 24)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_25(self):
        topic = self.menu.get_topic(self.data, 25)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_26(self):
        topic = self.menu.get_topic(self.data, 26)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_27(self):
        topic = self.menu.get_topic(self.data, 27)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_28(self):
        topic = self.menu.get_topic(self.data, 28)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_29(self):
        topic = self.menu.get_topic(self.data, 29)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_30(self):
        topic = self.menu.get_topic(self.data, 30)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_31(self):
        topic = self.menu.get_topic(self.data, 31)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_32(self):
        topic = self.menu.get_topic(self.data, 32)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_33(self):
        topic = self.menu.get_topic(self.data, 33)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_34(self):
        topic = self.menu.get_topic(self.data, 34)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_35(self):
        topic = self.menu.get_topic(self.data, 35)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_36(self):
        topic = self.menu.get_topic(self.data, 36)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_37(self):
        topic = self.menu.get_topic(self.data, 37)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_38(self):
        topic = self.menu.get_topic(self.data, 38)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_39(self):
        topic = self.menu.get_topic(self.data, 39)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_topic_40(self):
        topic = self.menu.get_topic(self.data, 40)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.title)

    def test_random_fact(self):
        facts = self.data["random_facts"]
        self.assertGreater(len(facts), 0)

        fact = random.choice(facts)
        self.assertIn("fact", fact)
        self.assertTrue(fact["fact"])

    def test_visual_link(self):
        topic = self.menu.get_topic(self.data, 40)
        self.assertIsNotNone(topic)
        self.assertTrue(topic.visual)

if __name__ == '__main__':
    unittest.main()