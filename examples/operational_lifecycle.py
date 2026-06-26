"""Public operational standing lifecycle example.

Run:
    python3 examples/operational_lifecycle.py

No external models, keys, network calls, or private data are used.
"""

from dataclasses import asdict, dataclass
from hashlib import sha256
from json import dumps


@dataclass(frozen=True)
class Material:
    material_id: str
    version: str
    status: str
    allowed_use: str


@dataclass(frozen=True)
class Movement:
    movement_id: str
    intended_use: str
    prompt_lineage: str
    provider_route: str
    active_material_ids: tuple[str, ...]


def witness_id(movement: Movement, basis: list[Material]) -> str:
    payload = {
        "movement": asdict(movement),
        "basis": [asdict(item) for item in basis],
    }
    digest = sha256(dumps(payload, sort_keys=True).encode()).hexdigest()[:16].upper()
    return f"WIT-{digest}"


def resolve(movement: Movement, material_map: dict[str, Material]) -> dict[str, object]:
    basis = [material_map[item_id] for item_id in movement.active_material_ids if item_id in material_map]
    if not basis:
        return {"standing": "HELD", "reason": "No active material basis."}
    if any(item.status != "active" for item in basis):
        return {"standing": "HELD", "reason": "Inactive material is present."}
    if any(item.allowed_use != movement.intended_use for item in basis):
        return {"standing": "HELD", "reason": "Material basis does not authorize the intended use."}
    return {
        "standing": "MAY_BIND",
        "reason": "Active basis, lineage, and provider route are declared.",
        "witness_id": witness_id(movement, basis),
        "snapshot": [asdict(item) for item in basis],
    }


def revalidate(snapshot: list[dict[str, str]], material_map: dict[str, Material]) -> dict[str, object]:
    changed = []
    for previous in snapshot:
        current = material_map.get(previous["material_id"])
        if current is None or asdict(current) != previous:
            changed.append(previous["material_id"])
    if changed:
        return {
            "standing": "REVALIDATION_REQUIRED",
            "reason": "Material drift changes the active field.",
            "changed_material_ids": changed,
        }
    return {"standing": "BOUND_REVIEWED", "reason": "Witnessed basis remains current."}


def run_demo() -> None:
    materials = {
        "product": Material("product", "1.0", "active", "public_launch"),
        "claims": Material("claims", "2026.06", "active", "public_launch"),
        "voice": Material("voice", "1.4", "active", "public_launch"),
    }
    movement = Movement(
        movement_id="MOVE-LAUNCH-001",
        intended_use="public_launch",
        prompt_lineage="launch-package@1.0",
        provider_route="evaluation-route/dry-run",
        active_material_ids=("product", "claims", "voice"),
    )

    first = resolve(movement, materials)
    print("RESOLUTION")
    print(dumps(first, indent=2))

    if first["standing"] == "MAY_BIND":
        print("\nREVIEWED STANDING")
        print(dumps({"standing": "BOUND_REVIEWED", "reviewer": "named reviewer"}, indent=2))

        materials["claims"] = Material("claims", "2026.07", "active", "public_launch")
        drift = revalidate(first["snapshot"], materials)
        print("\nAFTER MATERIAL DRIFT")
        print(dumps(drift, indent=2))


if __name__ == "__main__":
    run_demo()
