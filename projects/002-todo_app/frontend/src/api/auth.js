import axios from "axios";

const baseURL = "http://localhost:5000/api";

export async function registerUser(payload) {
  const res = await axios.post(`${baseURL}/auth/register`, payload);
  return res.data; // { token, user }
}

export async function loginUser(payload) {
  const res = await axios.post(`${baseURL}/auth/login`, payload);
  return res.data; // { token, user }
}

export async function fetchMe() {
  const token = localStorage.getItem("token");
  const res = await axios.get(`${baseURL}/auth/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  return res.data; // { user }
}