import unittest

from bst import BST

class TestBSTClass(unittest.TestCase):

    def test_SearchAndAddDepthOne(self):
        bst = BST()
        bst.add(2)
        self.assertEqual(2, bst.search(2).data)

        bst.add(3)
        self.assertEqual(3, bst.search(3).data)

        bst.add(1)
        self.assertEqual(1, bst.search(1).data)

    def test_SearchAndAddDepthTwo(self):
        bst = BST()
        bst.add(10)
        bst.add(15)
        bst.add(5)
        bst.add(3)
        bst.add(7)
        bst.add(13)
        bst.add(17)

        self.assertEqual(3, bst.search(3).data)
        self.assertEqual(7, bst.search(7).data)
        self.assertEqual(13, bst.search(13).data)
        self.assertEqual(17, bst.search(17).data)


if __name__ is '__main__':
    unittest.main()
