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