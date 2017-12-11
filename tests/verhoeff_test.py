import os, sys
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import verhoeff

class TestVerhoeff(unittest.TestCase):

  def test_digit(self):
    tests = [
      ("75872", 2),
      ("12345", 1),
      ("142857", 0),
      ("123456789012", 0),
      ("8473643095483728456789", 2),
      ("xy-1", None)
    ]

    for t in tests:
      number, expected = t
      valid = verhoeff.digit(number)
      self.assertEqual(valid, expected, "verhoeff.digit?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_validate(self):
    tests = [
      ("84736430954837284567892", True),
      ("8473643095483728456789", False),
      ("xy-1", False)
    ]

    for t in tests:
      number, expected = t
      valid = verhoeff.validate(number)
      self.assertEqual(valid, expected, "verhoeff.validate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

  def test_generate(self):
    tests = [
      ("8473643095483728456789", "84736430954837284567892")
    ]

    for t in tests:
      number, expected = t
      valid = verhoeff.generate(number)
      self.assertEqual(valid, expected, "verhoeff.generate?(%(number)s) == %(valid)s, expected %(expected)s" % locals())

if __name__ == '__main__':
  unittest.main()
