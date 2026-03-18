from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Iterable


@dataclass(slots=True)
class TestCase:
    """Represents one executable test case for a LeetCode problem."""

    name: str
    input: dict[str, Any]
    expected: Any
    method: str = "solve"
    normalizer: Callable[[Any], Any] | None = None
    description: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


class CaseNotFoundError(LookupError):
    """Raised when a requested test case name does not exist."""


class SolutionExecutionError(RuntimeError):
    """Raised when a solution method cannot be executed."""


def instantiate_solution(solution_cls: type[Any]) -> Any:
    return solution_cls()


def execute_case(solution_cls: type[Any], case: TestCase) -> Any:
    solution = instantiate_solution(solution_cls)
    try:
        method = getattr(solution, case.method)
    except AttributeError as exc:
        raise SolutionExecutionError(
            f"{solution_cls.__name__} is missing method '{case.method}'"
        ) from exc

    result = method(**case.input)
    return case.normalizer(result) if case.normalizer else result


def assert_case(solution_cls: type[Any], case: TestCase) -> None:
    actual = execute_case(solution_cls, case)
    expected = case.normalizer(case.expected) if case.normalizer else case.expected
    assert actual == expected, (
        f"Case '{case.name}' failed: expected {expected!r}, got {actual!r}. "
        f"Input={case.input!r}"
    )


def get_case(cases: Iterable[TestCase], name: str) -> TestCase:
    for case in cases:
        if case.name == name:
            return case
    raise CaseNotFoundError(f"Unknown case '{name}'")
