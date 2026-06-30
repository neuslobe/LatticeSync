# test_latticesync.py
"""
Tests for LatticeSync module.
"""

import unittest
from latticesync import LatticeSync

class TestLatticeSync(unittest.TestCase):
    """Test cases for LatticeSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LatticeSync()
        self.assertIsInstance(instance, LatticeSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LatticeSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
