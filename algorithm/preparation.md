# Independent testing foundation

The prepared checker uses Z3 5.1.0 with one Boolean per graph vertex, nonconstant
coloring and the native PbLe at-most-one constraint on each neighborhood. Source and target have the
same witness predicate and different radius domains. NetworkX checks simplicity,
connectivity, bipartiteness and radius. Every solver witness is recounted directly;
only UNSAT means NO. Unknown fails explicitly. No timeout is used.

The existing direct harness from the line-graph campaign was adapted to these
fixed graph languages, not imported from a candidate. `--self-test` compares all
witnesses against brute force on connected bipartite atlas graphs through five
vertices, validates eight stored source cases, and rejects deliberately malformed,
decision-mismatching and incorrectly recovering programs. Evidence:
[evidence/preparation/self-test.json](../history/campaigns/bipartite-radius-three-matching-cut/work/evidence/preparation/self-test.json).

Reproduce from repository root:
`python3 campaigns/bipartite-radius-three-matching-cut/work/check.py --self-test`.
The eight cases include the earlier bare-hub counterexample P3, source radius
four, YES/NO graphs, a singleton and cube. `--candidate PATH` will execute actual
outputs and test up to four distinct target witnesses per YES case in fresh
extractor subprocesses. The completed candidate passed this harness; see [verification](verification.md).
Arbitrary-size correctness and universal recovery are separate proof obligations.

## Encoding update during round 001

The initial arithmetic form used sums of integer-valued If terms. The first full
candidate suite was manually interrupted inside Z3 search, returned unknown,
and produced no completed suite result. It is not counted as a candidate failure
or as NO. See [diagnosis](../history/campaigns/bipartite-radius-three-matching-cut/rounds/001/arithmetic-interruption.txt) and preserved
checker. The direct Boolean cardinality form expresses the identical predicate.
The re-established self-test again passed all 11 source and 11 target graphs,
eight cases and three bad programs; see
[cardinality-self-test.json](../history/campaigns/bipartite-radius-three-matching-cut/rounds/001/cardinality-self-test.json).
This is one testing-encoding change, not another research round or a timeout.
