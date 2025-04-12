import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        test_1 = emotion_detector("I am glad this happened")
        test_2 = emotion_detector("I am really mad about this")
        test_3 = emotion_detector("I feel disgusted just hearing about this")
        test_4 = emotion_detector("I am so sad about this")
        test_5 = emotion_detector("I am really afraid that this will happen")

        self.assertEqual(test_1["dominant_emotion"],"joy")
        self.assertEqual(test_2["dominant_emotion"],"anger")
        self.assertEqual(test_3["dominant_emotion"],"disgust")
        self.assertEqual(test_4["dominant_emotion"],"sadness")
        self.assertEqual(test_5["dominant_emotion"],"fear")

unittest.main()
