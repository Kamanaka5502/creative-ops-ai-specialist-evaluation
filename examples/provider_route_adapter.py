"""Provider route adapter reference.

This demonstrates the boundary between an operational workflow and a provider.
It deliberately uses a dry-run adapter: no credentials, network calls, or
vendor SDKs are required in this public repository.
"""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from json import dumps
from typing import Protocol


@dataclass(frozen=True)
class ProviderRoute:
    route_id: str
    provider_family: str
    model_reference: str
    allowed_data_classification: str
    requires_prompt_lineage: bool = True
    requires_source_basis: bool = True


@dataclass(frozen=True)
class ProviderRequest:
    request_id: str
    task: str
    data_classification: str
    prompt_lineage: str
    source_basis_ids: tuple[str, ...]


@dataclass(frozen=True)
class ProviderResult:
    route_id: str
    status: str
    output: str
    observability: dict[str, object]


class Adapter(Protocol):
    def execute(self, route: ProviderRoute, request: ProviderRequest) -> ProviderResult:
        ...


class DryRunAdapter:
    """Safe stand-in for a real provider adapter."""

    def execute(self, route: ProviderRoute, request: ProviderRequest) -> ProviderResult:
        if request.data_classification != route.allowed_data_classification:
            return ProviderResult(
                route_id=route.route_id,
                status="HELD",
                output="",
                observability={"reason": "Data classification is not permitted for this route."},
            )
        if route.requires_prompt_lineage and not request.prompt_lineage:
            return ProviderResult(
                route_id=route.route_id,
                status="HELD",
                output="",
                observability={"reason": "Prompt lineage is required."},
            )
        if route.requires_source_basis and not request.source_basis_ids:
            return ProviderResult(
                route_id=route.route_id,
                status="HELD",
                output="",
                observability={"reason": "Source basis is required."},
            )
        return ProviderResult(
            route_id=route.route_id,
            status="DRY_RUN_COMPLETE",
            output="Provider call intentionally simulated. Route conditions were accepted.",
            observability={
                "timestamp": datetime.now(UTC).replace(microsecond=0).isoformat(),
                "route": asdict(route),
                "request_id": request.request_id,
                "prompt_lineage": request.prompt_lineage,
                "source_basis_count": len(request.source_basis_ids),
            },
        )


def run_demo() -> None:
    route = ProviderRoute(
        route_id="creative-evaluation-dry-run",
        provider_family="hosted_or_open_source_adapter",
        model_reference="declared-by-environment",
        allowed_data_classification="public_evaluation",
    )
    request = ProviderRequest(
        request_id="ROUTE-DEMO-001",
        task="Prepare a grounded draft for review.",
        data_classification="public_evaluation",
        prompt_lineage="launch-package@1.0",
        source_basis_ids=("product", "claims", "voice"),
    )
    print(dumps(asdict(DryRunAdapter().execute(route, request)), indent=2))


if __name__ == "__main__":
    run_demo()
