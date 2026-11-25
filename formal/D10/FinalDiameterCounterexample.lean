import ConcreteTreeCounterexampleFamily
import StarModelDiameter

/-! A final wrapper joining unchanged ordinary-game lower bounds with the
independently accepted exact diameter theorem on the same original graph.
This module asserts only lower bounds on game values. -/
namespace CounterexampleConcreteFinal
open CounterexampleStarSpine IsolationGame

/-- The literal Fin 13-leaf model is a 210-vertex diameter-ten tree and exceeds
the ceiling bound for either ordinary empty-history starting player. -/
theorem fourteenModel_complete_counterexample :
    fourteenModel.IsTree ∧ Fintype.card FourteenModelVertex = 210 ∧
      fourteenModel.diam = 10 ∧
      91 ≤ IsolationGame.gameValue fourteenModel .dominator ∅ ∧
      91 ≤ IsolationGame.gameValue fourteenModel .staller ∅ ∧
      (3 * Fintype.card FourteenModelVertex + 6) / 7 = 90 ∧
      (∀ p : Player, (3 * Fintype.card FourteenModelVertex + 6) / 7 <
        IsolationGame.gameValue fourteenModel p ∅) ∧
      (∀ p : Player, 3 * Fintype.card FourteenModelVertex <
        7 * IsolationGame.gameValue fourteenModel p ∅) :=
  ⟨fourteenModel_tree, fourteenModel_card,
    CounterexampleStarDiameter.fourteenModel_diam_eq_ten,
    fourteenModel_d_lower, fourteenModel_s_lower,
    fourteenModel_ceil_three_sevenths, fourteenModel_ordinary_exceeds_ceil,
    fourteenModel_scaled_violation⟩

/-- Every positive scale uses the existing literal star graph, with no new
graph construction, deletion, or identification of vertices. -/
theorem model_complete_counterexample (k : Nat) (hk : 1 ≤ k) :
    (model k).IsTree ∧ Fintype.card (ModelVertex k) = 210 * k ∧
      (model k).diam = 10 ∧
      91 * k ≤ IsolationGame.gameValue (model k) .dominator ∅ ∧
      91 * k ≤ IsolationGame.gameValue (model k) .staller ∅ ∧
      (3 * Fintype.card (ModelVertex k) + 6) / 7 = 90 * k ∧
      (∀ p : Player, (3 * Fintype.card (ModelVertex k) + 6) / 7 <
        IsolationGame.gameValue (model k) p ∅) ∧
      (∀ p : Player, 3 * Fintype.card (ModelVertex k) <
        7 * IsolationGame.gameValue (model k) p ∅) :=
  ⟨model_tree k, model_card k hk,
    CounterexampleStarDiameter.model_diam_eq_ten k hk,
    model_ordinary_lower k hk .dominator, model_ordinary_lower k hk .staller,
    model_ceil_three_sevenths k hk, model_ordinary_exceeds_ceil k hk,
    model_scaled_violation k hk⟩

#print axioms CounterexampleConcreteFinal.fourteenModel_complete_counterexample
#print axioms CounterexampleConcreteFinal.model_complete_counterexample
end CounterexampleConcreteFinal
