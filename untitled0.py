# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 13:40:06 2019

@author: M
"""

import unittest

class TestDemo(unittest.TestCase):
    
    def test_1(self):
        self.assertEqual('foo'.upper(),'FOO')
        
    def test_2(self):
        self.assertTrue('FOO'.isupper(),'测试失败！！')
        self.assertFalse('Foo'.isupper())
        
    def test_3(self):
        s = 'hello world'
        self.assertEqual(s.split(),['hello','world'])
        self.fail("这都是啥呀")
        with self.assertRaises(TypeError):
            s.split(2)
            
if __name__ == '__main__':
    unittest.main()