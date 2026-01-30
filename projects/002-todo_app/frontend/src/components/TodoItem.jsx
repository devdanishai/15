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