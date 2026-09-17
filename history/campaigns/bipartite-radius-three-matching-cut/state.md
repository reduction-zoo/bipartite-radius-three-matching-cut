# Bipartite radius-three Matching Cut

Status: ready_for_expert_review. Allocation: 40 rounds; 1 started and completed,
39 unused. Topic-selection probes were separately recorded before the campaign.

[Algorithm](work/algorithm.py) and [general proof](work/proof.md): a deterministic
Karp reduction from bipartite radius-four Matching Cut to radius three, including
polynomial recovery from every valid target witness. Output order and edge count
are O(n^3). The theorem would settle the cited bipartite radius boundary.

| Round | Result |
|---|---|
| [001](rounds/001/round.md) | One full construction; checks and independent review passed; inspected paper complete |

Checks: eight prepared cases/20 recoveries; eighteen additional cases/56
recoveries; reviewer three full cases/four recoveries plus local and adversarial
checks. Families overlap. [Verification](work/verification.md) gives commands
and raw-evidence links. One interrupted arithmetic solver run is excluded from
passing evidence; one checker encoding change and repeated self-test preceded
the completed run. Zero candidate algorithm repairs, no timeout.

The [independent review](reviews/complete-rule/review.md) advanced without repair.
The [seven-page paper](work/manuscript.pdf), [Typst source](work/manuscript.typ)
and [page-inspection record](work/evidence/paper-inspection.txt) are complete.
No mathematical or executable changes occurred after review.

Novelty is supported within the dated primary-literature coverage, not certified
by search failure. Significance: the radius-two/three complexity boundary.
No unresolved agent-side correctness gap is known. Human expert assessment of
correctness, novelty and significance remains necessary; its outcome is unknown.
Stop discovery here without using the remaining allocation to pad rounds.

Post-campaign experience closeout: **1 new entry, 1 existing entry updated,
0 pending**; collection total **8 entries** (excluding README).
[New interface finding](../../research/experience/dual-reservoir-matching-cut-interfaces.md);
[updated selector use history](../../research/experience/three-mate-choices-at-radius-three.md).
