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