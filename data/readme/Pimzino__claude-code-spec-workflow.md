# Claude Code Spec Workflow

> **⚠️ IMPORTANT NOTICE:** Development focus has shifted to the **MCP (Model Context Protocol) version** of this workflow system. The MCP version provides enhanced features, real-time dashboard, and broader AI tool compatibility.
> 
> **🚀 [View the new Spec Workflow MCP →](https://github.com/Pimzino/spec-workflow-mcp)**
>
> This Claude Code-specific version remains available for existing users but will receive limited updates.

[![npm version](https://badge.fury.io/js/@pimzino%2Fclaude-code-spec-workflow.svg?cacheSeconds=300)](https://badge.fury.io/js/@pimzino%2Fclaude-code-spec-workflow)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Automated workflows for Claude Code with intelligent task execution.**

Transform your development with structured workflows: **Requirements → Design → Tasks → Implementation** for new features, plus streamlined **Report → Analyze → Fix → Verify** for bug fixes.

## ☕ Support This Project

<a href="https://buymeacoffee.com/Pimzino" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

## 📦 Installation

1. Install the workflow globally
```bash
npm i -g @pimzino/claude-code-spec-workflow
```
2. Run the setup command in your project directory
```bash
claude-code-spec-workflow
```
**Thats it, you are ready to go!**
---

## ✨ What You Get

- **📁 Complete .claude/ structure** - All files and directories
- **📝 10 slash commands** - 5 spec workflow + 5 bug fix workflow
- **🎯 Intelligent task execution** - Automated implementation
- **🤖 4 specialized agents** - Enhanced automation
- **📊 Real-time dashboard** - Monitor progress visually
- **🔧 Auto-generated commands** - One command per task
- **📋 Document templates** - Professional spec documents
- **⚙️ Project steering** - Persistent context and standards
- **⚡ Smart optimization** - Intelligent context sharing and caching

---

## 🔄 Workflows Overview

### 📊 **Spec Workflow** (New Features)

**Complete automation in one command:**

```bash
/spec-create feature-name "Description"
```

**What happens:**
1. **Requirements** → User stories + acceptance criteria
2. **Design** → Technical architecture + diagrams
3. **Tasks** → Atomic, agent-friendly breakdown
4. **Commands** → Auto-generated task commands (optional)

**Execute tasks:**
```bash
# Manual control
/spec-execute 1 feature-name
/feature-name-task-1        # Auto-generated
```

### 🐛 **Bug Fix Workflow** (Quick Fixes)

```bash
/bug-create issue-name "Description"  # Document the bug
/bug-analyze                          # Find root cause
/bug-fix                             # Implement solution
/bug-verify                          # Confirm resolution
```

### 🎯 **Steering Setup** (Project Context)

```bash
/spec-steering-setup  # Creates product.md, tech.md, structure.md
```

---

## 🛠️ Commands Reference

<details>
<summary><strong>📊 Spec Workflow Commands</strong></summary>

| Command | Purpose |
|---------|---------|
| `/spec-steering-setup` | Create project context documents |
| `/spec-create <name>` | Complete spec workflow |
| `/spec-execute <task-id>` | Manual task execution |
| `/<name>-task-<id>` | Auto-generated task commands |
| `/spec-status` | Show progress |
| `/spec-list` | List all specs |

</details>

<details>
<summary><strong>🐛 Bug Fix Commands</strong></summary>

| Command | Purpose |
|---------|---------|
| `/bug-create <name>` | Document bug with structured format |
| `/bug-analyze` | Investigate root cause |
| `/bug-fix` | Implement targeted solution |
| `/bug-verify` | Verify resolution |
| `/bug-status` | Show bug fix progress |

</details>

---

## 🎯 Key Features

### 🤖 **Intelligent Task Execution**
- **Streamlined** task implementation
- **Context-aware** execution with full specification context
- **Agent-based** implementation with spec-task-executor

### 🧠 **Specialized Agents** (Optional)
4 AI agents for enhanced automation:

**Core Workflow:** `spec-task-executor`, `spec-requirements-validator`, `spec-design-validator`, `spec-task-validator`


> **Note:** Agents are optional - everything works with built-in fallbacks.

### ⚡ **Complete Context Optimization** (NEW!)
- **Universal context sharing** - Steering, specification, AND template documents optimized
- **60-80% token reduction** - Eliminates redundant document fetching across all document types
- **Triple optimization commands** - `get-steering-context`, `get-spec-context`, and `get-template-context`
- **Smart document handling** - Bug documents use direct reading (no redundancy), templates use bulk loading (high redundancy)
- **Improved performance** - Faster agent execution with cached context across all workflows
- **Automatic fallback** - Maintains reliability with individual `get-content` when optimization unavailable
- **Session-based caching** - Intelligent file change detection and cache invalidation

### 📊 **Real-Time Dashboard**
```bash
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard
```
- Live progress tracking
- WebSocket updates
- Git integration
- Modern UI with Tailwind CSS

---

### 🔗 Dashboard Tunnel (NEW!)

Share your dashboard securely with external stakeholders through temporary HTTPS URLs:

```bash
# Start dashboard with tunnel
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard --tunnel

# With password protection
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard --tunnel --tunnel-password mySecret123

# Choose specific provider
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard --tunnel --tunnel-provider cloudflare
```

**Tunnel Features:**
- **🔒 Secure HTTPS URLs** - Share dashboard with managers, clients, or remote team members
- **👁️ Read-Only Access** - External viewers cannot modify any project data
- **🔑 Optional Password** - Protect access with password authentication
- **🌐 Multiple Providers** - Automatic fallback between Cloudflare and ngrok
- **📊 Usage Analytics** - Track who accessed your dashboard and when
- **⏰ Auto-Expiration** - Tunnels close when you stop the dashboard
- **🚀 Zero Configuration** - Works out of the box with built-in providers

## 📊 Command Line Options

### Setup Commands
```bash
# Setup in current directory
npx @pimzino/claude-code-spec-workflow

# Setup in specific directory
npx @pimzino/claude-code-spec-workflow --project /path/to/project

# Force overwrite existing files
npx @pimzino/claude-code-spec-workflow --force

# Skip confirmation prompts
npx @pimzino/claude-code-spec-workflow --yes

# Test the setup
npx @pimzino/claude-code-spec-workflow test
```

### Dashboard Commands
```bash
# Basic dashboard
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard

# Dashboard with tunnel (share externally)
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard --tunnel

# Full tunnel configuration
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard \
  --tunnel \
  --tunnel-password mySecret123 \
  --tunnel-provider cloudflare \
  --port 3000 \
  --open
```

## 🎯 Steering Documents (NEW!)

Steering documents provide persistent project context that guides all spec development:

### **Product Document** (`product.md`)
- Product vision and purpose
- Target users and their needs
- Key features and objectives
- Success metrics

### **Technology Document** (`tech.md`)
- Technology stack and frameworks
- Development tools and practices
- Technical constraints and requirements
- Third-party integrations

### **Structure Document** (`structure.md`)
- File organization patterns
- Naming conventions
- Import patterns
- Code organization principles

Run `/spec-steering-setup` to create these documents. Claude will analyze your project and help you define these standards.

## 🎨 Features

### ✅ **Zero Configuration**
- Works out of the box with any project
- Auto-detects project type (Node.js, Python, Java, etc.)
- Validates Claude Code installation

### ✅ **Interactive Setup**
- Beautiful CLI with progress indicators
- Confirmation prompts for safety
- Helpful error messages and guidance

### ✅ **Smart File Management**
- Complete workflow instructions in each command file
- Creates comprehensive directory structure
- Includes all necessary templates and configs

### ✅ **Professional Quality**
- **Full TypeScript implementation** with strict type checking
- **Frontend converted to TypeScript** for enhanced dashboard development
- **95%+ type coverage** with no implicit any types
- **Modern build pipeline** with esbuild bundling and source maps
- Comprehensive error handling
- Follows npm best practices

### ✅ **Steering Document Integration**
- Persistent project context across all specs
- Automatic alignment with project standards
- Consistent code generation
- Reduced need for repetitive explanations

### ✅ **TypeScript Dashboard Frontend**
- **Type-safe frontend code** with comprehensive interfaces
- **Real-time WebSocket communication** with typed message handling
- **Petite-vue integration** with custom type definitions
- **Build pipeline** supporting development and production bundles
- **Strict null checking** and modern TypeScript patterns
- **JSDoc documentation** for all exported functions

## 🏗️ Project Structure After Setup

```
your-project/
├── .claude/
│   ├── commands/           # 14 slash commands + auto-generated
│   ├── steering/          # product.md, tech.md, structure.md
│   ├── templates/         # Document templates
│   ├── specs/            # Generated specifications
│   ├── bugs/             # Bug fix workflows
│   └── agents/           # AI agents (enabled by default)
```

## 🧪 Testing

The package includes a built-in test command:

```bash
# Test setup in temporary directory
npx @pimzino/claude-code-spec-workflow test
```

## 📋 Requirements

- **Node.js** 16.0.0 or higher
- **Claude Code** installed and configured
- Any project directory

## 🔧 Troubleshooting

### Common Issues

**❓ Command not found after NPX**
```bash
# Make sure you're using the correct package name
npx @pimzino/claude-code-spec-workflow
```

**❓ Setup fails with permission errors**
```bash
# Try with different directory permissions
npx @pimzino/claude-code-spec-workflow --project ~/my-project
```

**❓ Claude Code not detected**
```bash
# Install Claude Code first
npm install -g @anthropic-ai/claude-code
```

### Debug Information

```bash
# Show verbose output
DEBUG=* npx @pimzino/claude-code-spec-workflow

# Check package version
npx @pimzino/claude-code-spec-workflow --version
```

## 🌟 Examples

### Basic Usage
```bash
cd my-awesome-project
npx @pimzino/claude-code-spec-workflow
claude
# Type: /spec-create user-dashboard "User profile management"
```

### Advanced Usage
```bash
# Setup multiple projects
for dir in project1 project2 project3; do
  npx @pimzino/claude-code-spec-workflow --project $dir --yes
done
```

## 🔧 TypeScript Development

### Frontend Dashboard Development

The dashboard frontend is fully implemented in TypeScript for enhanced type safety and developer experience:

#### Type Definitions
```typescript
// Core dashboard types
interface Project {
  path: string;
  name: string;
  level: number;
  hasActiveSession: boolean;
  specs: Spec[];
  bugs: Bug[];
  steeringStatus?: SteeringStatus;
}

// WebSocket message types with discriminated unions
type WebSocketMessage = 
  | { type: 'initial'; data: InitialData }
  | { type: 'update'; data: UpdateData }
  | { type: 'error'; data: ErrorData }
  | { type: 'tunnel-status'; data: TunnelStatusData };
```

#### Build Commands
```bash
# TypeScript compilation and bundling
npm run build:frontend:dev   # Build frontend for development
npm run build:frontend:prod  # Build frontend for production (minified)
npm run watch:frontend       # Watch mode with auto-rebuild
npm run typecheck:frontend   # Type checking only (no output)
npm run typecheck           # Check both backend and frontend types

# Development workflow  
npm run dev:dashboard       # Start dashboard with hot reload (frontend + backend)
npm run dev:dashboard:backend-only  # Start only backend (for frontend debugging)

# Full build process
npm run build              # Complete build: TypeScript + frontend + static files
npm run lint               # Lint TypeScript files with auto-fix
npm run format             # Format code with Prettier
```

#### Type Safety Features
- **Strict TypeScript configuration** with null checks
- **Runtime type validation** with type guards
- **WebSocket message typing** for real-time updates  
- **State management types** for reactive UI components
- **Error handling types** with Result<T> pattern
- **Petite-vue integration** with custom type definitions

#### Type Usage Examples

```typescript
// Import dashboard types
import type { Project, WebSocketMessage, AppState } from './dashboard.types';

// Type-safe project handling
function selectProject(project: Project): void {
  console.log(`Selected: ${project.name} (${project.specs.length} specs)`);
  
  // Safe property access with optional chaining
  const steeringCount = project.steeringStatus?.totalDocs ?? 0;
  if (steeringCount > 0) {
    console.log(`Steering docs: ${steeringCount}`);
  }
}

// WebSocket message handling with discriminated unions
function handleMessage(message: WebSocketMessage): void {
  switch (message.type) {
    case 'initial':
      // TypeScript knows data is InitialData
      console.log(`Loaded ${message.data.projects.length} projects`);
      break;
    case 'update':
      // TypeScript knows data is UpdateData
      console.log(`Updated project: ${message.data.projectPath}`);
      break;
    case 'error':
      // TypeScript knows data is ErrorData
      console.error(`Error: ${message.data.message}`);
      break;
  }
}

// Type guards for runtime validation
function isValidProject(obj: unknown): obj is Project {
  return (
    typeof obj === 'object' &&
    obj !== null &&
    'path' in obj &&
    'name' in obj &&
    'specs' in obj &&
    Array.isArray((obj as Project).specs)
  );
}

// Result type for error handling
type Result<T, E = Error> = 
  | { success: true; data: T }
  | { success: false; error: E };

function parseProjectData(data: unknown): Result<Project> {
  if (isValidProject(data)) {
    return { success: true, data };
  }
  return { success: false, error: new Error('Invalid project data') };
}
```

#### Development Guidelines
- **JSDoc documentation** on all exported functions
- **95%+ type coverage** maintained (no implicit any types)
- **Modern TypeScript patterns** (optional chaining, nullish coalescing)
- **Type guards preferred** over type assertions
- **Interfaces for object shapes**, union types for discriminated unions
- **Result<T> pattern** for error handling
- **Runtime validation** with type guards for external data

## 📚 Documentation

- **[Full Documentation](https://github.com/pimzino/claude-code-spec-workflow#readme)**
- **[Tunnel Feature Guide](./docs/tunnel-feature.md)** - Comprehensive tunnel documentation
- **[Tunnel Examples](./examples/tunnel/)** - Ready-to-use tunnel scripts
- **[Claude Code Docs](https://docs.anthropic.com/claude-code)**
- **[TypeScript API Reference](./docs/typescript-api.md)** - Generated from JSDoc comments

## 🤝 Contributing

Contributions are welcome! Please see our [Contributing Guide](https://github.com/pimzino/claude-code-spec-workflow/blob/main/CONTRIBUTING.md).

## 📄 License

MIT License - see [LICENSE](https://github.com/pimzino/claude-code-spec-workflow/blob/main/LICENSE) for details.

## 🏷️ Changelog

See [CHANGELOG.md](https://github.com/pimzino/claude-code-spec-workflow/blob/main/CHANGELOG.md) for version history.

---

## 🚦 When To Use What

| Scenario | Recommended Approach |
|----------|---------------------|
| **New feature, well-defined** | `/spec-execute` or individual task commands |
| **Complex/experimental feature** | `/spec-execute` (manual control) |
| **Bug in existing code** | Bug workflow (`/bug-create` → `/bug-verify`) |
| **Learning the codebase** | Manual execution with individual commands |
| **Production deployment** | Full spec workflow with completion review |

---

## 🚀 Installation & Setup

### **Installation**
```bash
# Install globally (recommended)
npm install -g @pimzino/claude-code-spec-workflow

# Verify installation
claude-code-spec-workflow --version
```

### **Setup Options**
```bash
# Basic setup
claude-code-spec-workflow

# Advanced options
claude-code-spec-workflow --project /path --force --yes
```

**During setup you choose:**
- ✅ **Enable agents?** Enhanced automation vs simpler setup
- ✅ **Project analysis** Auto-detection of frameworks and patterns

---

## 📚 Examples
**Recommendation: Use Claude Opus 4 to generate the spec documentation '/spec-create', then use Claude Sonnet 4 for the implementation i.e. '/spec-execute' or '/{spec-name}-task-<id>'.**
<details>
<summary><strong>Basic Workflow Example</strong></summary>

```bash
# 1. Install globally (one time)
npm install -g @pimzino/claude-code-spec-workflow

# 2. Setup project (one time)
cd my-project
claude-code-spec-workflow

# 3. Create steering documents (recommended)
claude
/spec-steering-setup

# 4. Create feature spec
/spec-create user-authentication "Secure login system"

# 5. Execute tasks
/spec-execute 1 user-authentication

# 6. Monitor progress
/spec-status user-authentication
```

</details>

<details>
<summary><strong>Bug Fix Example</strong></summary>

```bash
/bug-create login-timeout "Users logged out too quickly"
/bug-analyze
/bug-fix
/bug-verify
```

</details>

---

## ⚡ Context Optimization Commands

The package includes optimized commands for efficient document loading across all document types:

### **get-steering-context**
Load all steering documents at once for context sharing:
```bash
claude-code-spec-workflow get-steering-context
```
**Output**: Formatted markdown with all steering documents (product.md, tech.md, structure.md)

### **get-spec-context**
Load all specification documents at once for context sharing:
```bash
claude-code-spec-workflow get-spec-context feature-name
```
**Output**: Formatted markdown with all spec documents (requirements.md, design.md, tasks.md)

### **get-template-context**
Load templates by category for context sharing:
```bash
# Load all templates
claude-code-spec-workflow get-template-context

# Load specific template category
claude-code-spec-workflow get-template-context spec    # Spec templates
claude-code-spec-workflow get-template-context bug     # Bug templates
claude-code-spec-workflow get-template-context steering # Steering templates
```
**Output**: Formatted markdown with requested templates

### **Smart Document Handling**
- **High-redundancy documents** (steering, specs, templates): Use optimized bulk loading
- **Low-redundancy documents** (bug reports): Use direct file reading for simplicity
- **Selective delegation**: Main agents load full context, but pass only relevant portions to sub-agents
- **Individual files**: Continue using `get-content` for edge cases

### **Benefits**
- **60-80% token reduction** compared to individual file loading
- **Faster execution** with cached context across all workflows
- **Automatic fallback** to individual `get-content` when needed
- **Session-based caching** with intelligent file change detection

### **Hierarchical Context Management**
The system implements a sophisticated **hierarchical context management strategy** for maximum efficiency:

**Main Agents** (Commands like `/spec-execute`, `/spec-create`):
- **Load ALL context once** at the beginning using optimized commands
- **Store complete context** for task coordination and decision-making
- **Distribute selective context** to sub-agents without requiring reloads

**Sub-Agents** (Agents like `spec-task-executor`):
- **Priority 1**: Use provided context from task instructions (steering, specification, task details)
- **Priority 2**: Fallback to loading context only if not provided above
- **Never redundantly load** context when it's already been provided by main agents

**Context Distribution Pattern**:
```
Main Agent loads: Steering + Full Spec + Task Details
↓ Delegates to Sub-Agent with:
├── Complete Steering Context
├── Selective Spec Context (Requirements + Design only)
├── Specific Task Details
└── Clear instruction: "Do NOT reload context"
```

This approach **eliminates redundant loading** while ensuring each agent has exactly the context it needs.

---

## 🛟 Troubleshooting

<details>
<summary><strong>Common Issues</strong></summary>

**❓ "Command not found"**
```bash
# Install globally first
npm install -g @pimzino/claude-code-spec-workflow

# Then use the command
claude-code-spec-workflow
```

**❓ "Claude Code not detected"**
```bash
npm install -g @anthropic-ai/claude-code
```

**❓ "Permission errors"**
```bash
claude-code-spec-workflow --project ~/my-project
```

</details>

---

## 📋 Requirements

- **Node.js** 16.0.0+
- **Claude Code** installed
- Any project directory

---

## 🔗 Links

- **[Full Documentation](https://github.com/pimzino/claude-code-spec-workflow#readme)**
- **[Claude Code Docs](https://docs.anthropic.com/claude-code)**
- **[Report Issues](https://github.com/pimzino/claude-code-spec-workflow/issues)**

---

## 📄 License & Credits

**MIT License** - [LICENSE](LICENSE)

**Made with ❤️ by [Pimzino](https://github.com/pimzino)**

**Special Thanks:**
- @pimzino - Initial setup
- @boundless-oss - Steering documents
- @mquinnv - Dashboard feature

**Powered by:** [Claude Code](https://docs.anthropic.com/claude-code) • [Mermaid](https://mermaid.js.org/) • [TypeScript](https://www.typescriptlang.org/)