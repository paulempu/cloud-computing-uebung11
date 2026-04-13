def test_math_logic():
    # Dieser Test ist korrekt
    assert 1 + 1 == 2

def test_trigger_failure():
    # Dieser Test wird fehlschlagen, damit man den Fehler im Bericht sieht
    assert "Cloud" == "Local"
