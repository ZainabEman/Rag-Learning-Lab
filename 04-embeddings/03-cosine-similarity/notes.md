# Cosine Similarity

> Status: `studied` (self-study, outside the course) | Section: [Embeddings](../README.md)

## What is it?

The standard metric for comparing embeddings: the cosine of the angle between
two vectors.

```
cos(u, v) = (u · v) / (||u|| · ||v||)
```

Range −1 to 1 (in practice 0 to 1 for text embeddings). 1 = same direction.

## Why it matters

It measures **direction, not magnitude**. Two documents about the same topic
should score as similar whether one is a sentence and the other three
paragraphs — and cosine ignores that length difference, while Euclidean distance
does not.

## How it works

The dot product measures alignment; dividing by both norms removes length.

Useful shortcut: if vectors are **normalised to unit length**, cosine similarity
and dot product are identical — which is why most vector stores normalise on
insert and then use the cheaper dot product.

## Simple example

```python
import math

def cosine(u, v):
    dot = sum(a * b for a, b in zip(u, v))
    nu = math.sqrt(sum(a * a for a in u))
    nv = math.sqrt(sum(b * b for b in v))
    return dot / (nu * nv)

cosine([1, 0, 1], [1, 0, 1])   # 1.0  - identical direction
cosine([1, 0, 1], [2, 0, 2])   # 1.0  - same direction, different magnitude
cosine([1, 0, 0], [0, 1, 0])   # 0.0  - orthogonal
```

## Remember

- Cosine ignores magnitude; Euclidean does not. For text, ignoring it is
  usually what you want.
- On normalised vectors, cosine == dot product. Vector stores exploit this.
- Many stores report **distance** (`1 − cosine`), so **lower is better** there.
  Always check which one an API returns.
- A high cosine score between unrelated short texts is common — short vectors
  are noisy.

## Related

- [02-semantic-similarity](../02-semantic-similarity/) · [05-vector-search/02-similarity-search](../../05-vector-search/02-similarity-search/)
