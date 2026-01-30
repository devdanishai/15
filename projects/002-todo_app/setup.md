Got it — we’ll build a fresh MERN **Todo app** in `projects/002-todo_app/` from zero, and I’ll give you the exact file/folder plan + code to paste. First I’ll quickly check what (if anything) already exists in that folder so the steps match your current state.

[1 tool called]

Great — `002-todo_app/` is basically empty (only `setup.txt`). Here’s the **from-scratch, step-by-step** build. You create folders/files and paste the code.

## Backend (Node + Express + MongoDB)

### Step 1: Create backend project + install packages
From `projects/002-todo_app/` run:

```bash
mkdir backend
cd backend
npm init -y
npm i express mongoose cors dotenv
npm i -D nodemon
```

Edit `backend/package.json` and add scripts:

```json
{
  "scripts": {
    "dev": "nodemon server.js",
    "start": "node server.js"
  }
}
```

### Step 2: Create backend folders/files
Inside `backend/` create:

```bash
mkdir config models routes controllers middleware
touch server.js .env
touch config/db.js
touch models/Todo.js
touch controllers/todoController.js
touch routes/todoRoutes.js
touch middleware/errorHandler.js
```

### Step 3: Add `.env`
`backend/.env`

```env
PORT=5000
MONGO_URI=mongodb://127.0.0.1:27017/todo_app_db
```

### Step 4: Mongo connection code
`backend/config/db.js`

```js
const mongoose = require("mongoose");

async function connectDB() {
  const uri = process.env.MONGO_URI;
  if (!uri) throw new Error("MONGO_URI missing in .env");

  await mongoose.connect(uri);
  console.log("MongoDB connected");
}

module.exports = connectDB;
```

### Step 5: Todo model
`backend/models/Todo.js`

```js
const mongoose = require("mongoose");

const todoSchema = new mongoose.Schema(
  {
    title: { type: String, required: true, trim: true },
    completed: { type: Boolean, default: false }
  },
  { timestamps: true }
);

module.exports = mongoose.model("Todo", todoSchema);
```

### Step 6: Controllers (logic)
`backend/controllers/todoController.js`

```js
const Todo = require("../models/Todo");

exports.getTodos = async (req, res) => {
  const todos = await Todo.find().sort({ createdAt: -1 });
  res.json(todos);
};

exports.createTodo = async (req, res) => {
  const title = (req.body.title || "").trim();
  if (!title) return res.status(400).json({ message: "title is required" });

  const todo = await Todo.create({ title });
  res.status(201).json(todo);
};

exports.updateTodo = async (req, res) => {
  const { id } = req.params;

  const updates = {};
  if (typeof req.body.title === "string") updates.title = req.body.title.trim();
  if (typeof req.body.completed === "boolean") updates.completed = req.body.completed;

  const todo = await Todo.findByIdAndUpdate(id, updates, { new: true });
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json(todo);
};

exports.deleteTodo = async (req, res) => {
  const { id } = req.params;

  const todo = await Todo.findByIdAndDelete(id);
  if (!todo) return res.status(404).json({ message: "Todo not found" });

  res.json({ message: "Deleted" });
};
```

### Step 7: Routes (API endpoints)
`backend/routes/todoRoutes.js`

```js
const express = require("express");
const {
  getTodos,
  createTodo,
  updateTodo,
  deleteTodo
} = require("../controllers/todoController");

const router = express.Router();

router.get("/", (req, res, next) => getTodos(req, res).catch(next));
router.post("/", (req, res, next) => createTodo(req, res).catch(next));
router.put("/:id", (req, res, next) => updateTodo(req, res).catch(next));
router.delete("/:id", (req, res, next) => deleteTodo(req, res).catch(next));

module.exports = router;
```

### Step 8: Error handler middleware
`backend/middleware/errorHandler.js`

```js
function errorHandler(err, req, res, next) {
  console.error(err);

  // common mongoose “bad id” case
  if (err.name === "CastError") {
    return res.status(400).json({ message: "Invalid id" });
  }

  res.status(500).json({ message: "Server error" });
}

module.exports = errorHandler;
```

### Step 9: `server.js` (wire everything)
`backend/server.js`

```js
const express = require("express");
const cors = require("cors");
require("dotenv").config();

const connectDB = require("./config/db");
const todoRoutes = require("./routes/todoRoutes");
const errorHandler = require("./middleware/errorHandler");

const app = express();

app.use(cors());
app.use(express.json());

app.get("/", (req, res) => {
  res.send("Todo API running");
});

app.use("/api/todos", todoRoutes);

// last middleware
app.use(errorHandler);

async function start() {
  await connectDB();
  const port = process.env.PORT || 5000;
  app.listen(port, () => console.log(`Server running on ${port}`));
}

start().catch((err) => {
  console.error("Failed to start:", err);
  process.exit(1);
});
```

### Step 10: Run backend + test
Run:

```bash
npm run dev
```

Test:

```bash
curl http://localhost:5000/
curl -X POST http://localhost:5000/api/todos -H "Content-Type: application/json" -d '{"title":"learn MERN"}'
curl http://localhost:5000/api/todos
```

If those work, backend is done.

---

## Frontend (React) — after backend works

### Step 11: Create frontend (Vite React)
From `projects/002-todo_app/`:

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm run dev
```

### Step 12: Frontend files you’ll create next
If you say “backend tests passed”, I’ll give you the exact code for:
- `frontend/src/api/todos.js` (fetch calls)
- `frontend/src/App.jsx` (UI + state)
- Components for add/toggle/delete

---

## One small choice (so I give you the right frontend code)
Do you want the frontend to use:
- **fetch** (no extra install), or
- **axios** (install one package, simpler API)?

Reply: `fetch` or `axios`.