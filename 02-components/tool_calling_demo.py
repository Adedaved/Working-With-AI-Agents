"""A deterministic tool-runtime demo. No LLM is called and no agent is deployed."""
from decimal import Decimal, InvalidOperation
import json


def add(a: Decimal, b: Decimal) -> Decimal:
    return a + b


TOOLS = {'add': add}


def dispatch(request: dict) -> str:
    if not isinstance(request, dict) or set(request) != {'name', 'arguments'}:
        raise ValueError('Expected exactly name and arguments')
    name = request['name']
    if not isinstance(name, str) or name not in TOOLS:
        raise ValueError('Tool is not allowed')
    arguments = request['arguments']
    if not isinstance(arguments, dict) or set(arguments) != {'a', 'b'}:
        raise ValueError('Expected exactly a and b')
    if not all(isinstance(arguments[k], str) for k in ('a', 'b')):
        raise ValueError('Arguments must be decimal strings')
    try:
        a, b = Decimal(arguments['a']), Decimal(arguments['b'])
    except InvalidOperation as exc:
        raise ValueError('Invalid decimal') from exc
    if not a.is_finite() or not b.is_finite():
        raise ValueError('Arguments must be finite')
    return str(TOOLS[name](a, b))


if __name__ == '__main__':
    simulated_model_request = {'name': 'add', 'arguments': {'a': '18', 'b': '24'}}
    print('SIMULATION: the request below is supplied by this script, not by an LLM.')
    print(json.dumps(simulated_model_request))
    print(dispatch(simulated_model_request))
