import Challenge
open BipartiteRadiusThreeMatchingCut
example : boundedCut ⟨3, [(0,1),(1,2)]⟩ 1 [false,true,true] = true := by native_decide
example : boundedCut ⟨3, [(0,1),(1,2)]⟩ 1 [false,true,false] = false := by native_decide
