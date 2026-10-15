---
status: ready-for-attempt
openness: supported-within-search-coverage
difficulty: moderate
importance: moderate
tags: [graph-cuts, NP-hardness, bipartite, radius]
last-literature-check: 2026-09-15
---

# Bipartite radius-four Matching Cut → radius-three Matching Cut

[Board](../../research/open-problems/README.md) · [Karp contract](../../research/open-problems/README.md#shared-karp-contract)

| Assessment | Evidence |
|---|---|
| Difficulty | Moderate, provisional: dual reservoirs and local interfaces pass; full composition and proof remain |
| Importance | Moderate: settle the bipartite radius threshold |
| Proof readiness | Pass for a bounded campaign after the new interface probe |

**Exact target.** Preserve existence of a nontrivial cut with crossing degree
at most one, while ensuring output bipartiteness and radius at most three.
No perfect-matching or objective-size condition is imposed.

**Evidence.** R3, Table 1 and Section 5, Open Problem 1, records hardness at
radius four and leaves radius three open. Radius two is polynomial. The question
also appears in R4's concluding Open Problem 1.

**Route.** Add a bounded-distance communication structure that transmits variable
colors without consuming their only crossing edge. The natural two-hub construction
adds a new vertex adjacent to each side of the bipartition and an edge between hubs.

**Executed failure.** Exhausted 27 connected bipartite atlas inputs through six
vertices. On P3 with edges {01,02}, the original is YES and the augmented graph
is NO. Every tested augmentation is bipartite with diameter at most three, so
the metric shortcut is valid but the Karp equivalence fails. A local transmission
gadget must overcome that defect. Its existence is not yet supported: Gate 6 hold.

## Primary sources

- **R3.** Lucke,
  [Matching Cut and Variants on Bipartite Graphs of Bounded Radius and Diameter](https://arxiv.org/html/2501.08735),
  arXiv:2501.08735v1, 15 January 2025, Table 1, Theorems 18–19,
  Corollary 17, Section 5, Open Problems 1–2.
- **R4.** Lucke, Paulusma, Ries,
  [On the complexity of Matching Cut for graphs of bounded radius and H-free graphs](https://durham-repository.worktribe.com/OutputFile/1188745),
  TCS 936 (2022), 33–42, concluding Open Problem 1.

## Research history

- [Recorded probe](../../research/evidence/cut-and-augmentation-probes.py). Finite checks do not prove a reduction.

- 2026-09-14: Web and arXiv update queries: `"Disconnected Perfect Matching" "radius 3" bipartite`; `"Perfect Matching Cut" "diameter" "open" 2026`; `"Matching Cut" "radius 3" 2026 bipartite`.
  No exact resolution was located within this search; unpublished, unindexed,
  and overlooked results remain outside the supported openness claim.

- 2026-09-15, new route: replace bare hubs by two disjoint K3,3 reservoirs joined
  by one edge. Under Matching Cut each reservoir is monochromatic. Attach every
  fixed-color vertex to two vertices of its reservoir; this enforces its color.
  A binary block and the previous selector topology then encode a bit and an
  exact-one triple when reservoir colors differ. When their colors agree, all
  private vertices are forced to agree, excluding local nontriviality. All vertices
  remain within three steps of the first reservoir's distinguished vertex.
  The earlier bare-hub counterexample is not reused: its forcing mechanism changed.
  [Executed probe](../../research/evidence/bipartite-radius-three-matching-cut/interface.py)
  and [results](../../research/evidence/bipartite-radius-three-matching-cut/results.json)
  cover four compositions with zero to two binary/selector blocks. All intended
  pinned extensions are SAT; bad local relations and nonconstant same-center
  assignments are UNSAT. These are finite evidence, not the full reduction.
  Existing exact-one PMC lemmas were used as design leads only: the new predicate
  is at most one, and its premises were checked afresh.
  Queries `"Matching Cut" "radius three" bipartite 2026` and
  `"Matching Cut" "radius 3" 2026 bipartite`; read R3 Table 1 and Section 5,
  Open Problem 1, at https://arxiv.org/html/2501.08735. No later exact resolution
  was found within coverage; unindexed and overlooked work remains possible.

## Current screening and handoff

All six gates pass provisionally: fixed Karp endpoints; the cited radius-four
hardness and radius-two tractability do not cover three; openness is supported
within the dated primary coverage; the result would close the bipartite radius
boundary; there is a concrete two-reservoir route; and the local experiment
supports that route. Difficulty is moderate provisionally, importance moderate.

The source consists of connected simple bipartite graphs of radius at most four
with a nontrivial matching cut; the target uses radius at most three and the same
cut predicate. Each map includes polynomial recovery from every target witness.
Encode source neighbor-pair restrictions and nontriviality as CNF, convert to
signed exact-one triples, then attach the validated interfaces. Recovery reads
one binary port per source vertex relative to the first reservoir's color.
The remaining work is full composition, total encoding, universal recovery and
polynomial bounds. The user authorized an initial 40-round campaign, stopping
without padding if a complete result is reached.
