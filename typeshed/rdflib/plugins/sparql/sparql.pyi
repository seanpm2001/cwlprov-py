import datetime
from rdflib import BNode as BNode, ConjunctiveGraph as ConjunctiveGraph, Graph as Graph, Literal as Literal, URIRef as URIRef, Variable as Variable
from rdflib.compat import Mapping as Mapping, MutableMapping as MutableMapping
from rdflib.namespace import NamespaceManager as NamespaceManager
from rdflib.plugins.sparql.parserutils import CompValue as CompValue
from rdflib.term import Node as Node
from typing import Any

class SPARQLError(Exception):
    def __init__(self, msg: Any | None = ...) -> None: ...

class NotBoundError(SPARQLError):
    def __init__(self, msg: Any | None = ...) -> None: ...

class AlreadyBound(SPARQLError):
    def __init__(self) -> None: ...

class SPARQLTypeError(SPARQLError):
    def __init__(self, msg) -> None: ...

class Bindings(MutableMapping):
    outer: Any
    def __init__(self, outer: Any | None = ..., d=...) -> None: ...
    def __getitem__(self, key): ...
    def __contains__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self): ...

class FrozenDict(Mapping):
    def __init__(self, *args, **kwargs) -> None: ...
    def __iter__(self): ...
    def __len__(self): ...
    def __getitem__(self, key): ...
    def __hash__(self): ...
    def project(self, vars): ...
    def disjointDomain(self, other): ...
    def compatible(self, other): ...
    def merge(self, other): ...

class FrozenBindings(FrozenDict):
    ctx: Any
    def __init__(self, ctx, *args, **kwargs) -> None: ...
    def __getitem__(self, key): ...
    def project(self, vars): ...
    def merge(self, other): ...
    @property
    def now(self): ...
    @property
    def bnodes(self): ...
    @property
    def prologue(self): ...
    def forget(self, before, _except: Any | None = ...): ...
    def remember(self, these): ...

class QueryContext:
    initBindings: Any
    bindings: Any
    graph: Any
    prologue: Any
    bnodes: Any
    def __init__(self, graph: Any | None = ..., bindings: Any | None = ..., initBindings: Any | None = ...) -> None: ...
    @property
    def now(self) -> datetime.datetime: ...
    def clone(self, bindings: Any | None = ...): ...
    @property
    def dataset(self): ...
    def load(self, source, default: bool = ..., **kwargs): ...
    def __getitem__(self, key): ...
    def get(self, key, default: Any | None = ...): ...
    def solution(self, vars: Any | None = ...): ...
    def __setitem__(self, key, value) -> None: ...
    def pushGraph(self, graph): ...
    def push(self): ...
    def clean(self): ...
    def thaw(self, frozenbindings): ...

class Prologue:
    base: Any
    namespace_manager: Any
    def __init__(self) -> None: ...
    def resolvePName(self, prefix, localname): ...
    def bind(self, prefix, uri) -> None: ...
    def absolutize(self, iri): ...

class Query:
    prologue: Any
    algebra: Any
    def __init__(self, prologue, algebra) -> None: ...