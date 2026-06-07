<!-- HEADER:START -->
<img width="2000" height="524" alt="Social Cover (9)"
     src="https://github.com/user-attachments/assets/cf66f045-c8be-494b-b696-b8d7e4fb709c" />
<!-- HEADER:END -->

<div style="height: 16px;"></div>

<p align="center">
    <a href="https://trendshift.io/repositories/17293" target="_blank"><img src="https://trendshift.io/api/badge/repositories/17293" alt="memvid%2Fmemvid | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>
<!-- BADGES:END -->

<p align="center">
  <strong>Memvid 是一个专为 AI Agent 设计的单文件记忆层，支持即时检索与长期记忆。</strong><br/>
  持久化、版本控制且可移植的记忆系统，无需数据库。
</p>

<!-- NAV:START -->
<p align="center">
  <a href="https://www.memvid.com">网站</a>
  ·
  <a href="https://sandbox.memvid.com">试用沙盒</a>
  ·
  <a href="https://docs.memvid.com">文档</a>
  ·
  <a href="https://github.com/memvid/memvid/discussions">讨论区</a>
</p>
<!-- NAV:END -->

<!-- BADGES:START -->
<p align="center">
  <a href="https://crates.io/crates/memvid-core"><img src="https://img.shields.io/crates/v/memvid-core?style=flat-square&logo=rust" alt="Crates.io" /></a>
  <a href="https://docs.rs/memvid-core"><img src="https://img.shields.io/docsrs/memvid-core?style=flat-square&logo=docs.rs" alt="docs.rs" /></a>
  <a href="https://github.com/memvid/memvid/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square" alt="License" /></a>
</p>

<p align="center">
  <a href="https://github.com/memvid/memvid/stargazers"><img src="https://img.shields.io/github/stars/memvid/memvid?style=flat-square&logo=github" alt="Stars" /></a>
  <a href="https://github.com/memvid/memvid/network/members"><img src="https://img.shields.io/github/forks/memvid/memvid?style=flat-square&logo=github" alt="Forks" /></a>
  <a href="https://github.com/memvid/memvid/issues"><img src="https://img.shields.io/github/issues/memvid/memvid?style=flat-square&logo=github" alt="Issues" /></a>
  <a href="https://discord.gg/2mynS7fcK7"><img src="https://img.shields.io/discord/1442910055233224745?style=flat-square&logo=discord&label=discord" alt="Discord" /></a>
</p>


## 基准测试亮点

**🚀 准确率超越所有其他记忆系统：** LoCoMo 基准测试 SOTA +35%，最佳长程对话回忆与推理能力

**🧠 卓越的多跳与时序推理能力：** 多跳推理提升 +76%，时序推理提升 +56%（对比行业平均水平）

**⚡ 超高吞吐量下的极低延迟：** P50 为 0.025ms，P99 为 0.075ms，吞吐量比标准方案高出 1,372 倍

**🔬 完全可复现的基准测试：** LoCoMo（10 × ~26K token 对话）、开源评估、LLM-as-Judge


## Memvid 是什么？

Memvid 是一个可移植的 AI 记忆系统，将你的数据、向量嵌入（embeddings）、搜索结构和元数据打包为单个文件。

无需运行复杂的 RAG（检索增强生成）管道或基于服务器的向量数据库，Memvid 可直接从文件中实现快速检索。

其结果是一个与模型无关、零基础设施依赖的记忆层，赋予 AI Agent 持久化且可随身携带的长期记忆。


## 什么是智能帧（Smart Frames）？

Memvid 借鉴了视频编码的理念——并非用于存储视频，而是将 **AI 记忆组织为一种仅追加（append-only）、超高效的“智能帧”序列。**

一个智能帧是不可变的数据单元，用于存储内容及其时间戳、校验和和基本元数据。这些帧以允许高效压缩、索引和并行读取的方式进行分组。

这种基于帧的设计带来了以下优势：
- 仅追加写入，无需修改或破坏现有数据
- 支持对历史记忆状态的查询
- 像时间线一样直观地查看知识的演变过程
- 通过已提交且不可变的帧实现崩溃安全（Crash safety）
- 采用源自视频编码的技术进行高效压缩

最终结果是一个单文件，其行为类似于 AI 系统可回溯的记忆时间轴。


## 核心概念

-   **活跃记忆引擎 (Living Memory Engine)**
    跨会话持续追加、分支并演进记忆数据。

-   **胶囊上下文 (Capsule Context, `.mv2`)**
    自包含且可共享的记忆胶囊，支持规则配置与过期机制。

-   **时光回溯调试 (Time-Travel Debugging)**
    可回滚、重放或分支任意记忆状态。

-   **智能召回 (Smart Recall)**
    结合预测缓存技术，实现亚 5ms 的本地记忆访问速度。

-   **编解码智能 (Codec Intelligence)**
    自动选择并随时间推移升级压缩算法。


## 应用场景

Memvid 是一个可移植、无服务器的记忆层，为 AI Agent 提供持久化记忆与快速召回能力。由于其模型无关性、多模态支持及完全离线运行的特性，开发者正将其广泛应用于各类真实场景：

-   长期运行的 AI Agent
-   企业知识库
-   优先离线的 AI 系统
-   代码库理解与分析
-   客户支持机器人
-   工作流自动化
-   销售与营销 Copilot
-   个人知识助手
-   医疗、法律与金融领域的专业 Agent
-   可审计且支持调试的 AI 工作流
-   自定义应用开发


## SDK & CLI

使用你偏好的语言集成 Memvid：

| Package         | Install                     | Links                                                                                                               |
| --------------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **CLI**         | `npm install -g memvid-cli` | [![npm](https://img.shields.io/npm/v/memvid-cli?style=flat-square)](https://www.npmjs.com/package/memvid-cli)       |
| **Node.js SDK** | `npm install @memvid/sdk`   | [![npm](https://img.shields.io/npm/v/@memvid/sdk?style=flat-square)](https://www.npmjs.com/package/@memvid/sdk)     |
| **Python SDK**  | `pip install memvid-sdk`    | [![PyPI](https://img.shields.io/pypi/v/memvid-sdk?style=flat-square)](https://pypi.org/project/memvid-sdk/)         |
| **Rust**        | `cargo add memvid-core`     | [![Crates.io](https://img.shields.io/crates/v/memvid-core?style=flat-square)](https://crates.io/crates/memvid-core) |

---

## 安装（Rust）

### 环境要求

-   **Rust 1.85.0+** — 请前往 [rustup.rs](https://rustup.rs) 安装

### 添加到项目

```toml
[dependencies]
memvid-core = "2.0"
```

### Feature Flags（特性开关）

| Feature             | Description                                                      |
| ------------------- | ---------------------------------------------------------------- |
| `lex`               | 基于 BM25 评分的全局全文搜索（Tantivy）                     |
| `pdf_extract`       | 纯 Rust 实现的 PDF 文本提取                                    |
| `vec`               | 向量相似度搜索（HNSW + 通过 ONNX 进行的本地文本嵌入） |
| `clip`              | 用于图像搜索的 CLIP 视觉嵌入                          |
| `whisper`           | 基于 Whisper 的音频转录                                 |
| `api_embed`         | 云端 API 嵌入（OpenAI）                                    |
| `temporal_track`    | 自然语言日期解析（如“上周二”）                   |
| `parallel_segments` | 多线程数据摄入                                         |
| `encryption`        | 基于密码的加密胶囊 (.mv2e)                       |
| `symspell_cleanup`  | 鲁棒的 PDF 文本修复（修正 "emp lo yee" -> "employee"）        |

按需启用相关特性：

```toml
[dependencies]
memvid-core = { version = "2.0", features = ["lex", "vec", "temporal_track"] }
```


## 快速开始

```rust
use memvid_core::{Memvid, PutOptions, SearchRequest};

fn main() -> memvid_core::Result<()> {
    // Create a new memory file
    let mut mem = Memvid::create("knowledge.mv2")?;

    // Add documents with metadata
    let opts = PutOptions::builder()
        .title("Meeting Notes")
        .uri("mv2://meetings/2024-01-15")
        .tag("project", "alpha")
        .build();
    mem.put_bytes_with_options(b"Q4 planning discussion...", opts)?;
    mem.commit()?;

    // Search
    let response = mem.search(SearchRequest {
        query: "planning".into(),
        top_k: 10,
        snippet_chars: 200,
        ..Default::default()
    })?;

    for hit in response.hits {
        println!("{}: {}", hit.title.unwrap_or_default(), hit.text);
    }

    Ok(())
}
```

---

## 构建项目

克隆仓库：

```bash
git clone https://github.com/memvid/memvid.git
cd memvid
```

以调试模式构建：

```bash
cargo build
```

以发布模式（优化）构建：

```bash
cargo build --release
```

构建指定特性版本：

```bash
cargo build --release --features "lex,vec,temporal_track"
```

---

## 运行测试

运行全部测试：

```bash
cargo test
```

带输出信息运行测试：

```bash
cargo test -- --nocapture
```

运行特定测试：

```bash
cargo test test_name
```

仅运行集成测试：

```bash
cargo test --test lifecycle
cargo test --test search
cargo test --test mutation
```

---

## 示例

`examples/` 目录中包含可运行的示例代码：

### 基础用法

演示创建、写入、搜索及时间线操作：

```bash
cargo run --example basic_usage
```

### PDF 数据摄入

导入并搜索 PDF 文档（使用《Attention Is All You Need》论文）：

```bash
cargo run --example pdf_ingestion
```

### CLIP 视觉搜索

使用 CLIP 嵌入进行图像搜索（需启用 `clip` 特性）：

```bash
cargo run --example clip_visual_search --features clip
```

### Whisper 音频转录

音频转写功能（需启用 `whisper` 特性）：

```bash
cargo run --example test_whisper --features whisper -- /path/to/audio.mp3
```

**可用模型：**

| Model                 | Size   | Speed   | Use Case                            |
| --------------------- | ------ | ------- | ----------------------------------- |
| `whisper-small-en`    | 244 MB | Slowest | Best accuracy (default)             |
| `whisper-tiny-en`     | 75 MB  | Fast    | Balanced                            |
| `whisper-tiny-en-q8k` | 19 MB  | Fastest | Quick testing, resource-constrained |

**模型选择：**

```bash
# Default (FP32 small, highest accuracy)
cargo run --example test_whisper --features whisper -- audio.mp3

# Quantized tiny (75% smaller, faster)
MEMVID_WHISPER_MODEL=whisper-tiny-en-q8k cargo run --example test_whisper --features whisper -- audio.mp3
```

**编程配置：**

```rust
use memvid_core::{WhisperConfig, WhisperTranscriber};

// Default FP32 small model
let config = WhisperConfig::default();

// Quantized tiny model (faster, smaller)
let config = WhisperConfig::with_quantization();

// Specific model
let config = WhisperConfig::with_model("whisper-tiny-en-q8k");

let transcriber = WhisperTranscriber::new(&config)?;
let result = transcriber.transcribe_file("audio.mp3")?;
println!("{}", result.text);
```


## 文本嵌入模型

`vec` 特性支持使用 ONNX 模型的本地文本嵌入。在使用前，你需要手动下载模型文件。

### 快速开始：BGE-small（推荐）

下载默认的 BGE-small 模型（384 维，速度快且高效）：

```bash
mkdir -p ~/.cache/memvid/text-models

# Download ONNX model
curl -L 'https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/onnx/model.onnx' \
  -o ~/.cache/memvid/text-models/bge-small-en-v1.5.onnx

# Download tokenizer
curl -L 'https://huggingface.co/BAAI/bge-small-en-v1.5/resolve/main/tokenizer.json' \
  -o ~/.cache/memvid/text-models/bge-small-en-v1.5_tokenizer.json
```

### 可用模型

| Model                   | Dimensions | Size   | Best For        |
| ----------------------- | ---------- | ------ | --------------- |
| `bge-small-en-v1.5`     | 384        | ~120MB | Default, fast   |
| `bge-base-en-v1.5`      | 768        | ~420MB | Better quality  |
| `nomic-embed-text-v1.5` | 768        | ~530MB | Versatile tasks |
| `gte-large`             | 1024       | ~1.3GB | Highest quality |

### 其他模型

**BGE-base**（768 维）：
```bash
curl -L 'https://huggingface.co/BAAI/bge-base-en-v1.5/resolve/main/onnx/model.onnx' \
  -o ~/.cache/memvid/text-models/bge-base-en-v1.5.onnx
curl -L 'https://huggingface.co/BAAI/bge-base-en-v1.5/resolve/main/tokenizer.json' \
  -o ~/.cache/memvid/text-models/bge-base-en-v1.5_tokenizer.json
```

**Nomic**（768 维）：
```bash
curl -L 'https://huggingface.co/nomic-ai/nomic-embed-text-v1.5/resolve/main/onnx/model.onnx' \
  -o ~/.cache/memvid/text-models/nomic-embed-text-v1.5.onnx
curl -L 'https://huggingface.co/nomic-ai/nomic-embed-text-v1.5/resolve/main/tokenizer.json' \
  -o ~/.cache/memvid/text-models/nomic-embed-text-v1.5_tokenizer.json
```

**GTE-large**（1024 维）：
```bash
curl -L 'https://huggingface.co/thenlper/gte-large/resolve/main/onnx/model.onnx' \
  -o ~/.cache/memvid/text-models/gte-large.onnx
curl -L 'https://huggingface.co/thenlper/gte-large/resolve/main/tokenizer.json' \
  -o ~/.cache/memvid/text-models/gte-large_tokenizer.json
```

### 代码中的使用

```rust
use memvid_core::text_embed::{LocalTextEmbedder, TextEmbedConfig};
use memvid_core::types::embedding::EmbeddingProvider;

// Use default model (BGE-small)
let config = TextEmbedConfig::default();
let embedder = LocalTextEmbedder::new(config)?;

let embedding = embedder.embed_text("hello world")?;
assert_eq!(embedding.len(), 384);

// Use different model
let config = TextEmbedConfig::bge_base();
let embedder = LocalTextEmbedder::new(config)?;
```

完整示例（包含相似度计算与搜索排序）请参阅 `examples/text_embedding.rs`。

### 模型一致性

为防止意外混用模型（例如：使用 OpenAI 嵌入查询 BGE-small 索引），你可以显式地将 Memvid 实例绑定到特定模型名称：

```rust
// Bind the index to a specific model.
// If the index was previously created with a different model, this will return an error.
mem.set_vec_model("bge-small-en-v1.5")?;
```

该绑定是持久化的。一旦设置，未来尝试使用不同模型名称的操作将快速失败并返回 `ModelMismatch` 错误。



## API 嵌入（OpenAI）

`api_embed` 特性支持通过 OpenAI API 生成云端嵌入。

### 环境配置

设置你的 OpenAI API Key：

```bash
export OPENAI_API_KEY="sk-..."
```

### 代码使用

```rust
use memvid_core::api_embed::{OpenAIConfig, OpenAIEmbedder};
use memvid_core::types::embedding::EmbeddingProvider;

// Use default model (text-embedding-3-small)
let config = OpenAIConfig::default();
let embedder = OpenAIEmbedder::new(config)?;

let embedding = embedder.embed_text("hello world")?;
assert_eq!(embedding.len(), 1536);

// Use higher quality model
let config = OpenAIConfig::large();  // text-embedding-3-large (3072 dims)
let embedder = OpenAIEmbedder::new(config)?;
```

### 可用模型

| Model                    | Dimensions | Best For                   |
| ------------------------ | ---------- | -------------------------- |
| `text-embedding-3-small` | 1536       | Default, fastest, cheapest |
| `text-embedding-3-large` | 3072       | Highest quality            |
| `text-embedding-ada-002` | 1536       | Legacy model               |

完整示例请参阅 `examples/openai_embedding.rs`。



## 文件格式

所有数据均存储于单个 `.mv2` 文件中：

```
┌────────────────────────────┐
│ Header (4KB)               │  Magic, version, capacity
├────────────────────────────┤
│ Embedded WAL (1-64MB)      │  Crash recovery
├────────────────────────────┤
│ Data Segments              │  Compressed frames
├────────────────────────────┤
│ Lex Index                  │  Tantivy full-text
├────────────────────────────┤
│ Vec Index                  │  HNSW vectors
├────────────────────────────┤
│ Time Index                 │  Chronological ordering
├────────────────────────────┤
│ TOC (Footer)               │  Segment offsets
└────────────────────────────┘
```

无需生成 `.wal`、`.lock`、`.shm` 或任何外部辅助文件。始终如此。

完整文件格式规范请参阅 [MV2_SPEC.md](MV2_SPEC.md)。



## 支持

有问题或反馈？
Email: contact@memvid.com

**如果觉得好用，欢迎点个 ⭐ 支持！**

---

> **Memvid v1（基于 QR 码的记忆）已弃用**
>
> 如果你正在参考 QR 码相关内容，说明你使用的是过时信息。
>
> 请参阅：https://docs.memvid.com/memvid-v1-deprecation

---

## 许可证

采用 Apache License 2.0 开源协议 —— 详见 [LICENSE](LICENSE) 文件。