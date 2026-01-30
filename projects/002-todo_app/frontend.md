Perfect — **axios** it is.

## Frontend (React + Axios) step-by-step

### Step 11: Create frontend (Vite React)
From `projects/002-todo_app/`:

```bash
npm create vite@latest frontend -- --template react
cd frontend
npm install
npm install axios
npm run dev
```

You should see Vite running (usually `http://localhost:5173`).

---

## Step 12: Create frontend file structure
Inside `frontend/src/` create:

```bash
mkdir api components
touch api/todos.js
touch components/TodoForm.jsx
touch components/TodoItem.jsx
touch components/TodoList.jsx
```

You’ll also edit:
- `frontend/src/App.jsx`
- `frontend/src/main.jsx` (usually already fine)

---

## Step 13: Axios API helper
`frontend/src/api/todos.js`

```js
import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api",
});

export async function fetchTodos() {
  const res = await api.get("/todos");
  return res.data;
}

export async function createTodo(title) {
  const res = await api.post("/todos", { title });
  return res.data;
}

export async function updateTodo(id, updates) {
  const res = await api.put(`/todos/${id}`, updates);
  return res.data;
}

export async function deleteTodo(id) {
  const res = await api.delete(`/todos/${id}`);
  return res.data;
}
```

---

## Step 14: UI Components

### `frontend/src/components/TodoForm.jsx`
```jsx
import { useState } from "react";

export default function TodoForm({ onAdd }) {
  const [title, setTitle] = useState("");

  async function handleSubmit(e) {
    e.preventDefault();
    const value = title.trim();
    if (!value) return;

    await onAdd(value);
    setTitle("");
  }

  return (
    <form onSubmit={handleSubmit} style={{ display: "flex", gap: 8 }}>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Add a todo..."
        style={{ flex: 1, padding: 10 }}
      />
      <button type="submit" style={{ padding: "10px 14px" }}>
        Add
      </button>
    </form>
  );
}
```

### `frontend/src/components/TodoItem.jsx`
```jsx
export default function TodoItem({ todo, onToggle, onDelete }) {
  return (
    <li
      style={{
        display: "flex",
        alignItems: "center",
        gap: 10,
        padding: "10px 0",
        borderBottom: "1px solid #eee",
      }}
    >
      <input
        type="checkbox"
        checked={todo.completed}
        onChange={() => onToggle(todo)}
      />

      <span
        style={{
          flex: 1,
          textDecoration: todo.completed ? "line-through" : "none",
          opacity: todo.completed ? 0.6 : 1,
        }}
      >
        {todo.title}
      </span>

      <button onClick={() => onDelete(todo)} style={{ padding: "6px 10px" }}>
        Delete
      </button>
    </li>
  );
}
```

### `frontend/src/components/TodoList.jsx`
```jsx
import TodoItem from "./TodoItem";

export default function TodoList({ todos, onToggle, onDelete }) {
  if (!todos.length) return <p style={{ marginTop: 16 }}>No todos yet.</p>;

  return (
    <ul style={{ listStyle: "none", padding: 0, marginTop: 16 }}>
      {todos.map((t) => (
        <TodoItem key={t._id} todo={t} onToggle={onToggle} onDelete={onDelete} />
      ))}
    </ul>
  );
}
```

---

## Step 15: App.jsx (connect UI ↔ API)
Replace `frontend/src/App.jsx` with:

```jsx
import { useEffect, useState } from "react";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";
import { createTodo, deleteTodo, fetchTodos, updateTodo } from "./api/todos";

export default function App() {
  const [todos, setTodos] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function load() {
    try {
      setError("");
      setLoading(true);
      const data = await fetchTodos();
      setTodos(data);
    } catch (e) {
      setError(e?.response?.data?.message || e.message || "Failed to load todos");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    load();
  }, []);

  async function handleAdd(title) {
    const created = await createTodo(title);
    setTodos((prev) => [created, ...prev]);
  }

  async function handleToggle(todo) {
    const updated = await updateTodo(todo._id, { completed: !todo.completed });
    setTodos((prev) => prev.map((t) => (t._id === updated._id ? updated : t)));
  }

  async function handleDelete(todo) {
    await deleteTodo(todo._id);
    setTodos((prev) => prev.filter((t) => t._id !== todo._id));
  }

  return (
    <div style={{ maxWidth: 520, margin: "40px auto", padding: 16 }}>
      <h2 style={{ marginBottom: 12 }}>Todo App</h2>

      <TodoForm onAdd={handleAdd} />

      {loading ? <p style={{ marginTop: 16 }}>Loading...</p> : null}
      {error ? <p style={{ marginTop: 16, color: "crimson" }}>{error}</p> : null}

      {!loading && !error ? (
        <TodoList todos={todos} onToggle={handleToggle} onDelete={handleDelete} />
      ) : null}
    </div>
  );
}
```

---

## Step 16: Run both servers
You need **two terminals**:

Backend (in `002-todo_app/backend`):
```bash
npm run dev
```

Frontend (in `002-todo_app/frontend`):
```bash
npm run dev
```

Open the frontend URL (usually `http://localhost:5173`) and test add/toggle/delete.

---

## If you get CORS or “Network Error”
Most common causes:
- backend not running on `5000`
- MongoDB not running
- wrong `baseURL` in `api/todos.js`

If you paste the exact error text, I’ll tell you exactly what to fix.