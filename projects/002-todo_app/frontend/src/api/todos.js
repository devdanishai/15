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