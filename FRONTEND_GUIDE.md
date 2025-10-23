# Codebase MCP - Frontend Dashboard User Guide

## 📋 Table of Contents

1. [Overview](#overview)
2. [Accessing the Dashboard](#accessing-the-dashboard)
3. [Dashboard Layout](#dashboard-layout)
4. [Core Features](#core-features)
   - [Dashboard Home](#1-dashboard-home)
   - [Search & Index Management](#2-search--index-management)
   - [File Operations](#3-file-operations)
   - [Git & AI Sessions](#4-git--ai-sessions)
   - [Memory System](#5-memory-system)
   - [Project Explorer](#6-project-explorer)
   - [Directory Browser](#7-directory-browser)
   - [Working Directory](#8-working-directory)
   - [Tool Call History](#9-tool-call-history)
   - [System Logs](#10-system-logs)
5. [Keyboard Shortcuts](#keyboard-shortcuts)
6. [Best Practices](#best-practices)
7. [Troubleshooting](#troubleshooting)

---

## 🎯 Overview

The **Codebase MCP Frontend Dashboard** is a modern, responsive web interface for managing your AI-powered development workflow. Built with Tailwind CSS and vanilla JavaScript, it provides a visual interface to all the MCP server capabilities including semantic search, file editing, Git sessions, and persistent memory.

**Key Features:**
- 🎨 Modern, gradient-rich UI with smooth animations
- 📱 Fully responsive (desktop, tablet, mobile)
- 🚀 Real-time updates and status monitoring
- ⌨️ Keyboard shortcuts for power users
- 🎯 No external dependencies (runs in browser)

---

## 🌐 Accessing the Dashboard

### Step 1: Start the FastAPI Server

```powershell
# Navigate to codebase-mcp directory
cd C:\github\codebase-mcp

# Activate virtual environment
.venv\Scripts\activate

# Start server with your project path
python main.py C:\path\to\your\project
```

### Step 2: Open in Browser

Once the server is running, open your browser and navigate to:

```
http://localhost:6789
```

**Alternative URLs:**
- **API Documentation**: http://localhost:6789/docs (Swagger UI)
- **ReDoc**: http://localhost:6789/redoc (Alternative API docs)

### Supported Browsers

- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

---

## 📐 Dashboard Layout

### Main Components

```
┌─────────────────────────────────────────────────────────┐
│  [☰] Header                          [🟢 Connected]     │
├───────────┬─────────────────────────────────────────────┤
│           │                                             │
│ Sidebar   │         Main Content Area                   │
│           │                                             │
│ • Dashboard│  ┌───────────────────────────────────┐    │
│ • Search   │  │                                   │    │
│ • Files    │  │    Active Section                 │    │
│ • Git      │  │    (Dashboard, Search, etc.)      │    │
│ • Memory   │  │                                   │    │
│ • Project  │  └───────────────────────────────────┘    │
│ • Directory│                                            │
│ • Working  │                                            │
│ • History  │                                            │
│ • Logs     │                                            │
│ • Settings │                                            │
│           │                                             │
│ [Status]  │                                             │
└───────────┴─────────────────────────────────────────────┘
```

### Navigation Elements

1. **Sidebar** (Left) - Primary navigation menu
2. **Header** (Top) - Connection status and quick actions
3. **Content Area** (Center) - Dynamic section content
4. **Toast Notifications** (Top Right) - Success/error messages
5. **Status Panel** (Bottom of sidebar) - System health indicators

---

## 🛠️ Core Features

## 1. Dashboard Home

**Access:** Click "Dashboard" in sidebar or press `Alt+1`

### Overview

The main landing page showing system health, statistics, and recent activity.

### Sections

#### Quick Actions
Four quick-access cards:
- **Search Code** - Jump to semantic search
- **Edit Files** - Open file operations
- **Git Sessions** - Manage development sessions
- **Tool History** - View API call history

#### System Health
Real-time status of core components:
- ✅ **FastAPI Server** - Backend API status
- ✅ **Semantic Search** - Search engine health
- ✅ **Memory System** - Persistent storage
- ✅ **Git Manager** - Version control
- ✅ **Code Tools** - Formatter availability

#### Project Stats
- **Total Files** - Indexed files in project
- **Total Lines** - Code line count
- **Languages** - Detected programming languages
- **Last Indexed** - Most recent indexing time

#### Tool Activity
- **Recent Tool Calls** - Last 10 API operations
- **Success Rate** - Percentage of successful calls
- **Most Used Tool** - Most frequently called endpoint

#### Current Session
- **Active Branch** - Current Git branch
- **Session Type** - AI session or main branch
- **Modified Files** - Uncommitted changes

#### Recent Tool Calls
List of last executed API operations with:
- Tool name and endpoint
- Timestamp
- Status (success/error)
- Response time

#### Activity Feed
Real-time feed of dashboard events:
- API calls
- Index updates
- Session changes
- Error notifications

#### API Route Statistics
Table showing usage stats for all endpoints:
- **Route** - API endpoint path
- **Method** - HTTP method (GET/POST)
- **Calls** - Total invocations
- **Avg Time** - Average response time
- **Success Rate** - Percentage of successful calls

### Actions

- **Refresh Dashboard** - Click refresh icon to reload all stats
- **View Tool History** - Click "View All" to see complete history
- **Clear Activity Feed** - Remove old activity entries

---

## 2. Search & Index Management

**Access:** Click "Search & Index" in sidebar or press `Alt+2`

### Overview

Powerful semantic and text-based code search with index management.

### Index Statistics

Four stat cards showing:
- **Indexed Files** - Total files in index
- **Code Chunks** - Semantic search chunks
- **Symbols** - Extracted functions/classes
- **Rebuild Index** - Button to reindex codebase

### Search Modes

#### Semantic Search Tab (AI-Powered)

**What it does:** Natural language code search using ML embeddings

**Fields:**
- **Semantic Query** - Describe what you're looking for
  - Example: `"function that processes user data"`
  - Example: `"authentication middleware"`
  - Example: `"database connection logic"`

- **File Pattern** (Optional) - Filter by file types
  - `*.py` - Only Python files
  - `*.js, *.ts` - JavaScript/TypeScript
  - `src/**/*.py` - Python files in src/

- **Max Results** - Number of results (1-50)

**How to use:**
1. Enter natural language query
2. Set file pattern (optional)
3. Click "Search Semantically"
4. Results show ranked by relevance

**Best for:**
- Finding functionality without knowing exact names
- Discovering similar code patterns
- Understanding code purpose

#### Text Search Tab

**What it does:** Exact text matching (like `grep`)

**Fields:**
- **Text to Find** - Exact text or regex pattern
- **File Pattern** - File type filter (e.g., `*.py`)
- **Use Regex** - Enable regular expressions
- **Case Sensitive** - Match case exactly

**Examples:**
```
Simple: "def authenticate"
Regex: "class \w+Service"
Case: "TODO" vs "todo"
```

**Best for:**
- Finding exact variable/function names
- Searching specific error messages
- Locating TODO comments

#### Symbol Search Tab

**What it does:** Search by function/class/interface names

**Fields:**
- **Symbol Name** - Name of symbol
- **Symbol Type** - Filter by type
  - All Types
  - Function
  - Class
  - Interface
  - Type
  - Enum

- **File Pattern** - File filter
- **Fuzzy Match** - Allow approximate matches

**Examples:**
```
Function: "process_data"
Class: "UserService"
Fuzzy: "usrSvc" → matches "UserService"
```

**Best for:**
- Navigating to specific functions
- Finding class definitions
- Exploring code structure

### Search Results

Results display shows:
- **File Path** - Location of match
- **Line Numbers** - Where code appears
- **Code Preview** - Highlighted context
- **Relevance Score** - Match quality (semantic only)

**Actions:**
- **Copy Path** - Copy file path to clipboard
- **View in Files** - Open file in editor
- **Clear Results** - Remove current results

### Index Management

**Rebuild Index** - Reindex entire codebase
- **When to use:**
  - After major file changes
  - New files added/removed
  - Search results outdated
  
- **Process:**
  1. Click "Rebuild Index"
  2. Wait for completion (30s for 10K lines)
  3. "Index rebuilt successfully" notification

**Auto-indexing:**
- Runs automatically on server start
- Updates when files change (if enabled)

---

## 3. File Operations

**Access:** Click "File Operations" in sidebar or press `Alt+3`

### Overview

Read, write, and AI-edit code files with quality checking.

### Tabs

#### Read Code Tab

**What it does:** Read file contents with smart filtering

**Fields:**
- **File Path** - Relative path to file
  - Example: `src/api/users.py`
  - Example: `components/Button.tsx`

- **Symbol Name** (Optional) - Read specific function/class
  - Example: `authenticate_user`
  - Only shows that symbol

- **Start Line** (Optional) - Begin reading from line
- **End Line** (Optional) - Stop reading at line
- **Show Line Numbers** - Display line numbers

**Usage Examples:**

```
Read entire file:
  File Path: src/api/users.py
  → Shows complete file

Read specific function:
  File Path: src/api/users.py
  Symbol Name: authenticate_user
  → Shows only that function

Read line range:
  File Path: src/api/users.py
  Start Line: 50
  End Line: 100
  → Shows lines 50-100
```

**Code Preview:**
- Syntax-highlighted display
- Copy code button
- Line numbers (if enabled)
- Terminal-style appearance

#### Write File Tab

**What it does:** Create new files with auto-formatting and quality checks

**Fields:**
- **File Path** - Path for new file
  - Example: `api/new_endpoint.py`
  - Creates directories if needed

- **Purpose** (Optional) - Describe file purpose
  - Example: `"User authentication endpoints"`
  - Stored in metadata

- **Language** - Auto-detected from extension
  - Manual override available
  - Options: Python, JavaScript, TypeScript

- **Code Content** - Your code

**Features:**
- ✅ **Auto-formatting** - Black (Python), Prettier (JS/TS)
- ✅ **Quality Scoring** - Code quality assessment (0-100%)
- ✅ **Dependency Check** - Validates imports
- ✅ **Auto-commit** - Commits if quality ≥ 80%

**Write Result Shows:**
- ✅ File created successfully
- 📊 Quality Score: 95%
- 🔄 Auto-committed: Yes
- 📝 Formatting: Applied
- ⚠️ Warnings (if any)

**Example Workflow:**
```
1. Set File Path: api/auth.py
2. Set Purpose: "JWT authentication handler"
3. Write code content
4. Click "Write File with Quality Check"
5. Review quality score
6. File auto-commits if quality good
```

#### AI Edit Tab

**What it does:** AI-assisted file editing using Gemini

**⚠️ Important:** This uses Gemini API (requires `GEMINI_API_KEY` in `.env`)

**Fields:**
- **Target File** - Existing file to edit
- **Edit Instructions** - Natural language changes
  - Example: `"Add error handling to process_data function"`
  - Example: `"Refactor to use async/await"`
  - Example: `"Add input validation"`

- **Code Edit (Sketch)** - Show desired changes
  - Use `// ... existing code ...` for unchanged parts
  - Show only what changes

**Example:**
```python
Edit Instructions: "Add try-except error handling"

Code Edit (Sketch):
# ... existing code ...
def process_data(data):
    try:
        result = transform(data)
        return result
    except ValueError as e:
        logger.error(f"Data error: {e}")
        raise
# ... existing code ...
```

**AI Edit Process:**
1. Reads current file
2. Sends to Gemini with instructions
3. AI generates complete edited file
4. Validates syntax
5. Formats code
6. Returns result with diff

**Edit Result Shows:**
- ✅ Edit successful
- 📝 Changes summary
- 🔍 Diff preview
- ⚠️ Validation errors (if any)

**Pro Tips:**
- Be specific in instructions
- Use code sketch to guide AI
- Edit smaller sections for faster results
- Review diff before accepting

#### List Symbols Tab

**What it does:** Extract all symbols from a file

**Fields:**
- **File Path** - File to analyze

**Shows:**
- Functions with signatures
- Classes with methods
- Interfaces (TypeScript)
- Enums and types
- Line numbers for each

**Use Cases:**
- Quick code navigation
- Understanding file structure
- Finding function signatures

---

## 4. Git & AI Sessions

**Access:** Click "Git & Sessions" in sidebar or press `Alt+4`

### Overview

Manage Git operations and AI-powered development sessions.

### Current Status Cards

Three status indicators:
- **Current Branch** - Active Git branch
- **Session Status** - 🟢 Active or ⚪ Inactive
- **Modified Files** - Uncommitted change count

### AI Session Management

**What are sessions?**
AI sessions create isolated development branches for feature work, allowing you to:
- Experiment safely
- Track AI-generated changes separately
- Merge when ready

**Session Operations:**

#### Start Session
```
1. Enter session name (optional)
   - Auto-generated if empty
   - Example: "feat/user-auth"

2. Click "Start"
   
3. Result:
   ✅ New branch created
   ✅ Switched to session
   ✅ Ready for changes
```

#### End Session
```
1. Click "End"

2. Options:
   - Return to main branch
   - Keep session branch
   - Delete session branch

3. Status updates automatically
```

#### List Sessions
```
Shows all session branches:
- Session name
- Creation date
- Commit count
- Status (active/inactive)
```

#### Current Session Info
```
Displays:
- Current branch name
- Is it a session? Yes/No
- Parent branch
- Time active
```

**Session Info Panel:**
- Shows detailed session information
- Recent commits in session
- Files changed
- Merge status

### Git Operations

Standard Git commands with visual feedback:

#### Status
```
Shows:
- Current branch
- Modified files (orange)
- Untracked files (gray)
- Staged files (green)
- Ahead/behind main
```

#### Branches
```
Lists all branches:
- Current (highlighted)
- Session branches (marked)
- Remote branches
- Last commit per branch
```

#### Log
```
Commit history:
- Commit hash (short)
- Author
- Date/time
- Message
- Files changed
```

#### Diff
```
Shows changes:
- File-by-file diff
- Added lines (green +)
- Removed lines (red -)
- Modified lines
```

#### Tree
```
Visual branch tree:
- Branch relationships
- Merge points
- Commit graph
- ASCII art representation
```

**Git Output Terminal:**
- Dark terminal theme
- Syntax-highlighted output
- Scrollable history
- Copy output button

### Available Sessions List

Table showing all session branches:
- **Session Name** - Branch identifier
- **Created** - Start timestamp
- **Commits** - Number of commits
- **Status** - Active/Inactive
- **Actions** - Switch/Delete/Merge buttons

**Actions:**
- **Switch** - Activate this session
- **Merge** - Merge into main (with confirmation)
- **Delete** - Remove session branch

### Branch Tree Visualization

ASCII art representation:
```
main
├─ session/oauth-impl
│  └─ 3 commits
├─ session/refactor-auth
│  └─ 5 commits
└─ feat/user-profile
   └─ 2 commits
```

---

## 5. Memory System

**Access:** Click "Memory System" in sidebar or press `Alt+5`

### Overview

Persistent knowledge storage across sessions - remember context, solutions, mistakes, and decisions.

### Memory Statistics

Four stat cards:
- **Total Memories** - All stored memories
- **Recent (7 days)** - Recent additions
- **Verified** - Confirmed accurate memories
- **Categories** - Number of distinct categories

### Store New Memory

**Purpose:** Save important knowledge for future reference

**Fields:**

- **Category** - Type of memory:
  - 📚 **Learning** - New knowledge gained
  - 🚀 **Progress** - Work completed
  - ⚙️ **Preference** - User/project preferences
  - ⚠️ **Mistake** - Errors to avoid
  - 💡 **Solution** - Working approaches
  - 🏗️ **Architecture** - Design decisions
  - 🔗 **Integration** - External system info
  - 🐛 **Debug** - Debugging insights

- **Importance** - 1-5 stars
  - 1⭐ - Minor note
  - 3⭐⭐⭐ - Important
  - 5⭐⭐⭐⭐⭐ - Critical

- **Memory Content** - What to remember
  - Be specific and clear
  - Include context
  - Note date if relevant

**Examples:**

```
Category: Architecture
Importance: 5 stars
Content: "We use JWT tokens with 24-hour expiry for authentication. 
Refresh tokens stored in httpOnly cookies. Public key rotation every 30 days."

---

Category: Mistake
Importance: 4 stars
Content: "Don't use synchronous database calls in async FastAPI endpoints.
Always use async SQLAlchemy or asyncpg. Caused 5s response times."

---

Category: Progress
Importance: 3 stars
Content: "Completed Stripe payment integration on 2025-10-20. 
API keys stored in .env, webhook endpoint at /api/webhooks/stripe"
```

### Search Memories

**Purpose:** Find relevant memories for current work

**Fields:**
- **Search Query** - Natural language search
  - Example: `"authentication setup"`
  - Example: `"database connection"`

- **Category Filter** - Narrow by category
  - Optional - leave blank for all

- **Max Results** - Limit results (1-50)

**Buttons:**
- **Search** - Standard search by query
- **Context** - Get relevant memories for current work

**Context Mode:**
- Automatically finds related memories
- Uses recent days filter (30 days default)
- Importance threshold (3+ stars)
- Sorted by relevance

### Memory Browser

**Purpose:** Browse all stored memories

**Features:**
- **Category Filter** - Dropdown to filter by category
- **Refresh** - Reload memory list
- **Sort** - By date, importance, or category

**Memory Cards Show:**
- 📅 **Date** - When stored
- 📂 **Category** - Memory type (with emoji)
- ⭐ **Importance** - Star rating
- 📝 **Content** - Memory text
- ✅ **Verified** - If confirmed accurate
- **Actions:**
  - Edit - Update memory
  - Delete - Remove memory
  - Verify - Mark as confirmed

**Memory Management:**
```
View: Click to expand full content
Edit: Update importance or content
Verify: Confirm accuracy
Delete: Remove outdated memory
```

### Best Practices

1. **Be Specific:** Include dates, versions, reasons
2. **Use Categories:** Helps with filtering and organization
3. **Set Importance:** Critical info gets 4-5 stars
4. **Verify Periodically:** Confirm memories are still accurate
5. **Clean Up:** Delete outdated or incorrect memories

### Memory Use Cases

**Architecture Decisions:**
```
"Decided to use PostgreSQL over MongoDB because we need 
strong relationships and ACID transactions. Migration done 2025-10-15."
```

**API Integrations:**
```
"Stripe webhooks need webhook signing key validation.
Key stored as STRIPE_WEBHOOK_SECRET in .env."
```

**Performance Lessons:**
```
"Database queries should use indexes. Added index on users.email 
which reduced query time from 2s to 50ms."
```

**Bug Solutions:**
```
"CORS errors fixed by adding 'http://localhost:3000' to 
CORS_ORIGINS in .env. Required for React dev server."
```

---

## 6. Project Explorer

**Access:** Click "Project Explorer" in sidebar or press `Alt+6`

### Overview

Analyze project structure, dependencies, and code organization.

### Project Overview Card

**Shows:**
- **Project Name** - Derived from directory
- **Total Files** - Count of indexed files
- **Total Lines** - Sum of all code lines
- **Languages** - Detected languages with percentages
- **Last Analysis** - Most recent scan time

### Language Distribution

**Pie chart showing:**
- Language names
- Percentage of codebase
- Line counts
- File counts

**Supported Languages:**
- Python (`.py`)
- JavaScript (`.js`)
- TypeScript (`.ts`, `.tsx`)
- React (`.jsx`)
- And more...

### File Structure Tree

**Visual directory tree:**
```
project/
├─ src/
│  ├─ api/
│  │  ├─ users.py (245 lines)
│  │  └─ auth.py (180 lines)
│  └─ models/
│     └─ user.py (120 lines)
├─ tests/
│  └─ test_api.py (89 lines)
└─ README.md (45 lines)
```

**Features:**
- Expandable directories
- File line counts
- Icon indicators
- Syntax highlighting

### Dependencies Analysis

**Shows:**
- **External Packages** - Libraries imported
- **Internal Modules** - Local file imports
- **Dependency Graph** - Import relationships
- **Circular Dependencies** - Warning if detected

**Example:**
```
External:
- fastapi (used in 5 files)
- pydantic (used in 12 files)
- sqlalchemy (used in 8 files)

Internal:
- api.users → models.user
- api.auth → utils.jwt_handler
```

### Code Metrics

**Quality metrics:**
- **Average File Size** - Lines per file
- **Largest Files** - Top 10 by size
- **Complexity Score** - Code complexity rating
- **Test Coverage** - If tests detected

### Project Actions

**Available actions:**
- **Refresh Analysis** - Rescan project
- **Export Structure** - Download JSON
- **Generate README** - Auto-create documentation
- **View Dependencies** - Detailed dependency tree

---

## 7. Directory Browser

**Access:** Click "Directory Browser" in sidebar or press `Alt+7`

### Overview

File system navigation with filtering and search.

### Directory Navigation

**Breadcrumb Trail:**
```
Home > Projects > my-app > src > api
```
- Click any level to jump back
- Shows current path

### File List View

**Columns:**
- **Type** - File/Directory icon
- **Name** - Item name
- **Size** - File size (human readable)
- **Modified** - Last modified timestamp
- **Actions** - Quick action buttons

**Icons:**
- 📁 - Directory (click to enter)
- 📄 - Text file
- 🐍 - Python file
- 📜 - JavaScript
- 🎨 - CSS/styling
- 🖼️ - Image
- 📦 - Package/config

### Filtering

**Filter Options:**
- **Show Hidden** - Toggle dot files
- **File Type** - Filter by extension
  - All Files
  - Python (`.py`)
  - JavaScript (`.js`)
  - TypeScript (`.ts`)
  - JSON (`.json`)
  - Markdown (`.md`)

- **Sort By** - Ordering
  - Name (A-Z)
  - Size (largest first)
  - Modified (newest first)
  - Type (files/directories)

### Search in Directory

**Quick search:**
- Type to filter visible files
- Real-time filtering
- Supports wildcards (`*.py`)
- Case-insensitive

### File Actions

**Per-file actions:**
- **View** - Open in read-only mode
- **Edit** - Open in file editor
- **Delete** - Remove file (confirmation)
- **Rename** - Change filename
- **Copy Path** - Copy to clipboard

**Bulk Actions:**
- Select multiple files (checkbox)
- Delete Selected
- Move Selected
- Archive Selected (create .zip)

### Directory Actions

**Available operations:**
- **Create Directory** - New folder
- **Create File** - New file with template
- **Upload File** - From local system
- **Download** - Download as .zip

---

## 8. Working Directory

**Access:** Click "Working Directory" in sidebar or press `Alt+8`

### Overview

Manage the current working directory for the MCP server.

### Current Directory Display

**Shows:**
- **Full Path** - Complete directory path
- **Project Name** - Derived from folder
- **Git Status** - If Git repository
- **Permissions** - Read/Write status

### Change Working Directory

**Process:**
```
1. Enter new directory path
   Example: C:\projects\my-app

2. Click "Change Directory"

3. Server validates:
   ✅ Path exists
   ✅ Readable
   ✅ Has write permissions

4. Updates:
   ✅ Working directory changed
   ✅ Index rebuilding
   ✅ Git repository detected
```

### Directory Statistics

**Shows:**
- **Total Files** - In directory
- **Total Directories** - Subdirectories
- **Total Size** - Disk usage
- **File Types** - Distribution

### Quick Actions

- **Open in Explorer** - System file browser
- **Open Terminal** - Command prompt here
- **Reset to Default** - Return to original directory
- **Recent Directories** - Quick switch to recent

### Directory History

**Last 10 working directories:**
- Path
- Last accessed
- Project name
- Quick switch button

---

## 9. Tool Call History

**Access:** Click "Tool Call History" in sidebar or press `Alt+9` or `Ctrl+H`

### Overview

Complete log of all API operations with detailed analytics.

### History Table

**Columns:**
- **#** - Call number (sequential)
- **Timestamp** - Exact time of call
- **Route** - API endpoint called
- **Method** - HTTP method (GET/POST)
- **Status** - Success/Error indicator
- **Duration** - Response time (ms)
- **Actions** - View details button

**Status Indicators:**
- ✅ **Success** - Green checkmark
- ❌ **Error** - Red X
- ⏱️ **Timeout** - Orange warning
- 🔄 **Pending** - Blue spinner

### Call Details Modal

**Click "View Details" to see:**
- **Request Details:**
  - Endpoint
  - Method
  - Parameters sent
  - Request body (if POST)
  - Headers

- **Response Details:**
  - Status code
  - Response body
  - Headers
  - Response time

- **Error Details** (if failed):
  - Error type
  - Error message
  - Stack trace
  - Debug hints

### Filtering

**Filter Options:**
- **Status** - Success/Error/All
- **Route** - Specific endpoint
- **Time Range** - Last hour/day/week
- **Method** - GET/POST

### Statistics Panel

**Shows:**
- **Total Calls** - All operations
- **Success Rate** - Percentage successful
- **Average Time** - Mean response time
- **Error Count** - Failed operations

**Top Routes:**
- Most frequently called
- Average time per route
- Success rate per route

### Export Options

- **Export CSV** - Download history
- **Export JSON** - Raw data export
- **Copy to Clipboard** - Selected entries

### Clear History

**Options:**
- Clear All
- Clear Errors Only
- Clear Before Date
- Keep Last N entries

---

## 10. System Logs

**Access:** Click "System Logs" in sidebar or press `Alt+10`

### Overview

Real-time system logs from FastAPI server.

### Log Stream

**Shows:**
- **Timestamp** - Exact time
- **Level** - DEBUG/INFO/WARNING/ERROR
- **Component** - Which module
- **Message** - Log content

**Log Levels:**
- 🐛 **DEBUG** - Gray (detailed info)
- ℹ️ **INFO** - Blue (normal operations)
- ⚠️ **WARNING** - Orange (potential issues)
- ❌ **ERROR** - Red (failures)
- 🔥 **CRITICAL** - Red background (severe)

### Filtering

**Filter logs by:**
- **Level** - Show only specific levels
- **Component** - Filter by module
- **Search** - Text search in messages
- **Time Range** - Last N minutes

### Log Actions

- **Pause** - Stop auto-scroll
- **Resume** - Continue streaming
- **Clear** - Remove all logs
- **Download** - Save as file
- **Share** - Copy to clipboard

### Auto-Refresh

**Settings:**
- **Refresh Rate** - 1s/5s/10s/30s
- **Max Lines** - Limit displayed logs
- **Auto-Scroll** - Follow newest logs

---

## ⌨️ Keyboard Shortcuts

### Global Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+H` or `Cmd+H` | Open Tool History modal |
| `Ctrl+R` or `Cmd+R` | Refresh current section |
| `Ctrl+K` or `Cmd+K` | Jump to Search section |
| `Esc` | Close modals/sidebar |

### Navigation Shortcuts

| Shortcut | Section |
|----------|---------|
| `Alt+1` | Dashboard |
| `Alt+2` | Search & Index |
| `Alt+3` | File Operations |
| `Alt+4` | Git & Sessions |
| `Alt+5` | Memory System |
| `Alt+6` | Project Explorer |
| `Alt+7` | Directory Browser |
| `Alt+8` | Working Directory |
| `Alt+9` | Tool Call History |

### Pro Tips

- Hold `Shift` while clicking nav items to open in background
- Double-click stat cards to drill down
- Right-click file paths to copy
- `Ctrl+F` in any section for in-page search

---

## 💡 Best Practices

### 1. Dashboard Organization

- **Check Dashboard First** - Get system overview
- **Monitor Tool Activity** - Watch for errors
- **Review API Stats** - Identify slow endpoints

### 2. Search Strategy

- **Start with Semantic** - Best for exploration
- **Use Text Search** - When you know exact terms
- **Symbol Search** - For navigation

### 3. File Operations

- **Read Before Edit** - Understand current state
- **Use AI Edit** - For complex changes
- **Review Quality Scores** - Aim for 80%+

### 4. Session Management

- **One Session Per Feature** - Keep focused
- **Descriptive Names** - Easy to identify
- **Merge Often** - Don't let sessions diverge

### 5. Memory Usage

- **Store as You Go** - Don't wait
- **Use Categories** - Makes retrieval easier
- **High Importance** - For critical info

---

## 🔧 Troubleshooting

### Dashboard Won't Load

**Problem:** Blank screen or loading forever

**Solutions:**
```
1. Check server is running:
   curl http://localhost:6789/health

2. Check browser console (F12):
   Look for JavaScript errors

3. Clear browser cache:
   Ctrl+Shift+Delete

4. Try different browser

5. Check firewall settings
```

### "Cannot Connect to API" Error

**Problem:** Connection indicator shows red

**Solutions:**
```
1. Verify FastAPI server running:
   Check terminal for "Uvicorn running"

2. Test API endpoint:
   curl http://localhost:6789/health

3. Check port 6789 not blocked:
   netstat -ano | findstr :6789

4. Restart server:
   Ctrl+C, then: python main.py

5. Check .env file configured
```

### Search Returns No Results

**Problem:** Empty results despite matching code

**Solutions:**
```
1. Rebuild index:
   Click "Rebuild Index" button

2. Check file patterns:
   Try broader pattern (*.*)

3. Wait for indexing:
   Large projects take time

4. Check working directory:
   Verify correct project loaded

5. Try text search:
   Semantic may miss exact matches
```

### File Edit Fails

**Problem:** "Edit failed" error

**Solutions:**
```
1. Check Gemini API key:
   Verify GEMINI_API_KEY in .env

2. Test API connection:
   curl https://generativelanguage.googleapis.com

3. Check rate limits:
   Free tier: 15 RPM, 1K RPD

4. Verify file exists:
   Use Read tab first

5. Simplify edit instructions:
   Try smaller changes
```

### Slow Performance

**Problem:** UI feels sluggish

**Solutions:**
```
1. Clear tool history:
   Click "Clear History"

2. Reduce auto-refresh:
   Settings > Refresh Interval

3. Close unused browser tabs

4. Check server resources:
   Task Manager > Python process

5. Restart browser

6. Restart FastAPI server
```

### Memory Not Saving

**Problem:** Stored memories don't appear

**Solutions:**
```
1. Check memory content:
   Must not be empty

2. Verify category selected

3. Click "Store Memory" button

4. Check for error notification

5. Refresh memory browser:
   Click refresh icon

6. Check server logs:
   System Logs section
```

### Session Operations Fail

**Problem:** Can't start/end sessions

**Solutions:**
```
1. Check Git installed:
   git --version

2. Verify Git repository:
   Check working directory is Git repo

3. Check for uncommitted changes:
   Git Status tab

4. Check branch permissions

5. Manually check Git:
   git status in terminal
```

---

## 📚 Additional Resources

- **API Documentation**: http://localhost:6789/docs
- **Setup Guide**: See `SETUP_GUIDE.md`
- **GitHub Issues**: https://github.com/danyQe/codebase-mcp/issues
- **Architecture Diagram**: `docs/architecture.png`

---

## 🎉 Tips for Success

1. **Explore Incrementally** - Try one section at a time
2. **Use Keyboard Shortcuts** - Faster workflow
3. **Monitor Tool History** - Learn API patterns
4. **Store Memories** - Build knowledge base
5. **Use Sessions** - Isolate experimental work
6. **Check Dashboard** - Stay informed
7. **Rebuild Index** - After major changes
8. **Review Logs** - Catch issues early

---

**Happy Coding! 🚀**

Built with ❤️ for developers by developers
