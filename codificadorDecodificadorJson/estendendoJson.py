import json
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
# Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

json.dumps(2 + 1j, cls=ComplexEncoder)
'[2.0, 1.0]'
ComplexEncoder().encode(2 + 1j)
'[2.0, 1.0]'
list(ComplexEncoder().iterencode(2 + 1j))
'[2.0', ', 1.0', ']'