from bukuserver import _key


def test_key_with_lazy_string_like_object():
    class FakeLazyString:
        _args = ('cached-key',)
    assert _key(FakeLazyString()) == 'cached-key'


def test_key_fallback_without_args_attribute():
    # objetos sem o atributo _args devem cair no except e retornar str(s)
    assert _key('plain-string') == 'plain-string'
    assert _key(123) == '123'
