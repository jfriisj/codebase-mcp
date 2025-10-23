# Codebase MCP - Complete Setup & Usage Guide

## 📋 Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Installation Methods](#installation-methods)
   - [Method 1: Local Python Setup (Recommended for Development)](#method-1-local-python-setup-recommended-for-development)
   - [Method 2: Docker Setup (Recommended for Production)](#method-2-docker-setup-recommended-for-production)
4. [Configuration](#configuration)
5. [Integrating with Claude Desktop](#integrating-with-claude-desktop)
6. [Using the Tools](#using-the-tools)
7. [Troubleshooting](#troubleshooting)
8. [Advanced Usage](#advanced-usage)

---

## 🎯 Overview

**Codebase MCP** is an AI-powered development assistant that connects Claude Desktop (or any MCP-compatible LLM) to your codebase through the Model Context Protocol. It provides 13+ specialized tools for semantic code search, intelligent file editing, persistent memory, and Git workflow management.

**Architecture:**
- **FastAPI Server** (`main.py`) - Core engine running on port 6789
- **MCP Server** (`mcp_server.py`) - Proxy layer connecting Claude Desktop to FastAPI
- **Local Processing** - Privacy-first with local embeddings (except edit tool uses Gemini API)

---

## 📦 Prerequisites

### Required
- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Git** ([Download](https://git-scm.com/downloads))
- **Claude Desktop** or any MCP-compatible client ([Download](https://claude.ai/download))

### Recommended
- **[uv](https://github.com/astral-sh/uv)** - Fast Python package manager
- **Windows Terminal** or **PowerShell 7+** (for Windows users)

### Optional
- **Docker Desktop** (for containerized deployment)
- **Visual Studio Code** (for development)

---

## 🚀 Installation Methods

### Method 1: Local Python Setup (Recommended for Development)

#### Step 1: Clone the Repository

```powershell
# Navigate to your projects directory
cd C:\github

# Clone the repository
git clone https://github.com/danyQe/codebase-mcp.git
cd codebase-mcp
```

#### Step 2: Set Up Python Environment

**Option A: Using uv (Recommended - Faster)**

```powershell
# Install uv if you haven't
pip install uv

# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\activate  # Windows PowerShell
# OR
.venv\Scripts\Activate.ps1  # Windows PowerShell (if execution policy requires)

# Install dependencies
uv pip install -r requirements.txt
```

**Option B: Using Standard pip**

```powershell
# Create virtual environment
python -m venv .venv

# Activate virtual environment
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Step 3: Install Code Formatters (Required)

These formatters are required for the auto-formatting features:

```powershell
# Install formatters globally (recommended)
pip install black ruff

# Verify installation
black --version
ruff --version
```

**Optional: JavaScript/TypeScript formatters**
```powershell
# If you work with JS/TS projects
npm install -g prettier eslint
```

#### Step 4: Configure Environment Variables

```powershell
# Copy example environment file
Copy-Item .env.example .env

# Edit .env file with your preferred editor
notepad .env  # Or use: code .env
```

**Required Configuration:**
Add your Gemini API key to `.env`:

```env
GEMINI_API_KEY=your_api_key_here
```

**Get a free Gemini API key:**
1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy and paste into `.env` file

**Free tier limits:**
- 15 requests per minute (RPM)
- 250K tokens per minute (TPM)
- 1K requests per day (RPD)

#### Step 5: Verify Installation

```powershell
# Test FastAPI server
python main.py C:\github\codebase-mcp

# You should see:
# 🚀 Starting FastAPI server on 127.0.0.1:6789
# 📁 Using working directory: C:\github\codebase-mcp

# Open another terminal and test the API
curl http://localhost:6789/docs  # Should show Swagger UI
```

Press `Ctrl+C` to stop the server.

---

### Method 2: Docker Setup (Recommended for Production)

#### Step 1: Install Docker Desktop

Download and install [Docker Desktop](https://www.docker.com/products/docker-desktop/) for Windows.

#### Step 2: Configure Environment

```powershell
# Navigate to project directory
cd C:\github\codebase-mcp

# Copy and configure .env
Copy-Item .env.example .env
notepad .env  # Add your GEMINI_API_KEY
```

#### Step 3: Build and Run with Docker

**Option A: Using docker-compose (Simplest)**

```powershell
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f

# Stop
docker-compose down
```

**Option B: Using Docker directly**

```powershell
# Build image
docker build -t codebase-mcp .

# Run container
docker run -d `
  --name codebase-mcp `
  -p 6789:6789 `
  -v ${PWD}:/app `
  -e GEMINI_API_KEY=your_key_here `
  codebase-mcp
```

#### Step 4: Using Pre-built Docker Image (From mcp.json)

The `mcp.json` file includes configuration for using a pre-built Docker image:

```json
{
    "servers": {
        "code-manager": {
            "command": "docker",
            "args": [
                "run", "--rm", "-i",
                "--name", "mcp-code-manager-${workspaceFolderBasename}",
                "-p", "6789:6789",
                "-e", "GEMINI_API_KEY={{GEMINI_API_KEY}}",
                "-v", "${workspaceFolder}:/app",
                "ghcr.io/jfriisj/codebase-mcp:sha-bcb96d7"
            ]
        }
    }
}
```

This configuration:
- Uses the pre-built image `ghcr.io/jfriisj/codebase-mcp:sha-bcb96d7`
- Mounts your workspace folder into the container
- Sets up environment variables from your config

---

## ⚙️ Configuration

### Environment Variables (.env)

Key configuration options:

```env
# ===== REQUIRED =====
GEMINI_API_KEY=your_gemini_api_key_here

# ===== OPTIONAL - Server Configuration =====
API_HOST=127.0.0.1      # Server host (default: localhost)
API_PORT=6789           # Server port (default: 6789)

# ===== OPTIONAL - Search & Indexing =====
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
MAX_SEARCH_RESULTS=10
FAISS_INDEX_TYPE=Flat

# ===== OPTIONAL - Code Quality =====
QUALITY_THRESHOLD=0.8      # Auto-commit threshold (0.0-1.0)
AUTO_FORMAT_PYTHON=true
AUTO_FORMAT_JS=true

# ===== OPTIONAL - Git Configuration =====
CODEBASE_GIT_DIR=.codebase    # Separate Git directory for AI changes
DEFAULT_BRANCH=main
AUTO_COMMIT_ENABLED=true

# ===== OPTIONAL - Memory System =====
MEMORY_CONTEXT_MAX=10
MEMORY_RECENT_DAYS=30
MEMORY_MIN_IMPORTANCE=3
```

### MCP Server Configuration (mcp.json)

The `mcp.json` file configures how MCP clients (like Claude Desktop) connect to the server. See [Method 2: Docker Setup](#method-2-docker-setup-recommended-for-production) for details.

---

## 🔗 Integrating with Claude Desktop

### Step 1: Locate Claude Desktop Config

Find your Claude Desktop configuration file:

**Windows:**
```
%APPDATA%\Claude\claude_desktop_config.json
```

**macOS:**
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

**Linux:**
```
~/.config/Claude/claude_desktop_config.json
```

### Step 2: Add MCP Server Configuration

**For Local Python Setup:**

```json
{
  "mcpServers": {
    "codebase-manager": {
      "command": "C:\\github\\codebase-mcp\\.venv\\Scripts\\python.exe",
      "args": [
        "C:\\github\\codebase-mcp\\mcp_server.py"
      ]
    }
  }
}
```

**Important Notes:**
- Use **absolute paths** (not relative)
- Use **double backslashes** (`\\`) for Windows paths
- Point to your virtual environment's Python executable
- Adjust paths to match your installation directory

**For Docker Setup:**

If using Docker, you can use the configuration from `mcp.json` (copy the content into your Claude Desktop config).

### Step 3: Restart Claude Desktop

1. Completely quit Claude Desktop
2. Restart Claude Desktop
3. Look for the hammer icon (🔨) indicating MCP tools are available

### Step 4: Start the FastAPI Server

Before using Claude Desktop, start the FastAPI server:

```powershell
# Navigate to codebase-mcp directory
cd C:\github\codebase-mcp

# Activate virtual environment (if using local setup)
.venv\Scripts\activate

# Start server with your project path
python main.py C:\path\to\your\project

# Example:
python main.py C:\github\my-awesome-app
```

**Server Output:**
```
🚀 Starting FastAPI server on 127.0.0.1:6789
📁 Using working directory: C:\github\my-awesome-app
✅ Registered router: ['Session']
✅ Registered router: ['Memory']
...
```

Keep this terminal open while using Claude Desktop.

---

## 🛠️ Using the Tools

### Available MCP Tools (13 Total)

| Tool | Purpose | Example Usage |
|------|---------|---------------|
| `session_tool` | Manage dev sessions | Start/end/merge branches |
| `memory_tool` | Store/retrieve knowledge | Remember solutions, mistakes |
| `git_tool` | Git operations | Status, diff, commit, log |
| `write_tool` | Create new files | Auto-format, quality scoring |
| `edit_file` | AI-assisted editing | Gemini-powered edits |
| `search_tool` | Semantic code search | Find functions, patterns |
| `read_code_tool` | Smart code reading | Read symbols, line ranges |
| `project_context_tool` | Project analysis | Structure, dependencies |
| `list_directory_tool` | Directory exploration | Tree view, metadata |
| `code_analysis_tool` | Quality checks | Syntax, linting, imports |
| `list_file_symbols_tool` | Symbol extraction | Functions, classes |
| `read_symbol_from_database` | DB symbol lookup | Fast indexed retrieval |
| `project_structure_tool` | Project visualization | Enhanced tree with stats |

### Example Workflows

#### 1. Starting a New Feature

```
You: "Create a new REST API endpoint for user profile management with CRUD operations"

Claude will:
✅ Create a new session (feat/user-profile)
✅ Search for existing patterns
✅ Write new files with proper structure
✅ Auto-format code (Black + Ruff)
✅ Score quality (aim for 80%+)
✅ Auto-commit if quality threshold met
✅ Store knowledge in memory
```

**Behind the scenes:**
1. `session_tool(operation="start", session_name="feat/user-profile")`
2. `search_tool(query="user management patterns")`
3. `write_tool(file_path="api/users.py", content=...)`
4. Auto-commit to `.codebase` branch

#### 2. Refactoring Code

```
You: "Refactor authentication.py to use dependency injection"

Claude will:
✅ Read current implementation
✅ Search for DI patterns in codebase
✅ Edit file with AI assistance (Gemini)
✅ Validate changes
✅ Format and commit
```

**Behind the scenes:**
1. `read_code_tool(file_path="authentication.py")`
2. `search_tool(query="dependency injection patterns")`
3. `edit_file(file_path="authentication.py", instructions="Apply DI pattern")`

#### 3. Debugging with Memory

```
You: "Continue working on the payment integration"

Claude will:
✅ Query memory for context
✅ Recall previous progress
✅ Remember past mistakes
✅ Continue from checkpoint
```

**Behind the scenes:**
1. `memory_tool(operation="search", query="payment integration")`
2. Retrieves: "Stripe API setup complete", "Don't use sync in async endpoints"
3. Continues work with context

#### 4. Code Search

```
You: "Find all functions that handle authentication"

Claude will:
✅ Use semantic search
✅ Find relevant functions
✅ Show implementations
```

**Behind the scenes:**
1. `search_tool(mode="semantic", query="authentication handlers")`
2. Returns ranked results with context

### Session Management

#### Start a Session
```
You: "Start a new session for implementing OAuth"
```
Creates branch: `session/oauth-implementation`

#### End a Session
```
You: "End the current session"
```
Switches back to main branch, optionally merges changes

#### List Sessions
```
You: "Show all active sessions"
```
Lists all session branches with status

#### Merge a Session
```
You: "Merge the OAuth session into main"
```
Merges changes with quality validation

### Memory System

#### Store Knowledge
```
You: "Remember that we use JWT tokens with 24-hour expiry"
```
Stored with category: `architecture`, importance: `high`

#### Query Memory
```
You: "What authentication method do we use?"
```
Retrieves: "JWT tokens with 24-hour expiry"

#### Categories:
- `progress` - What has been completed
- `mistakes` - Errors to avoid
- `solutions` - Working approaches
- `architecture` - Design decisions

---

## 🔧 Troubleshooting

### Common Issues

#### 1. "Cannot connect to FastAPI server"

**Problem:** MCP server can't reach FastAPI backend

**Solutions:**
```powershell
# Check if FastAPI server is running
curl http://localhost:6789/docs

# If not running, start it:
python main.py C:\path\to\your\project

# Check for port conflicts
netstat -ano | findstr :6789

# Kill conflicting process (find PID from above)
taskkill /PID <PID> /F
```

#### 2. "ModuleNotFoundError: No module named 'mcp'"

**Problem:** Dependencies not installed

**Solution:**
```powershell
# Activate virtual environment
.venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt

# Verify installation
pip list | findstr mcp
```

#### 3. "Gemini API key not found"

**Problem:** `.env` file not configured

**Solution:**
```powershell
# Check if .env exists
Test-Path .env

# If not, copy example
Copy-Item .env.example .env

# Edit and add your key
notepad .env
```

#### 4. "Black or Ruff not found"

**Problem:** Code formatters not installed

**Solution:**
```powershell
# Install globally
pip install black ruff

# Or in virtual environment
.venv\Scripts\pip install black ruff

# Verify
black --version
ruff --version
```

#### 5. Claude Desktop Not Showing MCP Tools

**Problem:** Configuration not loaded or server not running

**Solution:**
1. Check `claude_desktop_config.json` syntax (valid JSON)
2. Verify paths are absolute and correct
3. Ensure FastAPI server is running
4. Completely quit and restart Claude Desktop
5. Check Claude Desktop logs:
   ```powershell
   # Windows
   Get-Content "$env:APPDATA\Claude\logs\mcp*.log" -Tail 50
   ```

#### 6. "TimeoutError" in Claude Desktop

**Problem:** Operation taking too long (edit_file is slow)

**Solution:**
- Edit smaller sections of code
- Increase timeout in `mcp_server.py` (line 35):
  ```python
  HTTP_TIMEOUT = 60.0  # Increase from 30.0
  ```
- Check network connection to Gemini API

---

## 🚀 Advanced Usage

### Custom Working Directory Per Project

```powershell
# Start server for different projects
python main.py C:\projects\webapp
python main.py C:\projects\api --port 6790  # Use different port
```

### Running Multiple Instances

```powershell
# Terminal 1 - Project A
python main.py C:\projects\projectA --port 6789

# Terminal 2 - Project B
python main.py C:\projects\projectB --port 6790
```

Update `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "projectA": {
      "command": "C:\\github\\codebase-mcp\\.venv\\Scripts\\python.exe",
      "args": ["C:\\github\\codebase-mcp\\mcp_server.py"],
      "env": {"FASTAPI_BASE_URL": "http://localhost:6789"}
    },
    "projectB": {
      "command": "C:\\github\\codebase-mcp\\.venv\\Scripts\\python.exe",
      "args": ["C:\\github\\codebase-mcp\\mcp_server.py"],
      "env": {"FASTAPI_BASE_URL": "http://localhost:6790"}
    }
  }
}
```

### Web Dashboard

Access the web interface at `http://localhost:6789` when server is running:
- View project structure
- Search codebase
- Browse sessions
- Check memory entries

### API Documentation

Interactive API docs available at:
- **Swagger UI:** http://localhost:6789/docs
- **ReDoc:** http://localhost:6789/redoc

### Development Mode

```powershell
# Run with auto-reload (restarts on code changes)
python main.py C:\path\to\project --reload

# Enable debug logging
$env:LOG_LEVEL="DEBUG"
python main.py C:\path\to\project
```

### Performance Tuning

For large codebases (20K+ lines):

```env
# .env configuration
FAISS_INDEX_TYPE=IVF           # Use IVF instead of Flat for speed
MAX_FILE_SIZE_MB=10            # Increase max file size
WORKERS=4                       # Adjust workers based on CPU cores
REQUEST_TIMEOUT=60              # Increase timeout for large ops
```

### Git Workflow Isolation

Codebase MCP uses `.codebase` directory for AI-tracked changes, separate from your main `.git`:

```powershell
# Your main Git repo
git status                    # Your manual changes

# AI-tracked changes
cd .codebase
git log                       # AI session commits
cd ..

# Merge AI changes when ready
# (via session_tool merge operation in Claude)
```

### Custom Prompts

Modify AI behavior by editing `prompts/general_dev_prompt.py`:

```python
GENERAL_DEV_PROMPT = """
Your custom instructions for Claude's coding behavior...
"""
```

---

## 📚 Additional Resources

- **Full Documentation:** https://danyqe.github.io/codebase-mcp/
- **Architecture Diagram:** `docs/architecture.png`
- **Contributing Guide:** `CONTRIBUTING.md`
- **GitHub Issues:** https://github.com/danyQe/codebase-mcp/issues
- **GitHub Discussions:** https://github.com/danyQe/codebase-mcp/discussions

---

## 🎯 Quick Start Checklist

- [ ] Python 3.11+ installed
- [ ] Git installed
- [ ] Repository cloned
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Formatters installed (`pip install black ruff`)
- [ ] `.env` file configured with `GEMINI_API_KEY`
- [ ] Claude Desktop config updated with absolute paths
- [ ] FastAPI server started (`python main.py <project_path>`)
- [ ] Claude Desktop restarted
- [ ] MCP tools visible in Claude Desktop (🔨 icon)

---

## 📝 Notes

### Privacy
- All processing is local except `edit_file` tool (uses Gemini API)
- Only the file being edited is sent to Gemini
- No project context or history shared externally

### Performance
- Optimal for projects under 20K lines
- Initial indexing: ~30 seconds for 10K lines
- Semantic search: Sub-second response
- Edit operations: 5-15 seconds (Gemini API + formatting)

### Costs
- Gemini API: **Free tier** (15 RPM, 250K TPM, 1K RPD)
- Claude Desktop: Requires Claude Pro or Team subscription
- No additional costs beyond your existing Claude subscription

---

**Happy Coding! 🚀**

Made with ❤️ by developers, for developers
