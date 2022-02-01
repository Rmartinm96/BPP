import pytest
import ACTIVIDAD1

def test_recorrido():
    assert ACTIVIDAD1.recorrido_tabla()

def test_gasto_mes():
    assert ACTIVIDAD1.mes_gasto() == 'Abril'

def test_ahorro_mes():
    assert ACTIVIDAD1.mes_ahorro() == 'Enero'

def test_media_gastos():
    assert ACTIVIDAD1.media_gastos() == 24732.583333333332

def test_gasto_total():
    assert ACTIVIDAD1.gasto_total() == 296791

def test_ingreso_total():
    assert ACTIVIDAD1.ingreso_total() == 280961

def test_grafica():
    assert ACTIVIDAD1.grafica() == "GRÁFICA DE BARRAS REALIZADA CORRECTAMENTE"

def test_lectura_fichero():
    assert ACTIVIDAD1.lectura_fichero() == 'APERTURA LECTURA Y CIERRE CORRECTOS'