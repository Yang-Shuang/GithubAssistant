# llmware
![Static Badge](https://img.shields.io/badge/python-3.10_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?color=blue)
![PyPI - Version](https://img.shields.io/pypi/v/llmware?color=blue)
[![members](https://discord-live-members-count-badge.vercel.app/api/discord-members?guildId=1179245642770559067&label=discord%20members&color=5865F2)](https://discord.gg/bphreFK4NJ)
[![Documentation](https://github.com/llmware-ai/llmware/actions/workflows/pages.yml/badge.svg)](https://github.com/llmware-ai/llmware/actions/workflows/pages.yml)  

## 🧰🛠️ 构建基于知识的本地化、私有、安全的大语言模型（LLM）应用的统一框架       

`llmware` 针对 AI PC 和本地笔记本电脑进行了优化，支持在广泛的 Windows、Mac 和 Linux 平台上进行边缘计算和自我托管部署。它支持 GGUF、OpenVINO、ONNXRuntime、ONNXRuntime-QNN（高通）、WindowsLocalFoundry 和 PyTorch，提供高级接口，让你能够轻松利用针对目标平台优化的推理技术。  

 `llmware` 包含两个主要组件：  

 1.  **模型目录（含 300+ 个模型）** - 预打包为量化、优化格式的模型，以充分利用设备端的 GPU 和 NPU 能力。支持主流开源模型家族以及 50+ 个 llmware 微调的 SLIM、Bling、Dragon 和行业 BERT 模型，专门针对企业流程自动化中的关键任务进行了优化。同时也支持来自 OpenAI、Anthropic 和 Google 的主流云模型。  
 
 2.  **检索增强生成（RAG）流水线** - 集成组件涵盖将知识源连接到生成式 AI 模型的完整生命周期，具备广泛的文档解析与摄取能力，并能够构建可扩展的知识库。

通过整合这两个组件，`llmware` 提供了一套全面的工具集，让你能够快速构建基于知识的企業级 LLM 应用。  

我们的愿景是：AI 应当具备可持续性、准确性和成本效益，以最小的计算资源完成工作。  

我们几乎所有的示例和模型都可以在设备端运行——立即在你的笔记本电脑上开始使用。   

[加入 Discord 社区](https://discord.gg/MhZn5Nc39h)   |  [观看 YouTube 教程](https://www.youtube.com/@llmware)  | [在 Huggingface 探索我们的模型家族](https://www.huggingface.co/llmware)   


## 🎯 核心功能 
使用 `llmware` 编写代码基于以下几个主要概念：

<details>
<summary><b>模型目录（Model Catalog）</b>: 以统一的方式访问所有模型，无论底层实现如何，均可轻松查找。 
</summary>  


```python
#   300+ Models in Catalog with 50+ RAG-optimized BLING, DRAGON and Industry BERT models
#   Full support for GGUF, OpenVINO, Onnxruntime, HuggingFace, Sentence Transformers and major API-based models
#   Easy to extend to add custom models - see examples

from llmware.models import ModelCatalog
from llmware.prompts import Prompt

#   all models accessed through the ModelCatalog
models = ModelCatalog().list_all_models()

#   to use any model in the ModelCatalog - "load_model" method and pass the model_name parameter
my_model = ModelCatalog().load_model("llmware/bling-phi-3-gguf")

#   call model with: inference 
output = my_model.inference("what is the future of AI?", add_context="Here is the article to read")

#   call model with: stream
for token in my_model.stream("What is the future of AI?"):
    print(token, end="")

#   to integrate model into a Prompt
prompter = Prompt().load_model("llmware/bling-tiny-llama-v0")
response = prompter.prompt_main("what is the future of AI?", context="Insert Sources of information")
```

</details>  

<details>  
<summary><b>知识库（Library）</b>: 大规模地摄取、组织并索引知识集合——解析、文本分块与嵌入。</summary>  

```python

from llmware.library import Library

#   to parse and text chunk a set of documents (pdf, pptx, docx, xlsx, txt, csv, md, json/jsonl, wav, png, jpg, html)  

#   step 1 - create a library, which is the 'knowledge-base container' construct
#          - libraries have both text collection (DB) resources, and file resources (e.g., llmware_data/accounts/{library_name})
#          - embeddings and queries are run against a library

lib = Library().create_new_library("my_library")

#    step 2 - add_files is the universal ingestion function - point it at a local file folder with mixed file types
#           - files will be routed by file extension to the correct parser, parsed, text chunked and indexed in text collection DB

lib.add_files("/folder/path/to/my/files")

#   to install an embedding on a library - pick an embedding model and vector_db
lib.install_new_embedding(embedding_model_name="mini-lm-sbert", vector_db="milvus", batch_size=500)

#   to add a second embedding to the same library (mix-and-match models + vector db)  
lib.install_new_embedding(embedding_model_name="industry-bert-sec", vector_db="chromadb", batch_size=100)

#   easy to create multiple libraries for different projects and groups

finance_lib = Library().create_new_library("finance_q4_2023")
finance_lib.add_files("/finance_folder/")

hr_lib = Library().create_new_library("hr_policies")
hr_lib.add_files("/hr_folder/")

#    pull library card with key metadata - documents, text chunks, images, tables, embedding record
lib_card = Library().get_library_card("my_library")

#   see all libraries
all_my_libs = Library().get_all_library_cards()

```
</details>  

<details> 
<summary><b>查询（Query）</b>: 结合文本、语义、混合、元数据和自定义过滤器对知识库进行查询。</summary>

```python

from llmware.retrieval import Query
from llmware.library import Library

#   step 1 - load the previously created library 
lib = Library().load_library("my_library")

#   step 2 - create a query object and pass the library
q = Query(lib)

#    step 3 - run lots of different queries  (many other options in the examples)

#    basic text query
results1 = q.text_query("text query", result_count=20, exact_mode=False)

#    semantic query
results2 = q.semantic_query("semantic query", result_count=10)

#    combining a text query restricted to only certain documents in the library and "exact" match to the query
results3 = q.text_query_with_document_filter("new query", {"file_name": "selected file name"}, exact_mode=True)

#   to apply a specific embedding (if multiple on library), pass the names when creating the query object
q2 = Query(lib, embedding_model_name="mini_lm_sbert", vector_db="milvus")
results4 = q2.semantic_query("new semantic query")
```

</details>  

<details>
<summary><b>带来源的提示词（Prompt with Sources）</b>: 结合知识检索与 LLM 推理的最简单方式。</summary>

```python

from llmware.prompts import Prompt
from llmware.retrieval import Query
from llmware.library import Library

#   build a prompt
prompter = Prompt().load_model("llmware/bling-tiny-llama-v0")

#   add a file -> file is parsed, text chunked, filtered by query, and then packaged as model-ready context,
#   including in batches, if needed, to fit the model context window

source = prompter.add_source_document("/folder/to/one/doc/", "filename", query="fast query")

#   attach query results (from a Query) into a Prompt
my_lib = Library().load_library("my_library")
results = Query(my_lib).query("my query")
source2 = prompter.add_source_query_results(results)

#   run a new query against a library and load directly into a prompt
source3 = prompter.add_source_new_query(my_lib, query="my new query", query_type="semantic", result_count=15)

#   to run inference with 'prompt with sources'
responses = prompter.prompt_with_source("my query")

#   to run fact-checks - post inference
fact_check = prompter.evidence_check_sources(responses)

#   to view source materials (batched 'model-ready' and attached to prompt)
source_materials = prompter.review_sources_summary()

#   to see the full prompt history
prompt_history = prompter.get_current_history()
```

</details>  

<details> 
<summary><b>RAG 优化模型（RAG-Optimized Models）</b> - 专为 RAG 工作流集成和本地运行而设计的 10亿至 70亿参数模型。</summary>  

```
""" This 'Hello World' example demonstrates how to get started using local BLING models with provided context, using both
Pytorch and GGUF versions. """

import time
from llmware.prompts import Prompt


def hello_world_questions():

    test_list = [

    {"query": "What is the total amount of the invoice?",
     "answer": "$22,500.00",
     "context": "Services Vendor Inc. \n100 Elm Street Pleasantville, NY \nTO Alpha Inc. 5900 1st Street "
                "Los Angeles, CA \nDescription Front End Engineering Service $5000.00 \n Back End Engineering"
                " Service $7500.00 \n Quality Assurance Manager $10,000.00 \n Total Amount $22,500.00 \n"
                "Make all checks payable to Services Vendor Inc. Payment is due within 30 days."
                "If you have any questions concerning this invoice, contact Bia Hermes. "
                "THANK YOU FOR YOUR BUSINESS!  INVOICE INVOICE # 0001 DATE 01/01/2022 FOR Alpha Project P.O. # 1000"},

    {"query": "What was the amount of the trade surplus?",
     "answer": "62.4 billion yen ($416.6 million)",
     "context": "Japan’s September trade balance swings into surplus, surprising expectations"
                "Japan recorded a trade surplus of 62.4 billion yen ($416.6 million) for September, "
                "beating expectations from economists polled by Reuters for a trade deficit of 42.5 "
                "billion yen. Data from Japan’s customs agency revealed that exports in September "
                "increased 4.3% year on year, while imports slid 16.3% compared to the same period "
                "last year. According to FactSet, exports to Asia fell for the ninth straight month, "
                "which reflected ongoing China weakness. Exports were supported by shipments to "
                "Western markets, FactSet added. — Lim Hui Jie"},

    {"query": "When did the LISP machine market collapse?",
     "answer": "1987.",
     "context": "The attendees became the leaders of AI research in the 1960s."
                "  They and their students produced programs that the press described as 'astonishing': "
                "computers were learning checkers strategies, solving word problems in algebra, "
                "proving logical theorems and speaking English.  By the middle of the 1960s, research in "
                "the U.S. was heavily funded by the Department of Defense and laboratories had been "
                "established around the world. Herbert Simon predicted, 'machines will be capable, "
                "within twenty years, of doing any work a man can do'.  Marvin Minsky agreed, writing, "
                "'within a generation ... the problem of creating 'artificial intelligence' will "
                "substantially be solved'. They had, however, underestimated the difficulty of the problem.  "
                "Both the U.S. and British governments cut off exploratory research in response "
                "to the criticism of Sir James Lighthill and ongoing pressure from the US Congress "
                "to fund more productive projects. Minsky's and Papert's book Perceptrons was understood "
                "as proving that artificial neural networks approach would never be useful for solving "
                "real-world tasks, thus discrediting the approach altogether.  The 'AI winter', a period "
                "when obtaining funding for AI projects was difficult, followed.  In the early 1980s, "
                "AI research was revived by the commercial success of expert systems, a form of AI "
                "program that simulated the knowledge and analytical skills of human experts. By 1985, "
                "the market for AI had reached over a billion dollars. At the same time, Japan's fifth "
                "generation computer project inspired the U.S. and British governments to restore funding "
                "for academic research. However, beginning with the collapse of the Lisp Machine market "
                "in 1987, AI once again fell into disrepute, and a second, longer-lasting winter began."},

    {"query": "What is the current rate on 10-year treasuries?",
     "answer": "4.58%",
     "context": "Stocks rallied Friday even after the release of stronger-than-expected U.S. jobs data "
                "and a major increase in Treasury yields.  The Dow Jones Industrial Average gained 195.12 points, "
                "or 0.76%, to close at 31,419.58. The S&P 500 added 1.59% at 4,008.50. The tech-heavy "
                "Nasdaq Composite rose 1.35%, closing at 12,299.68. The U.S. economy added 438,000 jobs in "
                "August, the Labor Department said. Economists polled by Dow Jones expected 273,000 "
                "jobs. However, wages rose less than expected last month.  Stocks posted a stunning "
                "turnaround on Friday, after initially falling on the stronger-than-expected jobs report. "
                "At its session low, the Dow had fallen as much as 198 points; it surged by more than "
                "500 points at the height of the rally. The Nasdaq and the S&P 500 slid by 0.8% during "
                "their lowest points in the day.  Traders were unclear of the reason for the intraday "
                "reversal. Some noted it could be the softer wage number in the jobs report that made "
                "investors rethink their earlier bearish stance. Others noted the pullback in yields from "
                "the day’s highs. Part of the rally may just be to do a market that had gotten extremely "
                "oversold with the S&P 500 at one point this week down more than 9% from its high earlier "
                "this year.  Yields initially surged after the report, with the 10-year Treasury rate trading "
                "near its highest level in 14 years. The benchmark rate later eased from those levels, but "
                "was still up around 6 basis points at 4.58%.  'We’re seeing a little bit of a give back "
                "in yields from where we were around 4.8%. [With] them pulling back a bit, I think that’s "
                "helping the stock market,' said Margaret Jones, chief investment officer at Vibrant Industries "
                "Capital Advisors. 'We’ve had a lot of weakness in the market in recent weeks, and potentially "
                "some oversold conditions.'"},

    {"query": "Is the expected gross margin greater than 70%?",
     "answer": "Yes, between 71.5% and 72.%",
     "context": "Outlook NVIDIA’s outlook for the third quarter of fiscal 2024 is as follows:"
                "Revenue is expected to be $16.00 billion, plus or minus 2%. GAAP and non-GAAP "
                "gross margins are expected to be 71.5% and 72.5%, respectively, plus or minus "
                "50 basis points.  GAAP and non-GAAP operating expenses are expected to be "
                "approximately $2.95 billion and $2.00 billion, respectively.  GAAP and non-GAAP "
                "other income and expense are expected to be an income of approximately $100 "
                "million, excluding gains and losses from non-affiliated investments. GAAP and "
                "non-GAAP tax rates are expected to be 14.5%, plus or minus 1%, excluding any discrete items."
                "Highlights NVIDIA achieved progress since its previous earnings announcement "
                "in these areas:  Data Center Second-quarter revenue was a record $10.32 billion, "
                "up 141% from the previous quarter and up 171% from a year ago. Announced that the "
                "NVIDIA® GH200 Grace™ Hopper™ Superchip for complex AI and HPC workloads is shipping "
                "this quarter, with a second-generation version with HBM3e memory expected to ship "
                "in Q2 of calendar 2024. "},

    {"query": "What is Bank of America's rating on Target?",
     "answer": "Buy",
     "context": "Here are some of the tickers on my radar for Thursday, Oct. 12, taken directly from "
                "my reporter’s notebook: It’s the one-year anniversary of the S&P 500′s bear market bottom "
                "of 3,577. Since then, as of Wednesday’s close of 4,376, the broad market index "
                "soared more than 22%.  Hotter than expected September consumer price index, consumer "
                "inflation. The Social Security Administration issues announced a 3.2% cost-of-living "
                "adjustment for 2024.  Chipotle Mexican Grill (CMG) plans price increases. Pricing power. "
                "Cites consumer price index showing sticky retail inflation for the fourth time "
                "in two years. Bank of America upgrades Target (TGT) to buy from neutral. Cites "
                "risk/reward from depressed levels. Traffic could improve. Gross margin upside. "
                "Merchandising better. Freight and transportation better. Target to report quarter "
                "next month. In retail, the CNBC Investing Club portfolio owns TJX Companies (TJX), "
                "the off-price juggernaut behind T.J. Maxx, Marshalls and HomeGoods. Goldman Sachs "
                "tactical buy trades on Club names Wells Fargo (WFC), which reports quarter Friday, "
                "Humana (HUM) and Nvidia (NVDA). BofA initiates Snowflake (SNOW) with a buy rating."
                "If you like this story, sign up for Jim Cramer’s Top 10 Morning Thoughts on the "
                "Market email newsletter for free. Barclays cuts price targets on consumer products: "
                "UTZ Brands (UTZ) to $16 per share from $17. Kraft Heinz (KHC) to $36 per share from "
                "$38. Cyclical drag. J.M. Smucker (SJM) to $129 from $160. Secular headwinds. "
                "Coca-Cola (KO) to $59 from $70. Barclays cut PTs on housing-related stocks: Toll Brothers"
                "(TOL) to $74 per share from $82. Keeps underweight. Lowers Trex (TREX) and Azek"
                "(AZEK), too. Goldman Sachs (GS) announces sale of fintech platform and warns on "
                "third quarter of 19-cent per share drag on earnings. The buyer: investors led by "
                "private equity firm Sixth Street. Exiting a mistake. Rise in consumer engagement for "
                "Spotify (SPOT), says Morgan Stanley. The analysts hike price target to $190 per share "
                "from $185. Keeps overweight (buy) rating. JPMorgan loves elf Beauty (ELF). Keeps "
                "overweight (buy) rating but lowers price target to $139 per share from $150. "
                "Sees “still challenging” environment into third-quarter print. The Club owns shares "
                "in high-end beauty company Estee Lauder (EL). Barclays upgrades First Solar (FSLR) "
                "to overweight from equal weight (buy from hold) but lowers price target to $224 per "
                "share from $230. Risk reward upgrade. Best visibility of utility scale names."},

    {"query": "What was the rate of decline in 3rd quarter sales?",
     "answer": "20% year-on-year.",
     "context": "Nokia said it would cut up to 14,000 jobs as part of a cost cutting plan following "
                "third quarter earnings that plunged. The Finnish telecommunications giant said that "
                "it will reduce its cost base and increase operation efficiency to “address the "
                "challenging market environment. The substantial layoffs come after Nokia reported "
                "third-quarter net sales declined 20% year-on-year to 4.98 billion euros. Profit over "
                "the period plunged by 69% year-on-year to 133 million euros."},

    {"query": "What is a list of the key points?",
     "answer": "•Stocks rallied on Friday with stronger-than-expected U.S jobs data and increase in "
               "Treasury yields;\n•Dow Jones gained 195.12 points;\n•S&P 500 added 1.59%;\n•Nasdaq Composite rose "
               "1.35%;\n•U.S. economy added 438,000 jobs in August, better than the 273,000 expected;\n"
               "•10-year Treasury rate trading near the highest level in 14 years at 4.58%.",
     "context": "Stocks rallied Friday even after the release of stronger-than-expected U.S. jobs data "
               "and a major increase in Treasury yields.  The Dow Jones Industrial Average gained 195.12 points, "
               "or 0.76%, to close at 31,419.58. The S&P 500 added 1.59% at 4,008.50. The tech-heavy "
               "Nasdaq Composite rose 1.35%, closing at 12,299.68. The U.S. economy added 438,000 jobs in "
               "August, the Labor Department said. Economists polled by Dow Jones expected 273,000 "
               "jobs. However, wages rose less than expected last month.  Stocks posted a stunning "
               "turnaround on Friday, after initially falling on the stronger-than-expected jobs report. "
               "At its session low, the Dow had fallen as much as 198 points; it surged by more than "
               "500 points at the height of the rally. The Nasdaq and the S&P 500 slid by 0.8% during "
               "their lowest points in the day.  Traders were unclear of the reason for the intraday "
               "reversal. Some noted it could be the softer wage number in the jobs report that made "
               "investors rethink their earlier bearish stance. Others noted the pullback in yields from "
               "the day’s highs. Part of the rally may just be to do a market that had gotten extremely "
               "oversold with the S&P 500 at one point this week down more than 9% from its high earlier "
               "this year.  Yields initially surged after the report, with the 10-year Treasury rate trading "
               "near its highest level in 14 years. The benchmark rate later eased from those levels, but "
               "was still up around 6 basis points at 4.58%.  'We’re seeing a little bit of a give back "
               "in yields from where we were around 4.8%. [With] them pulling back a bit, I think that’s "
               "helping the stock market,' said Margaret Jones, chief investment officer at Vibrant Industries "
               "Capital Advisors. 'We’ve had a lot of weakness in the market in recent weeks, and potentially "
               "some oversold conditions.'"}

    ]

    return test_list


# this is the main script to be run

def bling_meets_llmware_hello_world (model_name):

    t0 = time.time()

    # load the questions
    test_list = hello_world_questions()

    print(f"\n > Loading Model: {model_name}...")

    # load the model 
    prompter = Prompt().load_model(model_name)

    t1 = time.time()
    print(f"\n > Model {model_name} load time: {t1-t0} seconds")
 
    for i, entries in enumerate(test_list):

        print(f"\n{i+1}. Query: {entries['query']}")
     
        # run the prompt
        output = prompter.prompt_main(entries["query"],context=entries["context"]
                                      , prompt_name="default_with_context",temperature=0.30)

        # print out the results
        llm_response = output["llm_response"].strip("\n")
        print(f"LLM Response: {llm_response}")
        print(f"Gold Answer: {entries['answer']}")
        print(f"LLM Usage: {output['usage']}")

    t2 = time.time()

    print(f"\nTotal processing time: {t2-t1} seconds")

    return 0


if __name__ == "__main__":

    # list of 'rag-instruct' laptop-ready small bling models on HuggingFace

    pytorch_models = ["llmware/bling-1b-0.1",                    #  most popular
                      "llmware/bling-tiny-llama-v0",             #  fastest 
                      "llmware/bling-1.4b-0.1",
                      "llmware/bling-falcon-1b-0.1",
                      "llmware/bling-cerebras-1.3b-0.1",
                      "llmware/bling-sheared-llama-1.3b-0.1",    
                      "llmware/bling-sheared-llama-2.7b-0.1",
                      "llmware/bling-red-pajamas-3b-0.1",
                      "llmware/bling-stable-lm-3b-4e1t-v0",
                      "llmware/bling-phi-3"                      # most accurate (and newest)  
                      ]

    #  Quantized GGUF versions generally load faster and run nicely on a laptop with at least 16 GB of RAM
    gguf_models = ["bling-phi-3-gguf", "bling-stablelm-3b-tool", "dragon-llama-answer-tool", "dragon-yi-answer-tool", "dragon-mistral-answer-tool"]

    #   try model from either pytorch or gguf model list
    #   the newest (and most accurate) is 'bling-phi-3-gguf'  

    bling_meets_llmware_hello_world(gguf_models[0]  

    #   check out the model card on Huggingface for RAG benchmark test performance results and other useful information
```

</details>

<details>
<summary><b>可扩展的数据库选项（Simple-to-Scale Database Options）</b> - 从笔记本电脑到并行集群的一体化数据存储。</summary>

```python

from llmware.configs import LLMWareConfig

#   to set the collection database - mongo, sqlite, postgres  
LLMWareConfig().set_active_db("mongo")  

#   to set the vector database (or declare when installing)  
#   --options: milvus, pg_vector (postgres), redis, qdrant, faiss, pinecone, mongo atlas  
LLMWareConfig().set_vector_db("milvus")  

#   for fast start - no installations required  
LLMWareConfig().set_active_db("sqlite")  
LLMWareConfig().set_vector_db("chromadb")   # try also faiss and lancedb  

#   for single postgres deployment  
LLMWareConfig().set_active_db("postgres")  
LLMWareConfig().set_vector_db("postgres")  

#   to install mongo, milvus, postgres - see the docker-compose scripts as well as examples

```

</details>

<details>

<summary><b>支持函数调用与 SLIM 模型的智能体（Agents）</b></summary>  

```python

from llmware.agents import LLMfx

text = ("Tesla stock fell 8% in premarket trading after reporting fourth-quarter revenue and profit that "
        "missed analysts’ estimates. The electric vehicle company also warned that vehicle volume growth in "
        "2024 'may be notably lower' than last year’s growth rate. Automotive revenue, meanwhile, increased "
        "just 1% from a year earlier, partly because the EVs were selling for less than they had in the past. "
        "Tesla implemented steep price cuts in the second half of the year around the world. In a Wednesday "
        "presentation, the company warned investors that it’s 'currently between two major growth waves.'")

#   create an agent using LLMfx class
agent = LLMfx()

#   load text to process
agent.load_work(text)

#   load 'models' as 'tools' to be used in analysis process
agent.load_tool("sentiment")
agent.load_tool("extract")
agent.load_tool("topics")
agent.load_tool("boolean")

#   run function calls using different tools
agent.sentiment()
agent.topics()
agent.extract(params=["company"])
agent.extract(params=["automotive revenue growth"])
agent.xsum()
agent.boolean(params=["is 2024 growth expected to be strong? (explain)"])

#   at end of processing, show the report that was automatically aggregated by key
report = agent.show_report()

#   displays a summary of the activity in the process
activity_summary = agent.activity_summary()

#   list of the responses gathered
for i, entries in enumerate(agent.response_list):
    print("update: response analysis: ", i, entries)

output = {"report": report, "activity_summary": activity_summary, "journal": agent.journal}  

```

</details>
<details>

<summary>🚀 <b>开始编码 - RAG 快速入门</b></summary>

```python
# This example illustrates a simple contract analysis
# using a RAG-optimized LLM running locally

import os
import re
from llmware.prompts import Prompt, HumanInTheLoop
from llmware.setup import Setup
from llmware.configs import LLMWareConfig

def contract_analysis_on_laptop (model_name):

    #  In this scenario, we will:
    #  -- download a set of sample contract files
    #  -- create a Prompt and load a BLING LLM model
    #  -- parse each contract, extract the relevant passages, and pass questions to a local LLM

    #  Main loop - Iterate thru each contract:
    #
    #      1.  parse the document in memory (convert from PDF file into text chunks with metadata)
    #      2.  filter the parsed text chunks with a "topic" (e.g., "governing law") to extract relevant passages
    #      3.  package and assemble the text chunks into a model-ready context
    #      4.  ask three key questions for each contract to the LLM
    #      5.  print to the screen
    #      6.  save the results in both json and csv for furthe processing and review.

    #  Load the llmware sample files

    print (f"\n > Loading the llmware sample files...")

    sample_files_path = Setup().load_sample_files()
    contracts_path = os.path.join(sample_files_path,"Agreements")
 
    #  Query list - these are the 3 main topics and questions that we would like the LLM to analyze for each contract

    query_list = {"executive employment agreement": "What are the name of the two parties?",
                  "base salary": "What is the executive's base salary?",
                  "vacation": "How many vacation days will the executive receive?"}

    #  Load the selected model by name that was passed into the function

    print (f"\n > Loading model {model_name}...")

    prompter = Prompt().load_model(model_name, temperature=0.0, sample=False)

    #  Main loop

    for i, contract in enumerate(os.listdir(contracts_path)):

        #   excluding Mac file artifact (annoying, but fact of life in demos)
        if contract != ".DS_Store":

            print("\nAnalyzing contract: ", str(i+1), contract)

            print("LLM Responses:")

            for key, value in query_list.items():

                # step 1 + 2 + 3 above - contract is parsed, text-chunked, filtered by topic key,
                # ... and then packaged into the prompt

                source = prompter.add_source_document(contracts_path, contract, query=key)

                # step 4 above - calling the LLM with 'source' information already packaged into the prompt

                responses = prompter.prompt_with_source(value, prompt_name="default_with_context")  

                # step 5 above - print out to screen

                for r, response in enumerate(responses):
                    print(key, ":", re.sub("[\n]"," ", response["llm_response"]).strip())

                # We're done with this contract, clear the source from the prompt
                prompter.clear_source_materials()

    # step 6 above - saving the analysis to jsonl and csv

    # Save jsonl report to jsonl to /prompt_history folder
    print("\nPrompt state saved at: ", os.path.join(LLMWareConfig.get_prompt_path(),prompter.prompt_id))
    prompter.save_state()

    # Save csv report that includes the model, response, prompt, and evidence for human-in-the-loop review
    csv_output = HumanInTheLoop(prompter).export_current_interaction_to_csv()
    print("csv output saved at:  ", csv_output)


if __name__ == "__main__":

    # use local cpu model - try the newest - RAG finetune of Phi-3 quantized and packaged in GGUF  
    model = "bling-phi-3-gguf"

    contract_analysis_on_laptop(model)

```
</details>

## 🔥 解决方案

如需项目灵感，请参阅 [solutions](https://github.com/llmware-ai/llmware/tree/main/solutions)，内含数十个创新示例。  

### OpenVINO 编码器（Encoders） - 设备端高效 RAG 的理想选择：
- 20 款 OV 优化编码模型，通过 `OVEmbeddingModel` 类支持广泛的嵌入、重排器和分类器，例如：  
- [使用 OpenVINO 嵌入模型](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_embedding_model.py)  
- [使用 OpenVINO 重排器模型](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_reranker_model.py)  
- [使用 OpenVINO 分类器模型](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_classifier_model.py)  

### ONNXRuntime 重排器（Reranker） - 使用针对 Onnxruntime 部署优化的重排器   

- [使用 ONNX 重排器模型](https://github.com/llmware-ai/llmware/blob/main/solutions/onnxruntime/using_onnx_reranker_models.py)   
  
### WindowsLocalFoundry 集成 - 在 llmware 中使用 WindowsLocalFoundry 模型  

- [使用本地 Foundry 模型](https://github.com/llmware-ai/llmware/blob/main/solutions/onnxruntime/using_local_foundry_models.py)  

### 模型仓库（Model Depot） - 最大的开箱即用 OpenVINO 基础 LLM 集合（95+ 个）   

- [Huggingface 上的 Model Depot](https://huggingface.co/collections/llmware/model-depot)   
- [使用流式生成与 OpenVino](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_streamer.py)     
- [OpenVino 入门指南](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_models.py)  

### 图像生成 - 多媒体机器人（Multimedia Bot）  
- [多媒体机器人示例](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/multimedia_bot.py)  

### ONNXRuntime-QNN - 在 Snapdragon NPU (Windows Arm64) 上运行模型 
- Model Catalog 中提供 7 款已优化至可直接运行的 NPU 模型 - 参见 [使用 QNN NPU 模型示例](https://github.com/llmware-ai/llmware/tree/main/solutions/onnxruntime/using-qnn-npu-models.py)  

### 面向专业 RAG 的行业专属嵌入模型（Embedding Models） 
- 查看 LLMware Industry Bert 模型系列 - 参见 [industry-bert-models](https://huggingface.co/collections/llmware/industry-bert-models)  

### 音频与文本处理
- **使用 WhisperCPP 进行语音转录**  
  借助 WhisperCPP 启动转录项目，提供示例文件使用和著名演讲解析工具。
  - [入门指南](solutions/gguf/using-whisper-cpp-getting-started.py) | [解析伟大演讲](solutions/gguf/parsing_great_speeches.py) | [演示视频](https://youtu.be/5y0ez5ZBpPE?si=KVxsXXtX5TzvlEws)

- **自然语言查询转 CSV**  
  使用 Slim-SQL 将自然语言查询转换为 CSV，支持自定义 Postgres 表。
  - [演示视频](https://youtu.be/z48z5XOXJJg?si=V-CX1w-7KRioI4Bi) | [端到端示例](solutions/slim_agents/text2sql-end-to-end-2.py) | [自定义表使用](https://github.com/llmware-ai/llmware/tree/main/solutions/slim_agents/agent_with_custom_tables.py)

### 多模型智能体（Multi-Model Agents）
- **结合 SLIM 的多模型智能体**  
  在 CPU 上使用 SLIM 模型执行复杂工作流中的多步智能体任务。
  - [演示视频](https://www.youtube.com/watch?v=cQfdaTcmBpY) | [示例目录](solutions/slim_agents)

### 文档与 OCR 处理
- **OCR 嵌入式文档图像**  
  系统性地从文档中的嵌入图像提取文本，增强文档处理能力。
  - [OCR 示例](solutions/sources/ocr_embedded_doc_images.py)

- **增强的 PDF、Word、PowerPoint 和 Excel 文档解析**  
  改进了文本分块控制、表格提取和内容解析功能。
  - [解析示例](solutions/sources/pdf_parser_new_configs.py)

- **优化 RAG 提示词的准确性**  
  关于调整 RAG 提示词设置以提高准确性的教程。
  - [配置示例](solutions/models/adjusting_sampling_settings.py) | 视频：[第一部分](https://youtu.be/7oMTGhSKuNY?si=14mS2pftk7NoKQbC), [第二部分](https://youtu.be/iXp1tj-pPjM?si=T4teUAISnSWgtThu)  
  
初次接触 RAG？[查看快速入门视频系列](https://www.youtube.com/playlist?list=PL1-dn33KwsmD7SB9iSO6vx4ZLRAWea1DB)  

[SLIM 函数调用模型简介](https://github.com/llmware-ai/llmware/blob/main/solutions/models/using_function_calls.py)  

## 🌱 快速开始

**步骤 1 - 安装 llmware** - `pip3 install llmware` 或 `pip3 install 'llmware[full]'`  

- [核心安装](https://github.com/llmware-ai/llmware/blob/main/llmware/requirements.txt)（最小依赖集）  
- [完整安装](https://github.com/llmware-ai/llmware/blob/main/llmware/requirements_extras.txt)（在核心基础上添加更广泛的 Python 库）。  

<details>
<summary><b>步骤 2 - 进入示例</b></summary>

## 🔥 最新热门示例 🔥  

端到端场景 - [**结合 SLIM Extract 与 Web 服务进行金融研究的函数调用**](https://github.com/llmware-ai/llmware/tree/main/solutions/use_cases/web_services_slim_fx.py)  
分析语音文件 - [**使用 LLM Query 和 Extract 解析伟大演讲**](https://github.com/llmware-ai/llmware/tree/main/solutions/use_cases/parsing_great_speeches.py)  
LLMWare 新手入门 - [**快速入门教程系列**](https://github.com/llmware-ai/llmware/tree/main/tutorials)  
环境配置 - [**开始使用指南**](https://github.com/llmware-ai/llmware/tree/main/tutorials/Getting_Started)  
SLIM 示例 - [**SLIM 模型**](solutions/slim_agents/)  

| 示例 | 说明 |
|-------------|--------------|
| 1. BLING 模型快速入门（[代码](solutions/models/bling_fast_start.py) / [视频](https://www.youtube.com/watch?v=JjgqOZ2v5oU)） | 使用快速、准确且基于 CPU 的模型开始工作——支持问答、键值提取和基本摘要。 |
| 2. 解析并嵌入 500 份 PDF 文档（[代码](solutions/embedding/docs2vecs_with_milvus-un_resolutions.py)） | 端到端示例：使用 Milvus 对联合国决议文档进行解析、嵌入和查询 |
| 3. 混合检索 - 语义 + 文本（[代码](solutions/sources/dual_pass_with_custom_filter.py)） | 使用“双路”检索结合语义搜索与文本搜索的最佳效果 |  
| 4. 使用 PG Vector 配置多个嵌入模型（[代码](solutions/embedding/using_multiple_embeddings.py) / [视频](https://www.youtube.com/watch?v=Bncvggy6m5Q)） | 使用 Postgres / PG Vector 比较多种嵌入模型 |
| 5. DRAGON GGUF 模型（[代码](solutions/models/dragon_gguf_fast_start.py) / [视频](https://www.youtube.com/watch?v=BI1RlaIJcsc&t=130s)） | 最先进的 7B RAG GGUF 模型。 | 
| 6. BLING + RAG（[代码](solutions/use_cases/contract_analysis_on_laptop_with_bling_models.py) / [视频](https://www.youtube.com/watch?v=8aV5p3tErP0)） | 以合同分析为例，在笔记本电脑上体验使用 `llmware` 的 BLING ~1B 参数 GPT 模型进行复杂文档分析和文本提取的 RAG。 |  
| 7. DRAGON + 主服务协议（MSA）分析（[代码](solutions/use_cases/msa_processing.py) / [视频](https://www.youtube.com/watch?v=Cf-07GBZT68&t=2s)） | 使用 DRAGON YI 6B 模型分析 MSA。   |                                                                                                                         
| 8. Streamlit UI 示例（[代码](solutions/ui/simple_rag_ui_with_streamlit.py)） | 通过 UI 向发票提问并运行推理。 |  
| 9. 集成 LM Studio（[代码](solutions/models/using-open-chat-models.py) / [视频](https://www.youtube.com/watch?v=h2FDjUyvsKE&t=101s)） | 将 LM Studio 模型与 LLMWare 集成 |                                                                                                                                       
| 10. 带来源的提示词（[代码](solutions/sources/prompt_with_sources.py)） | 直接将多种知识源附加到 Prompt 中。   |   
| 11. 事实核查（[代码](solutions/sources/fact_checking.py)） | 在此示例脚本中探索完整的证据方法，该脚本分析一组合同文件。   |


查看： [llmware solutions](https://github.com/llmware-ai/llmware/blob/main/solutions/README.md)  

</details>  

<details>
<summary><b>步骤 3 - 教程视频</b></summary>

🎬 观看以下视频快速上手：  
- [文档摘要](https://youtu.be/Ps3W-P9A1m8?si=Rxvst3RJv8ZaOk0L)  
- [Bling-3-GGUF 本地聊天机器人](https://youtu.be/gzzEVK8p3VM?si=8cNn_do0oxSzCEnM)  
- [基于智能体的复杂研究分析](https://youtu.be/y4WvwHqRR60?si=jX3KCrKcYkM95boe)  
- [SLIMs 入门（含代码）](https://youtu.be/aWZFrTDmMPc?si=lmo98_quo_2Hrq0C)  
- [你的 RAG 提示词方式对吗？随机采样 - 第一部分](https://youtu.be/7oMTGhSKuNY?si=_KSjuBnqArvWzYbx)  
- [你的 RAG 提示词方式对吗？随机采样 - 第二部分（代码实验）](https://youtu.be/iXp1tj-pPjM?si=3ZeMgipY0vJDHIMY)  
- [SLIM 模型简介](https://www.youtube.com/watch?v=cQfdaTcmBpY)  
- [Text2SQL 简介](https://youtu.be/BKZ6kO2XxNo?si=tXGt63pvrp_rOlIP)  
- [在笔记本电脑上使用 BLING + RAG](https://www.youtube.com/watch?v=JjgqOZ2v5oU)    
- [DRAGON-7B 模型](https://www.youtube.com/watch?v=d_u7VaKu6Qk&t=37s)  
- [安装并比较使用 Postgres 和 PGVector 的多个嵌入模型](https://www.youtube.com/watch?v=Bncvggy6m5Q)  
- [GGUF 量化背景与 DRAGON 模型示例](https://www.youtube.com/watch?v=ZJyQIZNJ45E)  
- [使用 LM Studio 模型](https://www.youtube.com/watch?v=h2FDjUyvsKE)  
- [使用 Ollama 模型](https://www.youtube.com/watch?v=qITahpVDuV0)  
- [使用任意 GGUF 模型](https://www.youtube.com/watch?v=9wXJgld7Yow)  
- [使用小型 LLM 进行 RAG（合同分析，LLMWare 出品）](https://www.youtube.com/watch?v=8aV5p3tErP0)
- [使用 LLMware 处理发票](https://www.youtube.com/watch?v=VHZSaBBG-Bo&t=10s)
- [大规模摄取 PDF](https://www.youtube.com/watch?v=O0adUfrrxi8&t=10s)
- [使用 LLMWare 评估 RAG 的 LLM](https://www.youtube.com/watch?v=s0KWqYg5Buk&t=105s)
- [LLMWare 开源库 RAG 快速入门](https://www.youtube.com/watch?v=0naqpH93eEU)
- [无数据库使用检索增强生成（RAG）](https://www.youtube.com/watch?v=tAGz6yR14lw)
- [启动 LLMWare 推理服务器](https://www.youtube.com/watch?v=qiEmLnSRDUA&t=20s)


</details>  

## ✍️ 使用 llmware GitHub 仓库

你可以将 llmware 仓库克隆到本地，以访问所有示例或直接使用最新版本的 llmware 代码。  

```bash
git clone git@github.com:llmware-ai/llmware.git
```  

我们在仓库根目录提供了一个 **welcome_to_llmware** 自动化脚本。克隆后：  
- Windows 命令行： `.\welcome_to_llmware_windows.sh`  
- Mac / Linux 命令行： `sh ./welcome_to_llmware.sh`  

或者，如果你偏好不使用欢迎自动化脚本完成设置，请执行以下步骤：  

1. **安装 requirements.txt** - 在 `/llmware` 路径内执行，例如： ```pip3 install -r llmware/requirements.txt```  

2. **安装 requirements_extras.txt** - 在 `/llmware` 路径内执行，例如： ```pip3 install -r llmware/requirements_extras.txt```（根据你的使用场景，你可能不需要全部或任何这些安装，但其中一些将在示例中使用。）

3. **运行示例** - 将所需的 `.py` 示例文件复制到项目根路径。（我们注意到某些 IDE 会尝试从嵌套的 `/example` 路径中交互式运行，从而导致无法访问 `/llmware` 模块。简单的解决方法是将你要运行的示例文件复制到根路径。）  

4. **安装向量数据库（Vector DB）** - 免安装的向量数据库选项包括 milvus lite、chromadb、faiss 和 lancedb，它们不需要服务器安装，但需要安装对应向量数据库的 Python SDK 库，例如 `pip3 install pymilvus` 或 `pip3 install chromadb`。查看 [examples/Embedding](https://github.com/llmware-ai/llmware/tree/main/solutions/embedding)，你将看到各种向量 DB 的入门示例；在仓库根目录，你还将找到用于安装 milvus、postgres/pgvector、mongo、qdrant、neo4j 和 redis 的 docker compose 脚本。  


## 数据存储选项

<details>
<summary><b>快速启动（Fast Start）</b>: 开箱即用 SQLite3 和 ChromaDB（基于文件）- 无需安装 </summary>  

```python
from llmware.configs import LLMWareConfig 
LLMWareConfig().set_active_db("sqlite")   
LLMWareConfig().set_vector_db("chromadb")  
```
</details>  

<details>
<summary><b>速度与扩展（Speed + Scale）</b>: 使用 MongoDB（文本集合）和 Milvus（向量数据库）- 通过 Docker Compose 安装 </summary> 

```bash
curl -o docker-compose.yaml https://raw.githubusercontent.com/llmware-ai/llmware/main/docker-compose.yaml
docker compose up -d
```

```python
from llmware.configs import LLMWareConfig
LLMWareConfig().set_active_db("mongo")
LLMWareConfig().set_vector_db("milvus")
```

</details>  

<details>
<summary><b>Postgres</b>: 使用 Postgres 同时作为文本集合和向量数据库 - 通过 Docker Compose 安装 </summary> 

```bash
curl -o docker-compose.yaml https://raw.githubusercontent.com/llmware-ai/llmware/main/docker-compose-pgvector.yaml
docker compose up -d
```

```python
from llmware.configs import LLMWareConfig
LLMWareConfig().set_active_db("postgres")
LLMWareConfig().set_vector_db("postgres")
```

</details>  

<details>
<summary><b>自由组合（Mix-and-Match）</b>: LLMWare 支持 3 种文本集合数据库（Mongo、Postgres、SQLite）和 
10 种向量数据库（Milvus、PGVector-Postgres、Neo4j、Redis、Mongo-Atlas、Qdrant、Faiss、LanceDB、ChromaDB 和 Pinecone） </summary>

```bash
# 部署其他选项的脚本
curl -o docker-compose.yaml https://raw.githubusercontent.com/llmware-ai/llmware/main/docker-compose-redis-stack.yaml
```

</details>  

## 了解我们的模型   

- **SLIM 模型系列：** 小型、专用模型，专为函数调用和多步骤、多模型智能体工作流微调。  
- **DRAGON 模型系列：** 生产级 RAG 优化的 60亿至 90亿参数模型——“在领先的基础基础模型上交付 RAG”。  
- **BLING 模型系列：** 小型 CPU 优化、RAG 优化、指令遵循的 10亿至 50亿参数模型。  
- **Industry BERT 模型：** 开箱即用的自定义训练句子转换器嵌入模型，针对以下行业微调：保险、合同、资产管理、SEC（美国证券交易委员会）。  
- **GGUF 量化：** 我们为许多 SLIM、DRAGON 和 BLING 模型提供 'gguf' 和 'tool' 版本，针对 CPU 部署进行了优化。  


有兴趣为 llmware 做出贡献？[贡献者指南](https://github.com/llmware-ai/llmware/blob/main/repo_docs/CONTRIBUTING.md#contributing-to-llmware) 提供了参与方式的详细信息。与本项目的所有方面一样，贡献行为受我们的 [行为准则（Code of Conduct）](https://github.com/llmware-ai/llmware/blob/main/repo_docs/CODE_OF_CONDUCT.md) 约束。

欢迎在 [GitHub Discussions](https://github.com/llmware-ai/llmware/discussions) 中提问和讨论。  

## 📣 发布说明与更新日志  

如需完整的发布历史，请查看变更日志标签页。  

**支持的操作系统**: Windows (x86 和 Arm64), MacOS (Metal - M1-M5), Linux (x86, aarch64)    
- Linux - 支持 Ubuntu 20+（glibc 2.31+）   
- 如需其他 Linux 版本的支持，请提交 Issue - 我们将优先进行测试并确保兼容性。    

**支持的向量数据库**: Milvus, Postgres (PGVector), Neo4j, Redis, LanceDB, ChromaDB, Qdrant, FAISS, Pinecone, Mongo Atlas Vector Search

**支持的文本索引数据库**: MongoDB, Postgres, SQLite  


<details>
<summary><b>可选依赖</b></summary>

- [Docker](https://docs.docker.com/get-docker/)
  
- 要启用 OCR 解析功能，请安装 [Tesseract v5.3.3](https://tesseract-ocr.github.io/tessdoc/Installation.html) 和 [Poppler v23.10.0](https://poppler.freedesktop.org/) 原生包。

</details>

<details>
  <summary><b>🚧 更新日志（Change Log）</b></summary>

**1月1日（周四）- v0.4.3 - 开发中 (WIP)**  
 - 更新 `BaseModel` 和 `PromptCatalog` 类 
 - 更新云模型版本，支持 OpenAI、Gemini 和 Anthropic 最新模型   
 - 移除已弃用的模型类 
 - 移除已弃用模块（Dataset Builder 和 Graph）  
 - 其他模型类和卡片更新的开发中工作  
 - 仓库已同步更新，但尚未发布至 pip（目标发布日期：2026年1月第二周）  
   
**3月3日（周一）- v0.4.0**  
 - GGUF 实现、配置和库的更新 
 - ONNXRuntime 实现与配置的更新  
 - ModelCatalog 新增模型，包括 phi-4、Deepseek-Qwen-7B、Deepseek-Qwen-14B 等大量新模型  
 - 增加对 Windows ARM64 的支持  
 - 将默认 `active_db` 更改为 "sqlite"（mongo 和 postgres 仍可用于生产环境）  
 - 精简核心 `requirements.txt` 依赖与 pip 安装流程  
 - 'Extra/可选' 依赖项现可通过 `requirements_extras.txt` 和在 pip install 过程中传入的配置获取（详见 setup.py）
   
**11月8日（周五）- v0.3.9**  
 - 增强 Azure OpenAI 配置，包括流式生成支持  
 - 移除 Linux aarch64 和 Mac x86 的已弃用解析器二进制文件  
 - 为 CustomTable 插入行提供进度反馈的 generator 选项   
   
**10月27日（周日）- v0.3.8**
 - 将包含 100+ OpenVino 和 ONNX 模型的 Model Depot 集合集成至 LLMWare 默认模型目录  
 - 支持模型类、模型目录和模型配置的相关变更   
   
**10月6日（周日）- v0.3.7**  
- 新增 `OVGenerativeModel` 模型类，以支持使用 OpenVino 格式打包的模型  
- 新增 `ONNXGenerativeModel` 模型类，以支持使用 ONNX 格式打包的模型  
- [OpenVino 入门示例](https://github.com/llmware-ai/llmware/blob/main/solutions/openvino/using_openvino_models.py)  
- [ONNX 入门示例](https://github.com/llmware-ai/llmware/blob/main/solutions/onnxruntime/using_onnx_models.py)  
  
**10月1日（周二）- v0.3.6**  
- 新增提示词和聊天模板  
- 改进并更新模型配置    
- 新增用于在搜索结果中定位和高亮文本匹配的实用函数  
- 改进哈希校验实用函数  
  
**8月26日（周一）- v0.3.5**  
- Model Catalog 新增 10 款 BLING+SLIM 模型，涵盖 Qwen2、Phi-3 和 Phi-3.5  
- 在 Qwen-7B、Yi-9B、Mistral-v0.3 和 Llama-3.1 上推出全新 DRAGON 模型  
- 改进 GGUF 配置以扩展上下文窗口  
- 为模型配置添加基准性能数据 
- 增强实用工具哈希函数  

**7月29日（周一）- v03.4**  
- 强化 LLMfx 智能体对 text2sql 数据库读取的安全保护   
- 新增示例 - 参见 [示例](https://github.com/llmware-ai/llmware/blob/main/solutions/ui/dueling_chatbot.py)    
- 更多 Notebook 示例 - 参见 [Notebook 示例](https://github.com/llmware-ai/llmware/blob/main/tutorials/notebooks)      
  
**7月8日（周一）- v03.3**  
- 改进模型配置选项、日志记录及多项小修复  
- 优化 Azure OpenAI 配置 - 参见 [示例](https://github.com/llmware-ai/llmware/blob/main/solutions/models/using-azure-openai.py)  
  
**6月29日（周六）- v0.3.2**  
- PDF 和 Office 解析器更新 - 改进日志记录配置与文本分块选项  
  
**6月22日（周六）- v0.3.1**  
- 快速入门示例系列新增模块 3 [示例 7-9：智能体与函数调用](https://github.com/llmware-ai/llmware/tree/main/fast_start)  
- 为内存中语义相似度 RAG 添加 Jina 重排器模型 - 参见 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/embeddings/using_semantic_reranker_with_rag.py)  
- 增强模型加载过程中的参数化模型获取功能  
- 新增 Pytorch 和 GGUF 版本的 'tiny' 版 slim-extract 和 slim-summary - 查看 'slim-extract-tiny-tool' 与 'slim-summary-tiny-tool'  
- [Biz Bot] 用例 - 参见 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/use_cases/biz_bot.py) 和 [视频](https://youtu.be/4nBYDEjxxTE?si=o6PDPbu0PVcT-tYd)  
- 更新 numpy 依赖至 <2，并更新 yfinance 最低版本 (>=0.2.38)     

**6月4日（周二）- v0.3.0**  
- 新增对 Milvus Lite 嵌入式“免安装”数据库的支持 - 参见 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/embeddings/using_milvus_lite.py)。   
- Model Catalog 和智能体流程新增两款 SLIM 模型：['q-gen'](https://github.com/llmware-ai/llmware/tree/main/solutions/slim_agents/using-slim-q-gen.py) 和 ['qa-gen'](https://github.com/llmware-ai/llmware/tree/main/solutions/slim_agents/using-slim-qa-gen.py)    
- 重构模型类实例化，提供更强的扩展性以在不同模块中添加新类  
- 新增 `welcome_to_llmware.sh` 和 `welcome_to_llmware_windows.sh` 快速安装脚本  
- Model 基类增强，新增可配置的 `post_init` 和 `register` 方法  
- 创建 `InferenceHistory` 以跟踪所有已完成推理的全局状态  
- 模块级日志记录多项改进与更新  
- 注意：自 v0.3.0 起，pip install 提供两种选项 - 基础最小化安装 `pip3 install llmware`（支持大多数使用场景），以及包含其他常用库的大型安装 `pip3 install 'llmware[full]'`。  
  
**5月22日（周三）- v0.2.15**  
- 改进 Model 类对 Pytorch 和 Transformers 依赖的处理（按需即时加载）  

**5月18日（周六）- v0.2.14**  
- 新增 OCR 图像解析方法 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/use_cases/slicing_and_dicing_office_docs.py)  
- 开始添加日志改进功能的第一部分（WIP），涉及 Configs 和 Models。    
- Catalog 新增嵌入模型 - industry-bert-loans。  
- 更新模型导入方法与配置。  

**5月12日（周日）- v0.2.13**  
- 新增 GGUF 流式生成方法 [基础示例](https://github.com/llmware-ai/llmware/tree/main/solutions/gguf/gguf_streaming.py) 和 [phi3 本地聊天机器人](https://github.com/llmware-ai/llmware/tree/main/solutions/ui/gguf_streaming_chatbot.py)  
- 大幅清理辅助导入与依赖以降低安装复杂度 - 注意：已更新的 requirements.txt 和 setup.py。  
- 增加防御性代码，针对 OCR、Web Parser 等特定模块缺失依赖提供明确警告。  
- 更新测试、通知及文档。   
- 新增 `OpenAIConfigs` 以支持 Azure OpenAI。   
  
**5月5日（周日）- v0.2.12 更新**  
- ModelCatalog 上线 ["bling-phi-3"](https://huggingface.co/llmware/bling-phi-3) 和 ["bling-phi-3-gguf"](https://huggingface.co/llmware/bling-phi-3-gguf) - 最新且最准确的 BLING/DRAGON 模型  
- 增加对 Python 3.12 的支持  
- faiss 已弃用，快速入门示例中替换为“免安装”的 chromadb  
- 重构 Datasets、Graph 和 Web Services 类  
- Library 集成 WhisperCPP 语音解析功能  
  
**4月29日（周一）- v0.2.11 更新**  
- 更新 Phi-3 和 Llama-3 的 gguf 库  
- 集成 WhisperCPP Model 类和预编译共享库 - [入门示例](https://github.com/llmware-ai/llmware/tree/main/solutions/gguf/using-whisper-cpp-getting-started.py)  
- 新增语音测试样本文件 - [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/gguf/using-whisper-cpp-sample-files.py)  
- 改进 Windows CUDA 检测及旧版 Mac OS 的安全检查  

**4月22日（周一）- v0.2.10 更新**  
- Agent 类更新，支持对 Postgres 自定义表进行自然语言查询 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/use_cases/agent_with_custom_tables.py)  
- 实现新的智能体 API 端点，结合 LLMWare Inference Server 与新功能 [示例](https://github.com/llmware-ai/llmware/tree/main/solutions/slim_agents/agent_api_endpoint.py)  
  
**4月16日（周二）- v0.2.9 更新**  
- 新增 `CustomTable` 类，快速创建与 LLM 工作流结合的自定义数据库表。  
- 增强将 CSV 和 JSON/JSONL 文件转换为 DB 表的方法。  
- 参见新示例 [创建自定义表示例](https://github.com/llmware-ai/llmware/tree/main/solutions/sources/create_custom_table-1.py)
    
**4月9日（周二）- v0.2.8 更新**  
- Office 解析器（Word Docx、Powerpoint PPTX、Excel XLSX）多项改进 - 新增库 + Python 方法。  
- 包含：多项修复、改进的文本分块控制、标题文本提取与配置选项。  
- 总体而言，新的 Office 解析器选项与新版 PDF 解析器保持一致。  
- 详见 [Office 解析配置示例](https://github.com/llmware-ai/llmware/tree/main/solutions/sources/office_parser_new_configs.py)  

**4月3日（周三）- v0.2.7 更新**  
- PDF 解析器多项改进 - 新增库 + Python 方法。  
- 包含：欧洲语言 UTF-8 编码支持。  
- 包含：更好的文本分块控制、标题文本提取与配置选项。  
- 详见 [PDF 解析配置示例](https://github.com/llmware-ai/llmware/tree/main/solutions/sources/pdf_parser_new_configs.py)。  
- 注意：弃用 aarch64-linux 支持（将使用 0.2.6 解析器）。未来全面支持 x86_64 + CUDA 上的 Ubuntu 20+ Linux。  
  
**3月22日（周五）- v0.2.6 更新**  
- 新增 SLIM 模型：summary, extract, xsum, boolean, tags-3b, 以及组合 sentiment-ner。  
- 新增 logit 和采样分析功能。  
- 展示如何使用新模型的 SLIM 示例。  
  
**3月14日（周四）- v0.2.5 更新**  
- 改进 CUDA (Windows/Linux) 上的 GGUF 支持，提供预编译二进制文件与异常处理。  
- 增强模型配置选项（采样、温度、top logit 捕获）。  
- 全面恢复对 Ubuntu 20+ 的支持，配备解析器与 GGUF 引擎。  
- 支持全新 Anthropic Claude 3 模型。  
- 新增检索方法：document_lookup 和 aggregate_text。  
- 新模型：bling-stablelm-3b-tool - 快速准确的 3B 量化问答模型 - 我们的新宠之一。  

**2月28日（周三）- v0.2.4 更新**  
- GGUF Generative Model 类重大升级 - 支持 Stable-LM-3B、CUDA 构建选项，并更好地控制采样策略。
- 注意：自 v0.2.4 起打包的新版 llama.cpp GGUF 库。  
- 改进 HF Embedding Models 的 GPU 支持。   
  
**2月16日（周五）- v0.2.3 更新**  
- ModelCatalog 新增 10+ 嵌入模型 - nomic, jina, bge, gte, ember 和 uae-large。   
- OpenAI 支持 >=1.0 及新版 text-3 嵌入模型。    
- SLIM 模型的 keys 和 output_values 现可通过 ModelCatalog 访问。  
- 更新编码为 'utf-8-sig'，以更好地处理带 BOM 的 txt/csv 文件。  

**最新更新 - 2024年1月19日 - llmware v0.2.0**
  - 新增数据库集成选项 - Postgres 和 SQlite
  - 改进并行解析的状态更新与解析器事件日志记录选项  
  - 嵌入 + 文本集合数据库间的交互大幅增强  
  - 动态模块加载时的错误异常处理改进

**最新更新 - 2024年1月15日：llmware v0.1.15**
  - 双路检索查询功能增强  
  - 扩展端点资源的配置对象与选项
    
**最新更新 - 2023年12月30日：llmware v0.1.14**
  - 新增对 Open Chat 推理服务器（兼容 OpenAI API）的支持  
  - 改进多嵌入模型和向量数据库配置能力  
  - 新增 PGVector 和 Redis 向量数据库的 docker-compose 安装脚本  
  - Model Catalog 新增 'bling-tiny-llama'
         
**最新更新 - 2023年12月22日：llmware v0.1.13**
  - 新增 3 种向量数据库 - Postgres (PG Vector), Redis, 和 Qdrant  
  - 改进直接在模型目录中集成句子转换器的支持  
  - 模型目录属性优化  
  - Models & Embeddings 多项新示例，涵盖 GGUF、向量数据库及模型目录

- **2023年12月17日：llmware v0.1.12**
  - Catalog 新增 dragon-deci-7b - 基于 Deci 高性能 7B 基础模型的 RAG 微调模型  
  - 新增 GGUFGenerativeModel 类，便于集成 GGUF 模型  
  - 为 Mac M1, Mac x86, Linux x86 和 Windows 添加预编译 llama_cpp / ctransformer 共享库  
  - 3 款 DRAGON 模型打包为 Q4_K_M GGUF 格式供 CPU 笔记本使用 (dragon-mistral-7b, dragon-llama-7b, dragon-yi-6b)
  - 默认目录新增 4 款主流开源聊天模型，配备 Q4_K_M
  
- **2023年12月8日：llmware v0.1.11**
  - 新增 Milvus 高容量文档摄取与嵌入的快速入门示例。
  - 全新 LLMWare 'Pop up' Inference Server 模型类及示例脚本。
  - RAG 发票处理新示例。
  - 改进 Windows 栈管理以支持解析大型文档。
  - 增强 PDF 和 Office 解析器的调试日志输出模式选项。

- **2023年11月30日：llmware v0.1.10**
  - Windows 正式成为受支持的操作系统。
  - 进一步改进原生栈管理代码。 
  - 多项缺陷修复。

- **2023年11月24日：llmware v0.1.9**
  - Markdown (.md) 文件现被解析并视为文本文件处理。
  - PDF 和 Office 解析器栈优化，避免设置 ulimit -s 的需求。
  - 新增 llmware_models_fast_start.py 示例，支持发现与选择所有 llmware HuggingFace 模型。
  - 原生依赖（共享库及依赖项）现包含在仓库中，便于本地开发。
  - Status 类更新以支持 PDF 和 Office 文档解析状态更新。
  - 多项缺陷修复，包括库导出中的图像块处理。

- **2023年11月17日：llmware v0.1.8**
  - 通过允许每个模型指定尾随空格参数提升生成性能。
  - 改进 llama2 和 mistral 的 eos_token_id 处理。
  - 改进对 Hugging Face 动态加载的支持
  - 新增结合全新 llmware DRAGON 模型的示例。
    
- **2023年11月14日：llmware v0.1.7**
  - 转向 Python Wheel 包格式用于 PyPi 分发，以在所有支持平台上无缝安装原生依赖。  
  - ModelCatalog 增强功能:
    - OpenAI 更新包含新公布的 'turbo' 4 和 3.5 模型。
    - Cohere embedding v3 更新包含全新 Cohere 嵌入模型。
    - BLING 模型作为开箱即用的注册选项加入目录。可像其他模型一样实例化，即使不设置 "hf=True" 标志。
    - ModelCatalog 的 register 方法现支持在现有模型类中注册新模型名称。
  - Prompt 增强功能:
    - prompt_main 输出字典新增 “evidence_metadata”，使响应可直接接入证据和事实核查步骤而无需修改。
    - API Key 现在可通过 `prompt.load_model(model_name, api_key="[my-api-key]")` 直接传入
  - LLMWareInference Server - 初始交付:
    - 全新 LLMWareModel 类，作为自定义 HF 风格 API 模型的包装器。    
    - LLMWareInferenceServer 是新类，可在远程 (GPU) 服务器上实例化以创建测试 API 服务器，无缝集成至任何 Prompt 工作流。    
 
- **2023年11月3日：llmware v0.1.6**
  - 更新打包要求 mongo-c-driver 1.24.4 以临时规避 mongo-c-driver 1.25 的段错误问题。
  - Python 代码更新，为未来 Windows 支持做准备。  

- **2023年10月27日：llmware v0.1.5**
  - 四个聚焦 RAG 工作流的新示例脚本，使用可在笔记本上运行的小型微调指令模型（`llmware` [BLING](https://huggingface.co/llmware) 模型）。
  - 扩展 Prompt 类内设置温度的选项。
  - 改进 Hugging Face 模型生成的后处理流程。
  - 简化 Hugging Face 生成模型加载至 Prompt 的流程。
  - 初始交付中央 Status 类：提供一致的调用者接口读写嵌入状态。
  - 增强内存字典多键查询支持。
  - 移除人机对话包装中的尾随空格，以改善部分微调模型的生成质量。
  - 多项缺陷修复、测试脚本更新及 Werkzeug 版本升级以解决 [依赖安全告警](https://github.com/llmware-ai/llmware/security/dependabot/2)。
- **2023年10月20日：llmware v0.1.4**
  - Hugging Face 模型 GPU 支持。
  - 缺陷修复及额外测试脚本。
- **2023年10月13日：llmware v0.1.3**
  - MongoDB Atlas Vector Search 支持。
  - 支持使用 MongoDB 连接字符串进行身份验证。
  - 文档摘要方法。
  - 自动捕获模型上下文窗口并传递预期输出长度变更的改进。  
  - Dataset 卡片及按名称查找的描述功能。
  - 模型推理使用字典新增处理时间统计。
  - 额外测试脚本、示例及缺陷修复。
- **2023年10月6日：llmware v0.1.1**
  - GitHub 仓库新增回归测试脚本。
  - 多项缺陷修复及 Pillow 版本升级以解决 [依赖安全告警](https://github.com/llmware-ai/llmware/security/dependabot/1)。
- **2023年10月2日：llmware v0.1.0** 🔥 llmware 正式开源发布！！ 🔥


</details>
<p align="centre">
  <a href="#top">⬆️ 回到顶部</a>
</p>

## 🤓 阅读我们的白皮书

- **革新 AI 部署：借助 Intel AI PC 与 LLMWare Model HQ 释放 AI 加速能力** [AI PC Model HQ.pdf](https://github.com/user-attachments/files/18024139/AI.PC.Model.HQ.pdf)
- **革新 AI 部署（Intel 摘要版）**  [LNL White paper (Abstract Version) final.pdf](https://github.com/user-attachments/files/18281644/LNL.White.paper.Abstract.Version.final.pdf)

- **加速 AI PC 驱动的 AI 生产力** [Laptop.Performance.WP.Final (10).pdf](https://github.com/user-attachments/files/18024294/Laptop.Performance.WP.Final.10.pdf)

## Intel 联合解决方案

- **Arrow Lake** 
[IPA.Optimization.Summary.LLMWare (1).pdf](https://github.com/user-attachments/files/18292873/IPA.Optimization.Summary.LLMWare.1.pdf)

## 关于 Model HQ
  - **隐私政策** [AI.BLOKS.PRIVACY.POLICY.1.3.25.pdf](https://github.com/user-attachments/files/19289355/AI.BLOKS.PRIVACY.POLICY.1.3.25.pdf)

- **服务条款** [AI.Bloks.Terms.of.Service.3.3.25.pdf](https://github.com/user-attachments/files/19289545/AI.Bloks.Terms.of.Service.3.3.25.pdf)

- **可接受使用政策**[Model HQ 可接受使用政策 by AI BLOKS LLC.docx](https://github.com/user-attachments/files/18291481/Acceptable.Use.Policy.for.Model.HQ.by.AI.BLOKS.LLC.docx)