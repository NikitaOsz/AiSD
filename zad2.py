from typing import Any


class Node:
    value: Any
    next: 'Node'


class LinkedList:
    head: Node
    tail: Node

    def push(self, value: Any) -> None:
        pass

    def append(self, value: Any) -> None:
        pass

    def node(self, at: int) -> Node:
        pass

    def insert(self, value: Any, after: Node) -> None:
        pass

    def pop(self) -> Any:
        pass

    def remove_last(self) -> Any:
        pass

    def remove(self, after: Node) -> Any:
        pass

    