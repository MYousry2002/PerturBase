// src/services/api.js
import axios from 'axios';

// We set baseURL to the subpath so that adding "/api/..." becomes
// "/students_25/Team10/PerturBase/main/api/..."
const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || '/students_25/Team10/PerturBase/main',
});

export default api;