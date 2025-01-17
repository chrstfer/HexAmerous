from langchain.document_loaders import PlaywrightURLLoader, SitemapLoader
from langchain.text_splitter import TextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from embeddings import create_embedding, load_embedding, base_formatter
from langchain.text_splitter import TokenTextSplitter
from langchain.document_loaders.sitemap import SitemapLoader
import nest_asyncio



#Scrape a website
def scrape_site(url):

    #Load Langchain variables
    embeddings = OpenAIEmbeddings()
    text_splitter = TokenTextSplitter(chunk_size=300, chunk_overlap=25)
    urls = [
        str(url)
    ]

    #File loader/scraper
    loader = PlaywrightURLLoader(urls=urls, remove_selectors=["header", "footer"])
    raw_data = loader.load()
    data = raw_data[0].page_content

    #Text splitter
    texts = text_splitter.split_text(data)
    print(texts)

    #Store in database
    chromadb = Chroma.from_texts(texts, embeddings, persist_directory='docs/index')
    chromadb.persist()

    return chromadb


def scrape_site_map(site_path, collection_name):

    nest_asyncio.apply()

    sitemap_loader = SitemapLoader(web_path=site_path)

    docs = sitemap_loader.load()
    data = docs[0].page_content

    #Text splitter
    texts = text_splitter.split_text(data)
    print(texts)

    #Store in database
    chromadb = Chroma.from_documents(texts, embeddings, persist_directory='docs/index',collection_name=collection_name)
    chromadb.persist()

    return chromadb