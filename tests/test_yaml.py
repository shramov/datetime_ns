#!/usr/bin/env python3
# vim: sts=4 sw=4 et

import datetime_ns
datetime_ns.datetime_patch()

import datetime_ns.yaml
datetime_ns.yaml.yaml_patch()

import yaml
import datetime
import unittest

class Test(unittest.TestCase):
    def test(self):
        data = {'d': datetime.datetime(2020, 1, 2, 3, 4, 5, nanosecond=123456)}
        s = yaml.dump(data)
        self.assertEqual(s, 'd: 2020-01-02 03:04:05.000123456\n')
        d = yaml.safe_load(s)
        self.assertEqual(d['d'].nanosecond, 123456)
        self.assertEqual(d, data)

if __name__ == "__main__":
    unittest.main()
