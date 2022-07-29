from vehiculos import Vehiculo, Coche, Bicicleta, Camioneta, Motocicleta

def test_vehiculo():
    v = Vehiculo('Rosa', 4)
    assert v.__str__() == 'Color Rosa, 4 Ruedas'


def test_coche():
    v = Coche('Rosa', 4, 45, 4)
    assert v.__str__() == 'Color Rosa, 4 Ruedas, 45 km/h, 4 cc'


def test_bicicleta():
    v = Bicicleta('Rosa', 'Urbana')
    assert v.__str__() == 'Color Rosa, 2 Ruedas, tipo Urbana'


def test_camioneta():
    v = Camioneta('Rosa', 4, 50, 8, 50)
    assert v.__str__() == 'Color Rosa, 4 Ruedas, 50 km/h, 8 cc, carga 8 kg'


def test_motocicleta():
    v = Motocicleta('Rosa', 'Urbana', 50, 8)
    assert v.__str__() == 'Color Rosa, 2 Ruedas, tipo Urbana, 50 km/h, 8 cc'


def test_subclass_coche_vehiculo():
    assert issubclass(Coche, Vehiculo)


def test_subclass_bicicleta_vehiculo():
    assert issubclass(Bicicleta, Vehiculo)


def test_subclass_camioneta_coche():
    assert issubclass(Camioneta, Coche)


def test_subclass_motocicleta_bicicleta():
    assert issubclass(Motocicleta, Bicicleta)


def test_subclass_camioneta_vehiculo():
    assert issubclass(Camioneta, Vehiculo)


def test_subclass_motocicleta_vehiculo():
    assert issubclass(Motocicleta, Vehiculo)
