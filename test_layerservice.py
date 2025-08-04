# test_layerservice.py
"""
Tests for LayerService module.
"""

import unittest
from layerservice import LayerService

class TestLayerService(unittest.TestCase):
    """Test cases for LayerService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LayerService()
        self.assertIsInstance(instance, LayerService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LayerService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
