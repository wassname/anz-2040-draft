# Probability provenance

This file separates AI 2040's estimates from our arithmetic and our ANZ-specific assumptions. It documents the current tree; it does not endorse every modelling choice in it.

## Short answer on "great future"

The formal 42% appears in one AI 2040 supplement, [Comparing Possible Plans](https://ai-2040.com/supplements/comparing-possible-plans). I found no explicit definition of "great future" beside its probability table.

The wider scenario uses global language, but its concrete treatment of middle powers focuses on joining the deal, access to AI, shares of compute and robot production, and material benefits. I found no condition that foreign middle powers remain democratic. The published material therefore leaves unresolved whether the 42% metric permits domestic autocracy in a materially prosperous client state.

## AI 2040 probabilities

These are conditional on a median Plan A implementation in Eli Lifland's plan-comparison table. They are not the probability that Plan A happens.

| Quantity | AI 2040 | Status | Calculation |
|---|---:|---|---|
| Humans avoid misaligned AI takeover | 72% | quoted | p(alignment) in the supplement |
| Misaligned AI takeover | 28% | derived | 100% - 72% |
| Great future, conditional on alignment | 58% | quoted | p(great future given alignment) |
| Great future | 42% | quoted, rounded | 72% x 58% = 41.76%, shown as 42% |
| Alignment without a great future | 30% | derived residual | 72% - 42% |

### Underlying Plan A calculation

The [linked calculation sheet](https://docs.google.com/spreadsheets/d/1FDyYPky6VeIs81ujssgQKyv-yIZc8iOZQrZv6KlJCNk/edit?gid=24026390#gid=24026390) decomposes Plan A into three end states, then applies competence adjustments:

| Sheet column | p(happens given initial competence) | p(alignment) | p(great future given alignment) | p(great future) |
|---|---:|---:|---:|---:|
| 2040 handoff | 49% | 92% | 67% | 62% |
| Stage 1 deal decline | 40% | 55% | 52% | 29% |
| Stage 2 deal decline | 11% | 75% | 60% | 45% |
| Plan A expected value | 100% | 75% | 60% | 47% |
| Adjusted up for better strategies | - | 80% | 62% | 50% |
| Final adjustment down for lower competence | - | 72% | 58% | 42% |

The sheet averages the alignment and conditional-great-future rows across end states separately, while the great-future row aggregates each branch's joint outcome. Therefore the displayed Plan A expected-value row is not reconstructed by multiplying 75% by 60%.

The sheet contains no term for democracy within foreign middle powers. It does not establish whether that consideration is intentionally excluded or merely left implicit.

The three unconditional outcome buckets used by our tree are:

| AI 2040 bucket | Probability |
|---|---:|
| Misaligned takeover | 28% |
| Aligned, but not a great future | 30% |
| Great future | 42% |
| **Total** | **100%** |

## Our additions

| Quantity | Our value | Conditional on | Absolute probability in the current tree | Status |
|---|---:|---|---:|---|
| AI progress plateaus first | about 35% | the whole forecast | excluded from the Plan A denominator | our rough estimate, currently unlabelled in the SVG |
| Homegrown ANZ autocracy | 30% | AI 2040's 42% positive outcome | 12.6% | our estimate: 42% x 30% |
| ANZ remains democratic | 70% | AI 2040's 42% positive outcome | 29.4% | complement: 42% x 70% |
| Later ANZ policy choices | no probabilities assigned | democratic ANZ path | n/a | drawn with uniform-width choice edges |

The current tree therefore preserves AI 2040's 28% + 30% + 42% = 100%, then subdivides the 42% branch using our 30% / 70% estimate.

## The unresolved semantic question

Our tree currently reads the 30% estimate as:

$$p(\text{ANZ autocracy} \mid \text{AI 2040 great future}) = 30\%$$

The supplement's expanded cells operationalize distribution of power through frontier companies and countries, and discuss extreme concentration of decisive AI power. They do not score democracy within each foreign state, but this omission does not tell us whether foreign democracy is implicit in "great future." There are three possible interpretations:

1. **Literal subset.** A future can count as great in AI 2040 while ANZ becomes autocratic. This preserves the current tree, but is an assumption rather than a sourced definition.
2. **Our downward adjustment.** We think AI 2040 omitted an ANZ failure mode, so we reclassify 30% of its 42% branch. The arithmetic remains 12.6%, but the diagram should call it our adjustment rather than an event occurring inside a great future.
3. **A different denominator.** Our 30% means autocracy conditional on human control, or on some other category. This requires new arithmetic and should not be changed without deciding the denominator first.

The existing SVG implements interpretation 1. The source does not establish whether interpretation 1 or 2 is correct.

## Our ANZ table

This table documents the current model. It is conditional on rapid AI progress and Plan A being attempted.

| Our mutually exclusive outcome | Probability | Relationship to AI 2040 |
|---|---:|---|
| Misaligned AI takeover | 28.0% | unchanged |
| Aligned, but not a great future by AI 2040's metric | 30.0% | unchanged residual |
| AI 2040-positive future with homegrown ANZ autocracy | 12.6% | our refinement: 30% of AI 2040's 42% branch |
| AI 2040-positive future with democratic ANZ | 29.4% | remainder: 70% of AI 2040's 42% branch |
| **Total** | **100.0%** | |

This table says that our autocracy estimate adds an ANZ political dimension that AI 2040 does not model:

$$
p_{\text{ours}}(\text{ANZ autocracy}) = 0.42 \times 0.30 = 0.126
$$

$$
p_{\text{ours}}(\text{AI 2040-positive and democratic ANZ}) = 0.42 \times 0.70 = 0.294
$$

The key assumption is that AI 2040's "great future" metric does not require each foreign middle power to remain democratic. The expanded cells do not test or state that assumption.

## Source evidence

### Comparing Possible Plans - Eli Lifland - [AI 2040 supplement](https://ai-2040.com/supplements/comparing-possible-plans)

> In this supplement I'll estimate how well each plan does on various intermediate metrics, and its chance of leading to a great future. I discuss quantitative metrics for the sake of concreteness, however I'm very much not confident in my precise estimates.

Epistemic context: this is the author of the probability table describing his own estimates and confidence.

> Outcomes (medians across implementations)  
> p(alignment); i.e., 1 - p(misaligned takeover) | 72%  
> p(great future | alignment) | 58%  
> p(great future) | 42%

Epistemic context: the Markdown mirror flattens an interactive table; these are the Plan A values in its first numeric column.

The live expanded cells add:

> Plan A has power distributed across many frontier companies in many countries. This seems fairly robust to poor implementations, depending on exactly how far you allow a departure from Plan A before considering it as an implementation.

Epistemic context: this is the expanded explanation for Plan A's 5/5 "Distribution of power" score.

> P(extreme COP | alignment) in Plan C is 25%, as opposed to 35% in Plan D, because Plan C gives actors more of a chance to wake up and prevent extreme COP, without having a classified govt project. This alone leads to less than a 10% difference in overall p(great future | alignment) though because whether there's extreme COP doesn't exactly correspond to whether there is a great future. But there's also various other stuff that the extra time helps for, like using AI to help with epistemics, and decision theory, and figuring out space governance.

Epistemic context: this is the expanded Plan C reasoning for "great future given alignment"; COP means concentration of power.

> p(great future) is not entered directly. For each plan it is computed as p(alignment) x p(great future | alignment) - the two rows above.

Epistemic context: this expanded note specifies the arithmetic behind the 42%.

### Plan A great-future calculation - [Google Sheet](https://docs.google.com/spreadsheets/d/1FDyYPky6VeIs81ujssgQKyv-yIZc8iOZQrZv6KlJCNk/edit?gid=24026390#gid=24026390)

> p(happens | initially competent) [...] 2040 handoff 49%, Stage 1 deal decline 40%, Stage 2 deal decline 11%  
> p(align) [...] 92%, 55%, 75% [...] 72%  
> p(gf | align) [...] 67%, 52%, 60% [...] 58%  
> p(gf) [...] 62%, 29%, 45% [...] 42%

Epistemic context: this is the public calculation tab linked from the expanded Plan A cell; values were read from its CSV export on 2026-07-12.

### AI 2040: Plan A - AI Futures Project - [main scenario](https://ai-2040.com/?choices=plan-a-root)

> Plan A is our positive vision for how humanity can avoid AI-driven existential catastrophe and reach a flourishing future.

Epistemic context: the project authors introduce the intended scope of Plan A in the main scenario, not the probability supplement.

> First, our goal was to construct a positive vision, a grand plan for how to achieve an actually good future for everyone.

Epistemic context: the epilogue authors explain why they extended the scenario beyond 2040.

> Our best guess is that if the world manages to get to a point similar to this part of the story [...] and also put transparency and governance structures in place to prevent people from being disempowered - then, in that situation, the benefits of superintelligence will outweigh the costs/risks.

Epistemic context: the PDF's handoff appendix describes the conditions for the depicted positive outcome; the omitted middle lists multi-country safety work and resources for everyone.

## Epistemic summary

- **Who supplied the numbers:** the 72%, 58%, and 42% are Eli Lifland's rough Plan A estimates in one supplement. The 28% and 30% buckets are arithmetic derived from them.
- **Who supplied the ANZ split:** the 30% autocracy estimate and its 12.6% path are ours, not AI 2040's.
- **Entanglement:** all quoted evidence comes from the same AI 2040 project. The main scenario gives interpretive context, not independent confirmation of the supplement's metric definition.
- **What the source covers:** foreign states receive AI access, compute and robot shares, and income. The expanded cells score ownership of frontier AI, extreme concentration of power, epistemics, decision theory, and space governance.
- **What the source does not cover:** I found no explicit requirement that each foreign middle power remain democratic.
- **Calibrated take:** the current ANZ table is internally consistent but depends on an unresolved semantic assumption. It remains our modelling choice, not an AI 2040 forecast.

## ANZ estimate to collect

The 30% should be replaced or supported by independent estimates from people who understand Australian or New Zealand institutions. Ask before revealing our current value:

> Conditional on rapid AI progress, Plan A being attempted, humans retaining control of AI, and ANZ receiving material access to the AI economy: what is the probability that Australia or New Zealand ceases to be a meaningful democracy by 2045?

Define meaningful democracy as competitive elections that can remove the executive, with courts, opposition, and protest still able to constrain power. Ask for Australia, New Zealand, either country, and both countries separately. Collect a probability, a 90% confidence interval, and the main causal mechanism. Do not calculate the joint answers by assuming Australia and New Zealand are independent.
