# Resources - Document Loading

Only things I actually read or watched. No link dumps.

| Resource | Type | Link | Why it was useful |
| --- | --- | --- | --- |
| Document Loaders (LangChain playlist) | Course video | *TODO — paste the video URL* | Primary source: the `Document` object, the four core loaders, `DirectoryLoader`, and `load()` vs `lazy_load()`. |
| LangChain document loader integrations | Docs | https://python.langchain.com/docs/integrations/document_loaders/ | The full catalogue, grouped by category (web pages, PDFs, cloud, messaging, common file types). Reference material — not for reading end to end. |
| How to load PDFs | Docs | https://python.langchain.com/docs/how_to/document_loader_pdf/ | Which PDF loader to use for which kind of PDF, including layout and image extraction. |
| How to write a custom document loader | Docs | https://python.langchain.com/docs/how_to/document_loader_custom/ | Subclassing the base loader to implement `lazy_load()` for a source with no existing loader. |
| pypdf | Library | https://pypdf.readthedocs.io/ | What `PyPDFLoader` actually calls. Worth knowing, since its limitations are the loader's limitations. |
| BeautifulSoup | Library | https://www.crummy.com/software/BeautifulSoup/bs4/doc/ | What `WebBaseLoader` uses to turn HTML into text, alongside `requests`. |

> LangChain documentation URLs move between versions. If one 404s, search the
> docs rather than assuming the page is gone.

## Best explanation I found

The most useful single idea was that **every loader returns a list**, and that
what determines the list length is a per-loader policy: one document per file,
per page, per row, or per URL. Once that clicked, every loader became
predictable without reading its documentation — and the `1186 = 326 + 392 + 468`
arithmetic on three PDFs made it concrete.

## Explanations that did NOT help

Loader documentation that shows only the happy path (`loader.load()`, done) and
never mentions `lazy_load()`. It is the more important of the two methods for
any real corpus, and it is usually a footnote.

<!-- Add sources here as I find them. -->
