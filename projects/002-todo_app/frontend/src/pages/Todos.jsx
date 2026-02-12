import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import TodoForm from "../components/TodoForm";
import TodoList from "../components/TodoList";
import { createTodo, deleteTodo, fetchTodos, updateTodo } from "../api/todos";

export default function Todos() {
  const navigate = useNavigate();
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
      if (e?.response?.status === 401) {
        localStorage.removeItem("token");
        navigate("/login");
        return;
      }
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

  function logout() {
    localStorage.removeItem("token");
    navigate("/login");
  }

  return (
    <div style={{ maxWidth: 520, margin: "40px auto", padding: 16 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h2 style={{ marginBottom: 12 }}>My Todos</h2>
        <button onClick={logout} style={{ padding: "8px 12px" }}>
          Logout
        </button>
      </div>

      <TodoForm onAdd={handleAdd} />

      {loading ? <p style={{ marginTop: 16 }}>Loading...</p> : null}
      {error ? <p style={{ marginTop: 16, color: "crimson" }}>{error}</p> : null}

      {!loading && !error ? (
        <TodoList todos={todos} onToggle={handleToggle} onDelete={handleDelete} />
      ) : null}
    </div>
  );
}

