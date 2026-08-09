# Resources - RAG vs Fine-tuning

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| RAG: why, what and how (LangChain playlist, video 1 of 2) | Course video | *TODO - paste the video URL* | Primary source: what fine-tuning is, the four-step SFT process, and why repeated retraining makes it a poor fit for changing knowledge. |
| Language Models are Few-Shot Learners (GPT-3) | Paper | https://arxiv.org/abs/2005.14165 | Quantifies the fine-tuning data cost (roughly 10k-1M labelled rows) that the whole comparison turns on. |
| LoRA: Low-Rank Adaptation of Large Language Models | Paper | https://arxiv.org/abs/2106.09685 | Named in the course as a parameter-efficient fine-tuning method. Added for reference; not yet read. |

## Best explanation I found

The engineering-graduate analogy: pre-training is the degree, fine-tuning is the
two-to-three month onboarding at the company. It makes clear that fine-tuning
*specialises* rather than replaces.

The sharper insight was about **deletion**. Adding knowledge by fine-tuning is
merely expensive; removing it is genuinely hard. RAG deletes a row. That
asymmetry decides more real architectures than the cost comparison does.

## Explanations that did NOT help

"RAG vs fine-tuning" content framed as a competition with a winner. They solve
different problems - knowledge versus behaviour - and production systems
routinely use both.

<!-- Add sources here as I find them. -->
