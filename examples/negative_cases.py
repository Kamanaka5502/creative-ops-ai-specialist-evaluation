"""Negative cases for the public operational lifecycle example.

Run:
    python3 examples/negative_cases.py
"""

from operational_lifecycle import Material, Movement, resolve


def expect_held_for_missing_basis() -> None:
    movement = Movement(
        movement_id="MOVE-EMPTY-001",
        intended_use="public_launch",
        prompt_lineage="launch-package@1.0",
        provider_route="evaluation-route/dry-run",
        active_material_ids=(),
    )
    outcome = resolve(movement, {})
    assert outcome["standing"] == "HELD"


def expect_held_for_inactive_material() -> None:
    materials = {
        "claims": Material("claims", "2026.06", "superseded", "public_launch"),
    }
    movement = Movement(
        movement_id="MOVE-INACTIVE-001",
        intended_use="public_launch",
        prompt_lineage="launch-package@1.0",
        provider_route="evaluation-route/dry-run",
        active_material_ids=("claims",),
    )
    outcome = resolve(movement, materials)
    assert outcome["standing"] == "HELD"


def expect_held_for_wrong_use() -> None:
    materials = {
        "support": Material("support", "1.0", "active", "support_response"),
    }
    movement = Movement(
        movement_id="MOVE-WRONG-USE-001",
        intended_use="public_launch",
        prompt_lineage="launch-package@1.0",
        provider_route="evaluation-route/dry-run",
        active_material_ids=("support",),
    )
    outcome = resolve(movement, materials)
    assert outcome["standing"] == "HELD"


def run() -> None:
    expect_held_for_missing_basis()
    expect_held_for_inactive_material()
    expect_held_for_wrong_use()
    print("Negative standing cases passed.")


if __name__ == "__main__":
    run()
