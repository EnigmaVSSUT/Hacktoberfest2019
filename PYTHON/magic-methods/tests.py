import unittest

from main import V6Engine, V8Engine, Car


class InheritanceTest(unittest.TestCase):
    def test_v6_engine_car(self):
        car = Car(V6Engine())
        car.turn_on()
        self.assertEqual(car._engine.active_pistons, 6)

    def test_v8_engine_car(self):
        car = Car(V8Engine())
        car.turn_on()
        self.assertEqual(car._engine.active_pistons, 8)

    def test_magic_methods(self):
        car = Car(V8Engine())

        self.assertEqual(Car.__name__, 'Car')
        self.assertTrue(car.__class__, Car)
        self.assertEqual(repr(car), '<Car with V8 Engine>')
        self.assertEqual(str(car), 'V8 Car')

        car.transmission = 'manual'
        self.assertEqual(car.transmission, 'manual')

        with self.assertRaises(AttributeError) as context:
            car.transmission = 'anything'
        self.assertEqual(context.exception.__class__, AttributeError)
        self.assertTrue('Valid values are' in str(context.exception))


if __name__ == '__main__':
    unittest.main()