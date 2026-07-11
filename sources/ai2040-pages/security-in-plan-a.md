---
url: https://ai-2040.com/supplements/security-in-plan-a
---

## [AI 2040](/)

≡[PDF](https://ghjyjqzwz4.ufs.sh/f/9qHa0cBclQ7sf6FVzqbp2gHFXC1IbGS5ZA7DmNBusfM4YJRP)

[Supplements](/supplements)

Plan A Basics

[FAQFAQ](/supplements/faq)[How Plan A solves our 5 biggest problemsHow Plan A solves our 5 biggest problems](/supplements/how-plan-a-solves-our-5-biggest-problems)

Plan A Policies

[Covert AI ProjectsCovert AI Projects](/supplements/covert-ai-projects)[Verification PlanVerification Plan](/supplements/verification-plan)[Transparency PlanTransparency Plan](/supplements/transparency-plan)[Capability Scaling StrategyCapability Scaling Strategy](/supplements/capability-scaling-strategy)[Security in Plan ASecurity in Plan A](/supplements/security-in-plan-a)

Analysis of Plan A Policies

[Plan A AssumptionsPlan A Assumptions](/supplements/plan-a-assumptions)[Comparing Possible PlansComparing Possible Plans](/supplements/comparing-possible-plans)[Deal DeclineDeal Decline](/supplements/deal-decline)[Takeoff SupplementTakeoff Supplement](/supplements/takeoff-supplement)

Economics

[Economics of Plan AEconomics of Plan A](/supplements/economics-of-plan-a)[Compute in Plan ACompute in Plan A](/supplements/compute-supplement)[Economic Growth ExplorerEconomic Growth Explorer](/supplements/econ-explorer)

Speculative Analysis

[Space Governance PlanSpace Governance Plan](/supplements/space-governance-plan)[AI for EpistemicsAI for Epistemics](/supplements/ai-for-epistemics)[Alignment RoadmapAlignment Roadmap](/supplements/alignment-roadmap)

[About](/about)

[![AI Futures Project](/ai-futures-logo.svg)](https://ai-futures.org/)

# Security in Plan A

### Romeo Dean, Thomas Larsen

Security is an area where expertise and access to classified information is particularly important for having an informed opinion. Nonetheless, this supplement provides a high-level overview of the security needed in Plan A in our best understanding, and why we think it is tractable.

We think it useful to think about three types of security, in increasing levels of difficulty from our point of view:

  1. **Model weights security:** Defending the exfiltration of model weights, and other large datasets.

     * Metric we care about: Exfiltration bandwidth. I.e., how much can the attacker steal in a given amount of time?

  2. **Verification integrity security:** Can we trust the results of our verification measures?

     * Metric we care about: Assurance level (the confidence-coverage curve explained in the verification supplement). I.e., how confident are we that the maximum unverified compute usage was less than X% (for values of X between 0 and 100%).

  3. **Algorithmic confidentiality:** Defending the exfiltration of code, algorithmic secrets, and anything else that doesn’t classify as ‘large datasets’.

     * Metric we care about: We are unsure. On the one hand, we could think about algorithmic security in terms of exfiltration bandwidth as well, but algorithmic secrets might be tiny and have an unpredictable mapping from data size to usefulness. Therefore it’s probably best to think about the percentage of algorithmic efficiency that is exfiltrated and usable by the attacker.




Throughout this supplement, we assume an [OC5 attacker](https://www.rand.org/pubs/research_reports/RRA2849-1.html) per RAND’s definition, because in Plan A the US and China will be worried about each other being potential attackers.

## Plan A security summary

In our scenario, we assume that SL5 security for model weights and to detect verification tampering is **viable with extreme effort; this is our low confidence best guess. It may turn out to be impossible** , in which case Plan A would need to be modified, which we discuss [here](/supplements/plan-a-assumptions#less-central-updates).

The security level desirable in Plan A is as follows:

| **Model Weights**| **Algorithmic Secrets**| **Verification**  
---|---|---|---  
**Inference Datacenters**|  SL5-100TB-5y(Maximum exfiltration of 100TB over 5y)| n/a| SL5(increasing assurance over time as compute scales)  
**R &D Datacenters**| SL5-100TB-5y| Depends on the transparency regime. In Total Research Transparency, most are intentionally transparent, small fraction SL5.| SL5(increasing assurance over time with compute scale)  
  
## Model weights security

Goal: We think the goal for model weights security in Plan A requires that frontier model weights (and similarly large important datasets) cannot be exfiltrated and used by potential adversaries and/or covert projects.

Concretely, we think the goal should be to defend against around 100TB of exfiltration over 5 years. Which we define as: weights security level 5, for 100TB over 5 years, or SL5-100TB-5y for short. We don’t think this will be trivial, but we do think it is highly tractable.

The following figure shows the size we expect frontier models to be in Plan A (and we also expect other datasets to be of similar magnitude, since data and parameters should continue to trade off with each other in compute optimal scaling).

**Frontier model size, 2022 to 2040**

Model sizeTraining compute

reportedours (α=0.5)α ∈ [0.2, 0.8]Nesov

1101001k10k100k1M2022202620292032203520382040Trillion parameters2026 anchor2029 dealGPT-4 ~1.8Tα=0.8α=0.2~650T (Nesov)31,000T~158T

### Plan A implementation

The **inference data centers** have SL-5 model weights security via defenses including:

  * They are surrounded by an information boundary, which is the datacenter walls, including a copper box (a faraday cage) preventing signals from coming in or out, except for one cable in and out of the datacenter, and a secure exchange chamber for other things that need to cross the perimeter.

  * For the output cable (which needs to exist, in order to communicate with the outside world), we make sure that the only information coming out of that wire is verified tokens produced by whitelisted models. You can read more in our [verification supplement](https://www.ai-2040.com/supplements/verification-plan). This is also similar to the proposal in [this paper](https://arxiv.org/abs/2511.02620).

  * For the other things that need to cross the boundary, power in, heat out, people in and out, we have further side channel mitigations and total bandwidth capping.




The **R &D datacenters** have two deliberate channels that allow information to leave the datacenter: (1) physically sending model weights to the inference datacenters, and (2) the fully transparent output channel used by researchers and for queries.

  * **The transportation of the model weights to the inference datacenters.** When a model is approved for public deployment, a package including the weights file, and any approved inference code (e.g., control scaffolds) gets downloaded on devices encrypted (sequentially) by both the US and China and physically escorted by both sides to inference clusters. At the inference clusters, they are added to the inference whitelist to allow for inference verification on public deployment.

  * **The transparent output channel** caps the total bandwidth coming off the datacenter at 1 MB/s, which means that over a 5 year period, 157 TB leave the datacenter. This is enough to let 50,000 people continuously read outputs at around 10 tokens / second (which might have thousands of corresponding internal chain of thought / scaffold tokens that don’t need to be outputted). Model weights of a current frontier model are currently on the order of 1T parameters (which corresponds to 1TB), so exfiltrating model weights via this channel would require hijacking .6% of the (fully transparent) output channel continuously for 5 years (or a larger fraction for a smaller duration of time), which would very likely be noticed. In Plan A, with compute scaling favoured over algorithmic progress, we expect the model weights of frontier models to become closer to 100T parameters, so a full exfiltration would require a continuous 60% of the output bandwidth for 5 years, ignoring compressibility which shouldn’t be a huge factor. There are additional layers of defense against model weight exfiltration within the datacenter: notably, we attempt to keep model weights on the opaque internal database.




The remaining threat models involve side channel attacks (such as staff members carrying small flash drives), and we don’t have a creative solution here: access to all of the data centers is tightly controlled, and well-funded, creative security teams are constantly red teaming and hardening the facilities. It also helps that the datacenters in Plan A are built from scratch in areas with low background radiofrequency (RF) noise with security top of mind.

Finally, the model weights also need to be regularly transported between the R&D datacenters (where they are trained) and the inference datacenters. We imagine that this could happen by transporting the model weights using several physical storage devices that are locked and continuously monitored by representatives of both the US and China for the entire duration of the transportation.

## Verification integrity

Goal: The goal for verification integrity should be to achieve a desirable assurance curve: The assurance curve captures information about the level of **coverage** (the % of the AI compute that the verification solution makes claims about) and **confidence** (with what probability is the verification solution correct about the claims it makes on the covered resources). We define an assurance curve as a set of relevant (coverage, confidence) values.

For example, with the middle curve, there is 99.99% confidence that 99.9% of the compute was verified to have been used correctly. Of course, such curves are theoretical and will be hard to measure, but conceptually we think its useful to think about the verification integrity goal in terms of this curve.

We think that the verification integrity goal should compare the risk incurred from verification integrity subversions (i.e., internal rogue compute uses) to external ongoing risk from other sources of rogue compute usage, i.e., covert projects, and aim for the possible internal rogue compute uses to be negligible in terms of additional risk vs. the external uses. Since internal rogue compute might have access to the opaque internal information (frontier weights, datasets and potentially some defended algorithms/code depending on the transparency regime) it is potentially much riskier than an equivalent amount of external covert project compute usage. A good approximation of ‘how much riskier’ might be to consider the gap in algorithmic efficiency available inside the R&D datacenters vs. in the potential covert projects.

Concretely, we think we should take something like the 90th percentile estimate of covert project effective compute (in terms of the frontier project’s current software level, so it's scaled to be comparable to internal compute use), and then set the verification integrity target such that we are 90% confident that the coverage of internal compute usage is at the level X (e.g., X=99.999% of the internal compute) such that the potential rogue internal compute (1-X) would be 10x smaller than the covert project’s effective compute. This basically would be like saying “we are 90% confident that rogue internal deployments would be about equivalent to a 10x smaller covert project than what we think might exist.”

### Plan A implementation

Verification in both R&D and inference datacenters needs to be mutually trusted by the US and China, so that they are both confident only the approved training runs, experiments, and inference workloads are running. In our concrete proposal, inference and R&D verification both rely mostly on network taps for evidence collection and trusted recomputation servers for verification. In order to have durable trust in this verification solution, these devices should be mutually trusted (or alternatively, trusted [optical splitters and unilaterally trusted devices](https://nacicankaya.substack.com/p/catching-misreporting-about-ml-hardware-bd2)). There also needs to be physical security to check these devices don’t get tampered with or modified, and trust in the software stack they build on top of them (which probably means it should be extremely simple, and maybe even formally verified).

Outside of the verification devices themselves, verification will also rely on wider security properties of the cluster that overlap with model weights security. For example, there not being side channels that could let an attacker smuggle out the results of rogue internal computations.

Over time, the verification assurance will need to improve drastically with the scale of compute. We discuss this in more detail in our [verification supplement](https://www.ai-2040.com/supplements/verification-plan).

## Algorithmic security

Goal: This depends on the transparency regime that we are aiming for, which is discussed in our [transparency supplement](https://www.ai-2040.com/supplements/transparency-plan).

More concerned aboutpoor regulationMore concerned aboutcovert projectsProposal #1:Radical TransparencyProposal #2:Filtered TransparencyProposal #3:Algorithmic SecurityTransparency proposals spectrum \- ai-2040.com

### Plan A: Total Research Transparency

To a first approximation, there will no longer be any algorithmic secrets in AI under the Total Research Transparency version of Plan A. There are a few exceptions:

  1. Massive (potentially synthetic) datasets have similar properties to model weights (in particular, are very large), and so it is viable to limit their output via upload limits out of the R&D datacenter. This isn’t sufficient for preventing the exfiltration of any given data; but could prevent the exfiltration of most data. Data progress is a substantial fraction of overall algorithmic progress, and so securing data might be both tractable and important.

  2. Hyperparameters found via computationally intensive procedures. For some hyperparameters, efficient settings for them are found via expensive procedures like sweeps over the possible values, and then tests for the training run. These values are small, but do not have to be known by any human. The code for selecting these hyperparameters can be transparent, but we can prevent anyone from knowing the value that running the code found, because it is computationally expensive to determine the value.




1.

Initially, this simply means “when the company that owns the model decides to deploy it publicly.” Later there’ll be more regulations, which may or may not take the form of a formal pre-deployment approval process.

2.

The process for downloading the weights file is extremely controlled, with both US and Chinese auditors unlocking a secure enclosure where there is a secure device that can make download requests to the opaque internal database and encrypt the files. It is the only device in the entire cluster with a usb (or similar) port that allows any physical device insertion for downloading.

3.

1 MB/s × 60 × 60 × 24 × 365.25 × 5 = 157 TB.

4.

This assumes FP8 parameters, i.e., that each parameter is 1 byte.

5.

In Plan A, we also recommend deliberately increasing the size of the model weights in order to get the security benefit of the weights files being bigger and thus harder to exfiltrate. This would require additional training compute because you are no longer selecting model size to be on the [optimal compute-optimal curve](https://arxiv.org/abs/2203.15556).

6.

Cheap compression that requires tiny amounts of compute, and therefore might go undetected by the verification measures, should not go beyond a factor of 2-4x, e.g., through [huffman encoding](https://en.wikipedia.org/wiki/Huffman_coding) (lossless) or cheap post-training quantization techniques (e.g., [](https://arxiv.org/abs/2210.17323)[GPTQ](https://arxiv.org/abs/2210.17323), [](https://arxiv.org/abs/2306.00978)[AWQ](https://arxiv.org/abs/2306.00978), [](https://arxiv.org/abs/2211.10438)[SmoothQuant](https://arxiv.org/abs/2211.10438), [](https://arxiv.org/abs/2402.04396)[QuIP#](https://arxiv.org/abs/2402.04396), [](https://arxiv.org/abs/2401.06118)[AQLM](https://arxiv.org/abs/2401.06118)) which compress weights by 2-4× at negligible quality cost using typically 0.0001-0.01% of training compute. For compression attacks that go further, e.g., more aggressive quantization or LoRA-style decomposition (e.g., [](https://arxiv.org/abs/2106.09685)[LoRA](https://arxiv.org/abs/2106.09685), [](https://arxiv.org/abs/2305.14314)[QLoRA](https://arxiv.org/abs/2305.14314), [](https://arxiv.org/abs/2310.11454)[VeRA](https://arxiv.org/abs/2310.11454), [](https://arxiv.org/abs/2402.09353)[DoRA](https://arxiv.org/abs/2402.09353), [](https://arxiv.org/abs/2303.10512)[AdaLoRA](https://arxiv.org/abs/2303.10512)), which might have >1000x compression, detection of the unauthorized computation to do this compression becomes the more load bearing security property than the bandwidth limit itself. Even still, 100TB weights being compressed 10,000x to 10GB still means you need to use 0.1% of the output channel for 116 days (1 KB * 60 * 60 * 24 * 116 = 10GB) without detection (which might require a large hit from steganography). Regulation can always be aware of the risks of compression and do red-teaming to determine how tractable it is, and adjust training run rules and/or the output bandwidth cap accordingly.
