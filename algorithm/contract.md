# Fixed encoding

A graph is a JSON object with exactly `n` and `edges`, on vertices 0,...,n-1.
Each edge is a distinct list [u,v] with integer 0 <= u < v < n. Graphs are simple,
connected and bipartite, n >= 1. Source radius is at most four; target radius is
at most three. Invalid strings are outside their respective languages.

A witness for either language is a nonconstant list of n integer bits, with
at most one opposite-colored neighbor per vertex. There is no perfect-matching
requirement. Target graph vertex order defines target witness order.

`python3 algorithm.py` maps source JSON to target JSON; every legal source,
including NO sources, must yield a structurally legal target. Invalid sources
may map to `{}`, outside the target language. `python3 algorithm.py --extract`
reads `{"source":...,"target_solution":...}` and emits a source witness for
every valid witness of the actual constructed output. Both modes run in fresh
processes without solvers, randomness or saved state, in deterministic polynomial
time and with polynomial output bit length. Diagnostics use stderr; execution
errors are nonzero. General proofs are required beyond finite injected tests.
