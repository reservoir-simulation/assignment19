#/usr/bin/env python


import unittest

from assignment19 import BuckleyLeverett

class TestSolution(unittest.TestCase):

    def setUp(self):

        self.inputs = {
                'reservoir': { 
                    'oil': {
                        'residual saturation': 0.2,
                        'corey-brooks exponent': 3.0,
                        'max relative permeability': 0.2,
                        },
                    'water': {
                        'critical saturation': 0.2,
                        'corey-brooks exponent': 3.0,
                        'max relative permeability': 1.0,
                        },
                    },
                'fluid': {
                    'oil': {
                        'viscosity': 1.0,
                    },
                    'water': {
                        'viscosity': 1.0,
                        },
                    },
                'initial conditions': {
                    'water saturation': 0.2,
                    },
                }

    def test_water_front_saturation(self):

        bl = BuckleyLeverett(self.inputs)
                
        Swf = bl.compute_saturation_front()

        self.assertAlmostEqual(Swf, 0.49999999999970984, 7)


if __name__ == '__main__':
    unittest.main()
                        
