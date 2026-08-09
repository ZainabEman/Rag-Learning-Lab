# 13 Multimodal RAG

> Track: **ADVANCED TOPICS** | [Back to repository root](../README.md)

Retrieval over documents that are not plain text: images, layout, tables, charts, audio and video.

## Topics

| # | Topic | What it covers | Status |
| --- | --- | --- | --- |
| 01 | [Image Retrieval](01-image-retrieval/) | Retrieving images by text query and images by image. | `not started` |
| 02 | [Image Embeddings](02-image-embeddings/) | How image vectors are produced and how they relate to text vectors. | `not started` |
| 03 | [CLIP](03-clip/) | Contrastive image-text pretraining and the shared embedding space it produces. | `not started` |
| 04 | [Vision-Language Models](04-vision-language-models/) | Using a VLM to describe or answer over retrieved pages instead of parsing them to text first. | `not started` |
| 05 | [PDF Layout Understanding](05-pdf-layout-understanding/) | Reading order, columns, figures and captions; why naive text extraction destroys meaning. | `not started` |
| 06 | [OCR](06-ocr/) | Scanned and image-only documents; quality, errors and their downstream effect on retrieval. | `not started` |
| 07 | [Tables](07-tables/) | Extracting, representing and retrieving tabular data so numbers survive chunking. | `not started` |
| 08 | [Charts](08-charts/) | Getting answerable information out of figures - description, data extraction, or page-image retrieval. | `not started` |
| 09 | [Multimodal Embeddings](09-multimodal-embeddings/) | Unified vs separate index designs for mixed-modality corpora. | `not started` |
| 10 | [Video RAG](10-video-rag/) | Segmentation, transcripts, keyframes and timestamped citation. | `not started` |
| 11 | [Audio RAG](11-audio-rag/) | Transcription, diarisation and chunking of spoken content. | `not started` |

## How to work through this section

1. Read the source material, then write `notes.md` in the topic folder in my own words.
2. Implement it in `implementation.py` - from scratch first, library second.
3. Run the experiment and record what actually happened.
4. Tick the topic off in [PROGRESS.md](../PROGRESS.md) and add an entry to
   [LEARNING_LOG.md](../LEARNING_LOG.md).

## Adding a new topic to this section

Copy the template and keep the numbering:

```bash
python _templates/new_topic.py 13-multimodal-rag <next-number>-<topic-slug> "Topic Title"
```
